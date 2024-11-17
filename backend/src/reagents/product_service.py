from bson import ObjectId
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector(force_ssl=True)

'''
CRUD operations for Product (Reagent) objects.
'''

def create_product(product_data):
    """
    Creates a new product in the database.
    :param product_data: Dictionary containing product details.
    :return: The created product document.
    """
    # Ensure versions is initialized as an empty list if not provided
    product_data.setdefault("versions", [])
    product_data.setdefault("active_version_index", 0)

    # Insert the document into the database
    result = connector.upload_document(product_data, CollectionType.REAGENTS)

    # Fetch and return the inserted document
    return connector.fetch_document({"_id": result.inserted_id}, CollectionType.REAGENTS)


def get_product(product_id):
    """
    Retrieves a product by its ID.
    :param product_id: ID of the product to retrieve.
    :return: The product document if found.
    """
    return connector.fetch_document({"_id": ObjectId(product_id)}, CollectionType.REAGENTS)

def get_all_products():
    """
       Retrieves all products.
       :return: All products
       """
    return list(connector.fetch_all_documents(CollectionType.REAGENTS))

def update_product(product_id, product_data):
    """
    Updates an existing product in the database.
    :param product_id: ID of the product to update.
    :param product_data: Dictionary with updated product data, including name or versions.
    :return: The updated product document.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update_operations = {}

    # Update the name if provided
    if "name" in product_data:
        update_operations["$set"] = {"name": product_data["name"]}

    # Append a new version if provided
    if "oligos" in product_data:
        new_version = product_data["oligos"]
        if "$set" not in update_operations:
            update_operations["$set"] = {}
        update_operations["$push"] = {"versions": new_version}

    # Perform the update operation
    result = connector.update_document(product_filter, update_operations, CollectionType.REAGENTS)

    # Fetch and return the updated document
    return connector.fetch_document(product_filter, CollectionType.REAGENTS)


def delete_product(product_id):
    """
    Deletes a product by its ID.
    :param product_id: ID of the product to delete.
    :return: True if the deletion was successful, False otherwise.
    """
    result = connector.delete_document({"_id": ObjectId(product_id)}, CollectionType.REAGENTS)
    return result.deleted_count > 0


def add_product_version(product_id, oligos):
    """
    Adds a set of oligo IDs to a new version of a product and updates the active version index.
    :param product_id: The ID of the product to update.
    :param oligos: A list of oligo IDs to add as a new version.
    :return: The updated product document.
    """
    product_filter = {"_id": ObjectId(product_id)}

    # Fetch the existing product
    existing_product = connector.fetch_document(product_filter, CollectionType.REAGENTS)
    if not existing_product:
        return None

    # Add the new version to the versions array
    update_operations = {
        "$push": {"versions": oligos},
        "$set": {"active_version_index": len(existing_product["versions"])}
    }

    # Perform the update
    connector.update_document(product_filter, update_operations, CollectionType.REAGENTS)

    # Fetch and return the updated product
    return connector.fetch_document(product_filter, CollectionType.REAGENTS)



def set_active_version(product_id, version_index):
    """
    Sets the active version of a product.
    :param product_id: ID of the product to update.
    :param version_index: Index of the version to set as active.
    :return: The updated product document.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update = {"$set": {"active_version_index": version_index}}

    # Perform the update operation
    connector.update_document(product_filter, update, CollectionType.REAGENTS)

    # Fetch and return the updated document
    return connector.fetch_document(product_filter, CollectionType.REAGENTS)
