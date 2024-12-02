import time
from time import perf_counter

import numpy as np
from flask import request, jsonify
from datetime import datetime

from backend.src.smith_wn.smith_wn import smith_waterman_alignment_iupac
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()

def convert_np_types(obj):
    if isinstance(obj, np.int64):
        return int(obj)
    elif isinstance(obj, dict):
        return {key: convert_np_types(value) for key, value in obj.items()}
    elif isinstance(obj, list):
        return [convert_np_types(item) for item in obj]
    return obj

def smith_wn_alignment(flask_request: request):
    data = flask_request.get_json()

    # Get the important IDs from the request JSON
    print(data)
    data = data['data']
    print(data)
    taxonomic_id = data['NCBI_taxonomy_ID']
    oligo_objects = data['product']['oligos']
    metadata = data['product']['metadata']
    # taxonomic_id = "10632"
    # oligos = ["AATGCAACAGTGCAATCTCA", "GGCCCAACACCAAATTCATC", "TTGGGTTCCTGATCCCACCAG", "AAGTACATGCCCATAAGCAA", "AGACAGCCATATGCAGTAG", "AAACCTGCTTAGTTTCTTCTGGTTCTT"]
    # metadata = "Extra Data"

    # pathogen_document = {
    #     "_id":{"$oid":"673b6b606c85a25ce15d3da8"},
    #     "taxonomicID":{"$numberInt":"10632"},
    #     "accessionID":"J02226.1",
    #     "genomic_sequence":"gcctcggcctcctgtatatataaaaaaaagggaagggatggctgccagccaagcatgagctcatacctagggagccaaccagctaacagccagtaaacaaagcacaaggctgtatatataaaaaaaagggaagggatggctgccagccaagcatgagctcatacctagggagccaaccagctaacagccagtaaacaaagcacaaggggaagtggaaagcagccaagggaacatgttttgcgagccagagctgttttggcttgtcaccagctggccatggttcttcgccagctgtcacgtaaggcttctgtgaaagttagtaaaacctggagtggaactaaaaaaagagctcaaaggattttaatttttttgttagaatttttgctggacttttgcacaggtgaagacagtgtagacgggaaaaaaagacagagacacagtggtttgactgagcagacatacagtgctttgcctgaaccaaaagctacataggtaagtaatgtttttttttgtgttttcaggttcatgggtgccgcacttgcacttttgggggacctagttgctactgtttctgaggctgctgctgccacaggattttcagtagctgaaattgctgctggagaggctgctgctactatagaagttgaaattgcatcccttgctactgtagaggggattacaagtacctctgaggctatagctgctataggccttactcctgaaacatatgctgtaataactggagctccgggggctgtagctgggtttgctgcattggttcaaactgtaactggtggtagtgctattgctcagttgggatatagattttttgctgactgggatcataaagtttcaacagttgggctttttcagcagccagctatggctttacaattatttaatccagaagactactatgatattttatttcctggagtgaatgcctttgttaacaatattcactatttagatcctagacattggggcccgtccttgttctccacaatctcccaggctttttggaatcttgttagagatgatttgccagccttaacctctcaggaaattcagagaagaacccaaaaactatttgttgaaagtttagcaaggtttttggaagaaactacttgggcaatagttaattcaccagctaacttatataattatatttcagactattattctagattgtctccagttaggccctctatggtaaggcaagttgcccaaagggagggaacctatatttcttttggccactcatacacccaaagtatagatgatgcagacagcattcaagaagttacccaaaggctagatttaaaaaccccaaatgtgcaatctggtgaatttatagaaagaagtattgcaccaggaggtgcaaatcaaagatctgctcctcaatggatgttgcctttacttttagggttgtacgggactgtaacacctgctcttgaagcatatgaagatggccccaacaaaaagaaaaggagaaaggaaggaccccgtgcaagttccaaaacttcttataagaggaggagtagaagttctagaagttaaaactggggttgactcaattacagaggtagaatgctttttaactccagaaatgggtgacccagatgagcatcttaggggttttagtaagtcaatatctatatcagatacatttgaaagtgactccccaaatagggacatgcttccttgttacagtgtggccagaattccactacccaatctaaatgaggatctaacctgtggaaatatactcatgtgggaggctgtgaccttaaaaactgaggttataggggtgacaagtttgatgaatgtgcactctaatgggcaagcaactcatgacaatggtgcagggaagccagtgcagggcaccagctttcattttttttctgttgggggggaggctttagaattacagggggtgctttttaattacagaacaaagtacccagatggaacaatttttccaaagaatgccacagtgcaatctcaagtcatgaacacagagcacaaggcgtacctagataagaacaaagcatatcctgttgaatgttgggttcctgatcccaccagaaatgaaaacacaagatattttgggacactaacaggaggagaaaatgttcctccagttcttcatataacaaacactgccacaacagtgttgcttgatgaatttggtgttgggccactttgcaaaggtgacaacttatacttgtcagctgttgatgtctgtggcatgtttacaaacaggtctggttcccagcagtggagaggactctccagatattttaaggtgcagctaaggaaaaggagggttaaaaacccctacccaatttctttccttcttactgatttaattaacagaaggactcctagagttgatgggcagcctatgtatggcatggatgctcaagtagaggaggttagagtttttgagggaacagaggagcttccaggggacccagacatgatgagatacgttgacaaatatggacagttgcagacaaaaatgctgtaatcaaaagcctttattgtaatatgcagtacattttaataaagtataaccagctttacttaacagttgcagttattttgggggaggggtctttggttttttgaaacattgaaagcctttacagatgtgaaaagtgcagttttcctgtgtgtctgcaccagaggcttctgagacctgggaaaagcattgtgattgtgattcagtgcttgatccatgtccagagtcttctgcttcagaatcttcctctctaggaaagtcaagaatgggtctccccataccaacattagctttcatagtagaaaatgtatacatgcttatttctaaatccagcctttctttccactgcacaatcctctcatgaatggcagctgcaaagtcagcaactggcctaaaccagattaaaagcaaaagcaaagtcataccactttgcaaaatccttttttctagcaaatactcagagcagcttagtgattttctcaggtaggcctttggtctaaaatctatctgccttacaaatctggcctgtaaagttctaggcactgaatattcattcatggttacaattccaggtggaaacacctgtgttcttttgttttggtgttttctctctaaattaacttttacacttccatctaagtaatctcttaagcaatcaaggttgcttatgccatgccctgaaggtaaatcccttgactctgcaccagtgccttttacatcctcaaatacaaccataaactgatctatacccactcctaattcaaagtttaatctttctaatggcatattaacatttaatgactttcccccacagagatcaagtaaagctgcagctaaagtagttttgccactgtctattggccccttgaatagccagtaccttttttttggaatgtttaatacaatgcattttagaaagtcataaataacagtgtccatttgaggcagcaagcaatgaatccaggccaccccagccatatattgctctaaaacagcattgccatgtgccccaaaaattaagtccattttatcaagcaagaaattaaacctttcaactaacatttcttctctggtcatgtggatgctgtcaaccctttgtttggctgctacagtatcaacagcctgctggcaaatgcttttttgatttttgctatctgcaaaaatttgggcattataatagtgtttttcatgatggttaaagtgatttggctgatcctttttttcacattttttgcattgctgtgggttttcctgaaagtctaagtacatgcccataagcaaaaaaacatcctcacacttggtttccaaggcatactgtgtaactaatttccatgaaacctgcttagtttcttctggttcttctgggttaaagtcatgctccttaaggcccccctgaatactttcttccactactgcatatggctgtctacacagggcactataaaacaagtattccttattcacacctttacaaattaaaaaactaaaggtacatagtttttgacagtagttattaattgctgacactctatgtctatgtggtgttaagaaaaacaaaatattatgacccccaaaaccatgtctacttataaaagttacagaatatttttccataagtttcttatataaaatttgagctttttctttagtggtatacacagcaaaagaagcaacagttctattactaaacacagcttgactgaggaatgcatgcagatctacaggaaagtctttagggtcttctaccttttttttctttttaggtggggtagagtgttgggatcctgtgttttcatcatcactggcaaacatttcttcatggcaaaacaggtcttcatcccacttctcattaaatgtattccaccaggattcccattcatctgttccataggttggcacctaaaaaaaaacaattaagtttattgtaaaaaacaaaatgccctgcaaaagaaaaatagtggtttaccttaaagctttagatccctgtagggggtgtctccaagaactttctcccagcaatgaagagcttcttgggttaagtcacacccaaaccattgtctgaagcaatcaaagcaatagcaatctatccacacaagtgggctgcttcttaaaaattttctgtttctatgccttaattttagcatgcacattaaacaggggcaatgcactgaaggattagtggcacagttaggccattccttgcaataaagggtatcagaattaggaggaaaatcacaaccaacctctgaactattccatgtaccaaaatcaggctgatgagcaacttttacaccttgttccatttttttatataaaaaattcattctcttcatcttgtcttcgtccccacctttatcagggtggagttctttgcattttttcagataagcttttctcatgacaggaatgttcccccatgcagacctatcaaggcctaataaatccataagctccatggattcctccctattcagcactttgtccattttagctttttgcagcaaaaaattactgcaaaaaagggaaaaacaagggaatttccctggcctcctaaaaagcctccacgcccttactacttctgagtaagcttggaggcggaggcg",
    #     "common_name":"JC polyomavirus (JCPyV)",
    #     "gcf":"",
    #     "collection_date":"",
    #     "fwdxdatabase_import_date":"2024-11-18",
    #     "organism":"JC polyomavirus",
    #     "mol_type":"genomic DNA",
    #     "strain":"Mad1"
    # }

    # pathogen_document = connector.fetch_document({"taxonomicID": taxonomic_id}, CollectionType.PATHOGENS)
    pathogens_cursor = connector.fetch_all_documents(CollectionType.PATHOGENS, filter={'taxonomicID': taxonomic_id})
    print(pathogens_cursor)
    pathogens = []
    for pathogen in pathogens_cursor:
        fmtd_pathogen = _object_id_to_string(pathogen)
        pathogens.append(fmtd_pathogen)
    print(f"\n\n\n{pathogens}")
    # genomic_sequence = pathogen_document['genomic_sequence'].upper()
    # pathogen_name = pathogen_document['common_name']
    # pathogen_accession = pathogen_document['accessionID']
    # pathogens = []
    # pathogens.append(pathogen_document)
    # TODO eventually the oligos is going to be a list of Oligo objects that we need to parse out the sequences from it
    # TODO For now I am just going to pass it as sequences for now

    # Pass the Genome and Oligos to the algorithm
    start_time = time.perf_counter()
    results = []
    for pathogen in pathogens:
        print("\n\n")
        print(pathogen)
        genomic_sequence = pathogen['genomic_sequence'].upper()
        pathogen_name = pathogen['common_name']
        pathogen_accession = pathogen['accessionID']
        pathogen_date = pathogen['collection_date']
        for oligo in oligo_objects:
            alignment1, alignment2, match_line, start_index, end_index, score = smith_waterman_alignment_iupac(genomic_sequence, oligo['sequence'])

            # oligo_result = {
            #     "oligoID": "oligoIDHere",
            #     "oligoName": "oligoNameHere",
            #     "oligoSequence": alignment2,
            #     "mismatchLines": match_line,
            #     "pathogenSubsequence": alignment1,
            #     "start_index": start_index,
            #     "end_index": end_index,
            #     "score": score,
            #     "pathogenName": pathogen_name,
            #     "pathogenAccessionID": pathogen_accession,
            #     "metadata": metadata
            # }

            oligo_result = {
                "oligoID":"oligoIDHere",
                "oligoName": oligo['oligoName'],
                "oligoSequence": alignment2,
                "mismatchLines": match_line,
                "pathogenSequence": alignment1,
                "pathogenAccessionID": pathogen_accession,
                "pathogenCommonName": pathogen_name,
                "pathogenLocation": "USA",
                "start_index": start_index, 
                "end_index": end_index,
                "score": score,
                "mismatchCount": match_line.count("X")
            }

            if len(pathogen_date) > 0:
                oligo_result['pathogenCollectionDate'] = pathogen_date
            else: 
                oligo_result['pathogenCollectionDate'] = "None"


            results.append(oligo_result)

    end_time = time.perf_counter()
    print(end_time - start_time)
    # response_data = {
    #     "product": {
    #         "NCBI_taxonomy_ID": taxonomic_id,  # Example genome_id
    #         "oligos": results
    #     }
    # }

    response_data = {
        "report_id": "1234567",
        "creation_date": datetime.today().strftime('%m/%d/%Y'),
        "schedule_id": "None",
        "report_title": data['report_title'],
        "product_name": data['product_name'],
        "product_id": data['product_id'],
        "pathogen_id": taxonomic_id,
        "pathogen_name": data['pathogen_name'],
        "mismatches": results
    }
    print(f"\nRESPONSE DATA\n{response_data}")
    response_data = convert_np_types(response_data)
    connector.upload_document(document=response_data, collection=CollectionType.REPORTS)
    response_data = _object_id_to_string(response_data)
    print(f"\nRESPONSE DATA AFTER\n{response_data}")
    return jsonify(response_data), 200

def _object_id_to_string(document):
        document['_id'] = str(document['_id'])
        return document