from pymongo.results import InsertOneResult, UpdateResult
from flask import request, jsonify

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()


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
    accession_id = flask_request.get_json()["accession_id"]

    result = connector.delete_document({"accession_id": accession_id}, CollectionType.PATHOGENS)

    if result is not None:
        return f"Successfully deleted pathogen with accession_id: {accession_id}", 200
    else:
        return "Failed to delete pathogen document", 400
