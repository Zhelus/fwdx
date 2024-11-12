from flask import Blueprint, request
from .product_service import create_product, get_product, update_product, delete_product, add_product_version, set_active_version
from ...definitions import API_VERSION

bp = Blueprint('products', __name__)

# Endpoint to create a new product
# Example query: POST http://127.0.0.1:5000/v1/products
@bp.route(f'/{API_VERSION}/products', methods=['POST'])
def api_create_product():
    product_data = request.get_json()
    document = create_product(product_data)
    return f"Product created is: {document}", 201


# Endpoint to get a product by its ID
# Example query: GET http://127.0.0.1:5000/v1/products/6730f02aec38fbfe063398da
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['GET'])
def api_get_product(product_id):
    document = get_product(product_id)
    return f"Product returned is: {document}", 200


# Endpoint to update a product by its ID
# Example query: PUT http://127.0.0.1:5000/v1/products/<product_id>
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['PUT'])
def api_update_product(product_id):
    product_data = request.get_json()
    document = update_product(product_id, product_data)
    return f"Product updated to: {document}", 200


# Endpoint to delete a product by its ID
# Example query: DELETE http://127.0.0.1:5000/v1/products/<product_id>
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['DELETE'])
def api_delete_product(product_id):
    document = delete_product(product_id)
    return f"Product deleted is: {document}", 204


# Endpoint to add a new version to a product
# Example query: POST http://127.0.0.1:5000/v1/products/<product_id>/versions
@bp.route(f'/{API_VERSION}/products/<string:product_id>/versions', methods=['POST'])
def api_add_product_version(product_id):
    oligos = request.get_json().get('oligos')
    document = add_product_version(product_id, oligos)
    return f"New version added to product: {document}", 201


# Endpoint to set an active version for a product
# Example query: PATCH http://127.0.0.1:5000/v1/products/<product_id>/active_version
@bp.route(f'/{API_VERSION}/products/<string:product_id>/active_version', methods=['PATCH'])
def api_set_active_version(product_id):
    version_index = request.get_json().get('versionIndex')
    document = set_active_version(product_id, version_index)
    return f"Active version set for product: {document}", 200
