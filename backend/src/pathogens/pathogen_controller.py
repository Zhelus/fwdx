from flask import Blueprint, request

from backend.definitions import API_VERSION
from backend.src.pathogens.pathogen_service import create_pathogen_document, update_pathogen_document, \
    delete_pathogen_document, get_pathogen_document

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


# example query: GET -> http://127.0.0.1:5000/v1/pathogen?limit=10
# example query: GET -> http://127.0.0.1:5000/v1/pathogen?id=12345

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


# example query: DELETE -> http://127.0.0.1:5000/v1/pathogen/NC_045512.2
@bp.route(f'/{API_VERSION}/pathogen/', methods=['DELETE'])
def delete_pathogen():
    return delete_pathogen_document(request)
