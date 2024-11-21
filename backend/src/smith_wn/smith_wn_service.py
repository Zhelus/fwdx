import time
from time import perf_counter

import numpy as np
from flask import request, jsonify

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
    taxonomic_id = data['NCBI_taxonomy_ID']
    oligos = data['product']['oligos']
    metadata = data['product']['metadata']

    pathogen_document = connector.fetch_document({"taxonomicID": taxonomic_id}, CollectionType.PATHOGENS)
    genomic_sequence = pathogen_document['genomic_sequence'].upper()
    pathogen_name = pathogen_document['common_name']
    pathogen_accession = pathogen_document['accessionID']
    # TODO eventually the oligos is going to be a list of Oligo objects that we need to parse out the sequences from it
    # TODO For now I am just going to pass it as sequences for now

    # Pass the Genome and Oligos to the algorithm
    start_time = time.perf_counter()
    results = []
    for oligo in oligos:
        alignment1, alignment2, match_line, start_index, end_index, score = smith_waterman_alignment_iupac(genomic_sequence, oligo)

        oligo_result = {
            "oligoID": "oligoIDHere",
            "oligoName": "oligoNameHere",
            "oligoSequence": alignment2,
            "mismatchLines": match_line,
            "pathogenSubsequence": alignment1,
            "start_index": start_index,
            "end_index": end_index,
            "score": score,
            "pathogenName": pathogen_name,
            "pathogenAccessionID": pathogen_accession,
            "metadata": metadata
        }

        results.append(oligo_result)

    end_time = time.perf_counter()
    print(end_time - start_time)
    response_data = {
        "product": {
            "NCBI_taxonomy_ID": taxonomic_id,  # Example genome_id
            "oligos": results
        }
    }

    response_data = convert_np_types(response_data)
    return jsonify(response_data), 200