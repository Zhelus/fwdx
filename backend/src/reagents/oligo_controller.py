# oligo_controller.py

from flask import Blueprint, jsonify, request
from .oligo_service import create_oligo, archive_oligo, get_all_active_oligos, get_oligo_by_id, get_all_oligos
from ...definitions import API_VERSION

bp = Blueprint('oligos', __name__)
# Endpoint to create a new oligo
# Example query: POST http://127.0.0.1:5000/v1/oligos
@bp.route(f'/{API_VERSION}/oligos', methods=['POST'])
def api_create_oligo():
    oligo_data = request.get_json()
    document = create_oligo(oligo_data)
    return f"Oligo created is: {document}", 201



# Endpoint to archive an oligo by its ID
# Example query: PATCH http://127.0.0.1:5000/v1/oligos/<oligo_id>/archive
@bp.route(f'/{API_VERSION}/oligos/<string:oligo_id>/archive', methods=['DELETE'])
def api_archive_oligo(oligo_id):
    document = archive_oligo(oligo_id)
    return f"Oligo archived: {document}", 200

# Example query: GET http://127.0.0.1:5000/v1/oligos/active
@bp.route(f'/{API_VERSION}/oligos', methods=['GET'])
def api_get_all_active_oligos():
    oligos = get_all_active_oligos()
    # Convert each oligo's '_id' field to a string for JSON serialization
    for oligo in oligos:
        oligo = _object_id_to_string(oligo)
    return jsonify({'oligos': oligos}), 200

@bp.route(f'/{API_VERSION}/oligos/all', methods=['GET'])
def api_get_all_oligos():
    oligos = get_all_oligos()
    # Convert each oligo's '_id' field to a string for JSON serialization
    for oligo in oligos:
        oligo = _object_id_to_string(oligo)
    return jsonify({'oligos': oligos}), 200
# Endpoint to get a single oligo by its ID
# Example query: GET http://127.0.0.1:5000/v1/oligos/<oligo_id>
@bp.route(f'/{API_VERSION}/oligos/<string:oligo_id>', methods=['GET'])
def api_get_oligo_by_id(oligo_id):
    """
    Endpoint to get a single oligo by its ID.
    Example query: GET http://127.0.0.1:5000/v1/oligos/<oligo_id>
    """
    try:
        # Fetch the oligo using the service
        oligo = get_oligo_by_id(oligo_id)
        if oligo:
            # Convert '_id' to string for JSON serialization
            oligo = _object_id_to_string(oligo)
            return jsonify({"message": "Oligo found", "oligo": oligo}), 200
        else:
            return jsonify({"error": "Oligo not found"}), 404
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


"""
Helper method to translate a report's MongoDB 'ObjectId' to a string (needed to convert report data to JSON)
    - Inputs: report (dict with '_id' as an ObjectId)
    - Outputs: report (dict with '_id' as a string)
"""
def _object_id_to_string(oligo):
        oligo['_id'] = str(oligo['_id'])
        return oligo