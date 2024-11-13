from bson import ObjectId
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()

def create_oligo(product_id, oligo_data):
    """
    Creates a new oligo and adds it to a new version of the specified product.
    :param product_id: ID of the product to which the oligo is added.
    :param oligo_data: Dictionary with oligo details.
    :return: Result of the MongoDB update operation.
    """
    # Filter to find the product by its ID
    product_filter = {"_id": ObjectId(product_id)}

    # Retrieve the current product document
    product = connector.fetch_document(product_filter, CollectionType.REAGENTS)
    if not product:
        return {"error": "Product not found"}, 404

    # Copy the current active version and add the new oligo
    current_version = product["versions"][product["active_version_index"]]
    new_version = current_version + [oligo_data]  # Append the new oligo to the copied version

    # Prepare the update payload
    update_operations = {
        "$push": {"versions": new_version},
        "$set": {"active_version_index": len(product["versions"])}
    }

    # Perform the update operation
    result = connector.update_document(product_filter, update_operations, CollectionType.REAGENTS)

    return result

def update_oligo(product_id, oligo_id, oligo_data):
    """
    Updates an existing oligo by creating a new version with the modified oligo data.
    :param product_id: ID of the product containing the oligo.
    :param oligo_id: ID of the oligo to update.
    :param oligo_data: Dictionary with updated oligo details.
    :return: Result of the MongoDB update operation.
    """
    # Filter to find the product by its ID
    product_filter = {"_id": ObjectId(product_id)}

    # Retrieve the current product document
    product = connector.fetch_document(product_filter, CollectionType.REAGENTS)
    if not product:
        return {"error": "Product not found"}, 404

    # Copy the current active version
    current_version = product["versions"][product["active_version_index"]]
    new_version = []

    # Update the oligo if it matches oligo_id, otherwise keep it unchanged
    for oligo in current_version:
        if oligo.get("oligo_id") == oligo_id:
            # Update the oligo with provided data
            updated_oligo = {**oligo, **oligo_data}
            new_version.append(updated_oligo)
        else:
            new_version.append(oligo)

    # Prepare the update payload to append the new version and update active_version_index
    update_operations = {
        "$push": {"versions": new_version},
        "$set": {"active_version_index": len(product["versions"])}
    }

    # Perform the update operation
    result = connector.update_document(product_filter, update_operations, CollectionType.REAGENTS)

    return result
