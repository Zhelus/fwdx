from flask import Blueprint, request, jsonify

from backend.definitions import API_VERSION
from .pathogen_service import create_pathogen_document, update_pathogen_document, \
    delete_pathogen_document, get_pathogen_document, get_all_pathogens, \
    get_unique_taxonomic_ids, _object_id_to_string, get_pathogen_by_taxonomic_id, \
    process_pathogen_data

"""
This file defines the API endpoints for pathogen use cases.
Make sure the blueprint is attached in "app.py"

All relevant information for the request is in the body of the request NOT in the URL endpoint definition.
See Postman for example implementations.
"""

bp = Blueprint('pathogen', __name__)


# example query: POST -> http://127.0.0.1:5000/v1/pathogen/
@bp.route(f'/{API_VERSION}/pathogen', methods=['POST'])
def create_pathogen():
    return create_pathogen_document(request)


# Query one document:
# example query: GET -> http://127.0.0.1:5000/v1/pathogen?id=12345

# Query one or more documents
# example query: GET -> http://127.0.0.1:5000/v1/pathogen?limit=10

# Combined GET endpoint for a single pathogen or multiple pathogens
# For example:
#   - ?limit=10 get X number of documents
#   - ?id=<id> to filter by name
@bp.route(f'/{API_VERSION}/pathogen/', methods=['GET'])
def get_pathogen():
    return get_pathogen_document(request)


# example query: PUT -> http://127.0.0.1:5000/v1/pathogen/
@bp.route(f'/{API_VERSION}/pathogen/', methods=['PUT'])
def update_pathogen():
    return update_pathogen_document(request)


# example query: DELETE -> http://127.0.0.1:5000/v1/pathogen?id=12345
@bp.route(f'/{API_VERSION}/pathogen/', methods=['DELETE'])
def delete_pathogen():
    return delete_pathogen_document(request)
##
@bp.route(f'/{API_VERSION}/pathogens/all', methods=['GET'])
def api_get_all_pathogens():
    #flask endpoint constructor to get all pathogens
    try:
        pathogens = get_all_pathogens()
        for pathogen in pathogens:
            pathogen = _object_id_to_string(pathogen)
        
        #this removes the genomic_sequence to make reading logs easier
        #Should be removed in next sprint along with geneSequences
        pathogens_without_geneSeq = [
        {key: value for key, value in pathogen.items() if key != "genomic_sequence"}
        for pathogen in pathogens ]
        pathogenTable = process_pathogen_data(pathogens_without_geneSeq)
        #pathogenTable = pathogens_without_geneSeq
        #uniqueTaxIDs = get_unique_taxonomic_ids(pathogens_without_geneSeq)
        #pathogenTable = uniqueTaxIDs
    # Print the modified list
        #print(f"Returning pathogens: {pathogenTable}")
        return jsonify({"pathogens": pathogenTable}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@bp.route(f'/{API_VERSION}/pathogens/<taxonomic_id>', methods=['GET'])
def api_get_pathogen_by_taxonomic_id(taxonomic_id):
    """
    Flask endpoint to get pathogen details by taxonomicID
    """
    try:
        # Fetch pathogen details from the service layer
        pathogen = get_pathogen_by_taxonomic_id(taxonomic_id)

        if not pathogen:
            return jsonify({"error": f"No pathogen found with taxonomicID {taxonomic_id}"}), 404

        # Remove unwanted fields (if needed) and return pathogen
        pathogen = {key: value for key, value in pathogen.items() if key != "genomic_sequence"}

        return jsonify({"pathogen": pathogen}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500





