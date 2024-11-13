from flask import Blueprint, request
from .oligo_service import create_oligo, update_oligo
from ...definitions import API_VERSION

bp = Blueprint('oligos', __name__)

# Endpoint to create a new oligo and add it to the latest version of a product
# Example query: POST http://127.0.0.1:5000/v1/oligos/<product_id>
@bp.route(f'/{API_VERSION}/oligos/<string:product_id>', methods=['POST'])
def api_create_oligo(product_id):
    oligo_data = request.get_json()
    document = create_oligo(product_id, oligo_data)
    return f"Oligo added to product: {document}", 201

# Endpoint to update an existing oligo within a product
# Example query: PUT http://127.0.0.1:5000/v1/oligos/<product_id>/<oligo_id>
@bp.route(f'/{API_VERSION}/oligos/<string:product_id>/<string:oligo_id>', methods=['PUT'])
def api_update_oligo(product_id, oligo_id):
    oligo_data = request.get_json()
    document = update_oligo(product_id, oligo_id, oligo_data)
    return f"Oligo updated in product: {document}", 200
