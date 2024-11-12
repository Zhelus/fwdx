from bson import ObjectId

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()

'''
CRUD operations for Product (Reagent) objects.
'''

def create_product(product_data):
    """
    Creates a new product in the database.
    :param product_data: Dictionary containing product details.
    :return: Result of the MongoDB insert operation.
    """
    return connector.upload_document(product_data, CollectionType.REAGENTS)


def get_product(product_id):
    """
    Retrieves a product by its ID.
    :param product_id: ID of the product to retrieve.
    :return: Document of the product if found.
    """
    return connector.fetch_document({"_id": ObjectId(product_id)}, CollectionType.REAGENTS)


def update_product(product_id, product_data):
    """
    Updates an existing product in the database.
    :param product_id: ID of the product to update.
    :param product_data: Dictionary with updated product data.
    :return: Result of the MongoDB update operation.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update = {"$set": product_data}
    return connector.update_document(product_filter, update, CollectionType.REAGENTS)


def delete_product(product_id):
    """
    Deletes a product by its ID.
    :param product_id: ID of the product to delete.
    :return: Result of the MongoDB delete operation.
    """
    return connector.delete_document({"_id": ObjectId(product_id)}, CollectionType.REAGENTS)


def add_product_version(product_id, oligos):
    """
    Adds a new version to an existing product.
    :param product_id: ID of the product to update.
    :param oligos: List of oligos to add as a new version.
    :return: Result of the MongoDB update operation.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update = {"$push": {"versions": oligos}}
    return connector.update_document(product_filter, update, CollectionType.REAGENTS)


def set_active_version(product_id, version_index):
    """
    Sets the active version of a product.
    :param product_id: ID of the product to update.
    :param version_index: Index of the version to set as active.
    :return: Result of the MongoDB update operation.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update = {"$set": {"active_version_index": version_index}}
    return connector.update_document(product_filter, update, CollectionType.REAGENTS)
