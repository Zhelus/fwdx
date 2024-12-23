from pymongo.results import InsertOneResult, UpdateResult
from flask import request, jsonify

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector(force_ssl=True)


def create_pathogen_document(flask_request: request):
    # TODO: make sure we do not create multiple documents with the same accession_id
    result: InsertOneResult = connector.upload_document(flask_request.get_json(), CollectionType.PATHOGENS)

    if result.inserted_id is not None:
        return "Created pathogen document", 200
    else:
        return "Failed to create pathogen document", 400


def get_pathogen_document(flask_request: request):
    limit_arg = flask_request.args.get('limit', type=int)
    id_arg = flask_request.args.get('id', type=str)

    if id_arg is not None:
        # query single document by accession_id
        result = connector.fetch_document({"accession_id": id_arg}, CollectionType.PATHOGENS)

        if result is not None:
            result['_id'] = str(result['_id'])
            return jsonify(result), 200
        else:
            return f"Failed to find pathogen with accession_id: {id_arg}", 400
    elif limit_arg is not None:
        # query limit_arg number of pathogen documents
        result = connector.fetch_documents(limit_arg, CollectionType.PATHOGENS)

        if result is not None:
            documents = []
            for document in result:
                document['_id'] = str(document['_id'])
                documents.append(document)

            return documents, 200

        else:
            return f"Failed to find {limit_arg} pathogen(s)", 400

    return "Incorrectly formatted query. Specify id or limit parameter.", 400


def update_pathogen_document(flask_request: request):
    mongodb_filter = {"accession_id": flask_request.get_json()["accession_id"]}

    result: UpdateResult = connector.update_document(mongodb_filter, {"$set": flask_request.get_json()},
                                                     CollectionType.PATHOGENS)

    if result.modified_count > 0:
        return f"{result.modified_count} pathogen document(s) updated", 200
    else:
        return "Failed to update pathogen document", 400


def delete_pathogen_document(flask_request: request):
    id_arg = flask_request.args.get('id', type=str)

    if id_arg is None:
        return "Failed to delete pathogen, no ID found in request", 400

    result = connector.delete_document({"accession_id": id_arg}, CollectionType.PATHOGENS)

    if result is not None:
        return f"Successfully deleted pathogen with accession_id: {id_arg}", 200
    else:
        return "Failed to delete pathogen document", 400
    

def get_all_pathogens():

    # Call fetch_all_documents from MongoDBConnector
    cursor = connector.fetch_all_documents(CollectionType.PATHOGENS)
    # Convert MongoDB cursor to a list
    return list(cursor)

#???
def get_unique_taxonomic_ids(pathogens):
    seen = set()
    unique_pathogens = []
    for pathogen in pathogens:
        if pathogen['taxonomicID'] not in seen:
            seen.add(pathogen['taxonomicID'])
            unique_pathogens.append(pathogen)
    return unique_pathogens

def process_pathogen_data(pathogens):

    taxonomic_counts = {}
    
    # Loop through pathogens to count taxonomicID occurrences and store common_name
    for pathogen in pathogens:
        taxonomicID = pathogen.get('taxonomicID')
        common_name = pathogen.get('common_name', 'Unknown')

        if taxonomicID in taxonomic_counts:
            taxonomic_counts[taxonomicID]['count'] += 1
        else:
            taxonomic_counts[taxonomicID] = {
                'taxonomicID': taxonomicID,
                'common_name': common_name,
                'count': 1
            }
    
    # Convert the dictionary to a list
    unique_taxonomic_data = list(taxonomic_counts.values())
    return unique_taxonomic_data

"""
def get_pathogen_by_taxonomic_id(taxonomic_id):
    query = {"taxonomicID": taxonomic_id}
    # Use fetch_all_documents to retrieve all non-archived oligos
    return list(connector.fetch_all_documents(CollectionType.PATHOGENS, query))
"""

def get_pathogen_by_taxonomic_id(taxonomic_id):
    query = {"taxonomicID": int(taxonomic_id)}  # Cast taxonomic_id to int if stored as an integer
    try:
        # Fetch all matching documents
        results = list(connector.fetch_all_documents(CollectionType.PATHOGENS, query))
        #removes genomic sequence from fetch
        results = remove_genomic_sequence(results)
        if not results:
            print(f"DEBUG: No pathogens found for taxonomicID: {taxonomic_id}")
            return None
        
        # Convert ObjectId to string for each document
        for result in results:
            result["_id"] = str(result["_id"])
        
        print(f"DEBUG: Found pathogens: {results}")
        return results
    except Exception as e:
        print(f"DEBUG: Error retrieving pathogens: {e}")
        raise
def remove_genomic_sequence(data):
    if isinstance(data, list):
        return [{key: value for key, value in item.items() if key != "genomic_sequence"} for item in data]
    elif isinstance(data, dict):
        return {key: value for key, value in data.items() if key != "genomic_sequence"}
    else:
        raise TypeError("Input data must be a dictionary or a list of dictionaries.")
    
def _object_id_to_string(pathogen):
        pathogen['_id'] = str(pathogen['_id'])
        return pathogen

