from flask import Blueprint, jsonify, request
from .product_service import (
    create_product, get_product, update_product, delete_product,
    add_product_version, set_active_version, get_all_products,get_all_products_with_oligo_names
)
from ...definitions import API_VERSION


bp = Blueprint('products', __name__)

# Endpoint to create a new product
# Example query: POST http://127.0.0.1:5000/v1/products
@bp.route(f'/{API_VERSION}/products', methods=['POST'])
def api_create_product():
    """
    Creates a new product.
    """
    try:
        product_data = request.get_json()
        if not product_data or "name" not in product_data:
            return jsonify({"error": "Product name is required"}), 400

        document = create_product(product_data)
        document = _object_id_to_string(document)
        return jsonify({"message": "Product created successfully", "product": document}), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



# Endpoint to get a product by its ID
# Example query: GET http://127.0.0.1:5000/v1/products/<product_id>
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['GET'])
def api_get_product(product_id):
    """
    Retrieves a product by its ID.
    """
    try:
        document = get_product(product_id)
        if document:
            document =_object_id_to_string(document)
            return jsonify({"message": "Product retrieved successfully", "product": document}), 200
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Endpoint to get all products
# Example query: GET http://127.0.0.1:5000/v1/products
@bp.route(f'/{API_VERSION}/products', methods=['GET'])
def api_get_all_products():
    products = get_all_products()
    # Convert each oligo's '_id' field to a string for JSON serialization
    for product in products:
        product = _object_id_to_string(product)
    return jsonify({'products': products}), 200


@bp.route(f'/{API_VERSION}/products_by_oligo_names', methods=['GET'])
def api_get_all_products_with_oligo_names():
    """
    Fetch all products with oligo names instead of IDs.
    """
    try:
        products = get_all_products_with_oligo_names()
        # Convert ObjectIds to strings for JSON serialization
        products = [_object_id_to_string(product) for product in products]
        return jsonify({"products": products}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Endpoint to update a product by its ID
# Example query: PUT http://127.0.0.1:5000/v1/products/<product_id>
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['PUT'])
def api_update_product(product_id):
    """
    Updates a product by its ID.
    """
    try:
        product_data = request.get_json()
        document = update_product(product_id, product_data)
        document = _object_id_to_string(document)
        return jsonify({"message": "Product updated successfully", "product": document}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Endpoint to delete a product by its ID
# Example query: DELETE http://127.0.0.1:5000/v1/products/<product_id>
@bp.route(f'/{API_VERSION}/products/<string:product_id>', methods=['DELETE'])
def api_delete_product(product_id):
    """
    Deletes a product by its ID.
    """
    try:
        result = delete_product(product_id)
        if result:
            return jsonify({"message": "Product deleted successfully"}), 204
        else:
            return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Endpoint to add a new version to a product
# Example query: POST http://127.0.0.1:5000/v1/products/<product_id>/versions
@bp.route(f'/{API_VERSION}/products/<string:product_id>/versions', methods=['POST'])
def api_add_product_version(product_id):
    """
    Adds a new version to a product and updates the active version index.
    """
    try:
        oligos = request.get_json().get('oligos')
        if not oligos or not isinstance(oligos, list):
            return jsonify({"error": "Invalid or missing 'oligos' field. Must be a non-empty list."}), 400

        document = add_product_version(product_id, oligos)
        if document:
            document = _object_id_to_string(document)
            return jsonify({
                "message": "New version added successfully, and active version index updated.",
                "product": document
            }), 201
        else:
            return jsonify({"error": "Product not found"}), 404
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500



# Endpoint to set an active version for a product
# Example query: PATCH http://127.0.0.1:5000/v1/products/<product_id>/active_version
@bp.route(f'/{API_VERSION}/products/<string:product_id>/active_version', methods=['PATCH'])
def api_set_active_version(product_id):
    """
    Sets the active version for a product.
    """
    try:
        version_index = request.get_json().get('versionIndex')
        document = set_active_version(product_id, version_index)
        document = _object_id_to_string(document)
        return jsonify({"message": "Active version set successfully", "product": document}), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

"""
Helper method to translate a report's MongoDB 'ObjectId' to a string (needed to convert report data to JSON)
    - Inputs: report (dict with '_id' as an ObjectId)
    - Outputs: report (dict with '_id' as a string)
"""
def _object_id_to_string(product):
        product['_id'] = str(product['_id'])
        return product