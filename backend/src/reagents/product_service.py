from bson import ObjectId
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType
from bson.errors import InvalidId


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
    oligos = product_data.get("oligos", [])
    if oligos:
        # Initialize versions with the provided oligos
        product_data["versions"] = [oligos]
        product_data["active_version_index"] = 0
        # Remove 'oligos' from product_data to prevent duplication
        product_data.pop("oligos", None)
    else:
        # Ensure versions is initialized as an empty list if not provided
        product_data.setdefault("versions", [])
        product_data.setdefault("active_version_index", 0)

    # Insert the document into the database
    result = connector.upload_document(product_data, CollectionType.REAGENTS)

    # Fetch and return the inserted document
    return connector.fetch_document({"_id": result.inserted_id}, CollectionType.REAGENTS)



def get_product_with_oligo_details(product_id):
    """
    Retrieves a product by its ID and replaces oligo IDs in its versions with detailed oligo information.
    :param product_id: ID of the product to retrieve.
    :return: The product document with oligo details if found.
    """
    # Fetch the product by ID
    product = connector.fetch_document({"_id": ObjectId(product_id)}, CollectionType.REAGENTS)
    if not product:
        return None

    # Collect all oligo IDs from the product versions
    oligo_ids = set()
    for version in product.get("versions", []):
        oligo_ids.update(version)

    # Fetch oligo documents based on collected IDs
    oligos = connector.fetch_all_documents_by_filter(
        {"_id": {"$in": [ObjectId(oligo_id) for oligo_id in oligo_ids if ObjectId.is_valid(oligo_id)]}},
        CollectionType.OLIGOS
    )

    # Create a mapping of oligo ID to oligo details
    oligo_map = {
        str(oligo["_id"]): {
            "_id": str(oligo["_id"]),
            "name": oligo.get("name"),
            "sequence": oligo.get("sequence"),
            "archived": oligo.get("archived", False),
            "dna_strand_positive": oligo.get("dna_strand_positive", False),
        }
        for oligo in oligos
    }

    # Replace oligo IDs in product versions with full oligo details
    for i, version in enumerate(product.get("versions", [])):
        product["versions"][i] = [oligo_map.get(oligo_id, {"_id": oligo_id}) for oligo_id in version]

    return product


def get_all_products():
    """
       Retrieves all products.
       :return: All products
       """
    return list(connector.fetch_all_documents(CollectionType.REAGENTS))

def get_products_with_oligo_details():
    """
    Retrieves all products and replaces oligo IDs in their versions with detailed oligo information.
    :return: List of products with parsed oligo details.
    """
    # Fetch all products from the REAGENTS collection
    products = list(connector.fetch_all_documents(CollectionType.REAGENTS))
    oligo_ids = set()

    # Collect all oligo IDs from product versions
    for product in products:
        for version in product.get("versions", []):
            oligo_ids.update(version)

    # Fetch oligo documents based on collected IDs
    oligos = connector.fetch_all_documents_by_filter(
        {"_id": {"$in": [ObjectId(oligo_id) for oligo_id in oligo_ids if ObjectId.is_valid(oligo_id)]}},
        CollectionType.OLIGOS
    )

    # Create a mapping of oligo ID to oligo details
    oligo_map = {
        str(oligo["_id"]): {
            "name": oligo.get("name"),
            "sequence": oligo.get("sequence"),
            "archived": oligo.get("archived", False),
            "dna_strand_positive": oligo.get("dna_strand_positive", False),
        }
        for oligo in oligos
    }

    # Replace oligo IDs in product versions with full oligo details
    for product in products:
        for i, version in enumerate(product.get("versions", [])):
            product["versions"][i] = [oligo_map.get(oligo_id, {"_id": oligo_id}) for oligo_id in version]

    return products


def update_product(product_id, product_data):
    """
    Updates an existing product in the database.
    """
    product_filter = {"_id": ObjectId(product_id)}
    update_operations = {}
    update_set = {}
    update_push = {}

    # Fetch the existing product
    existing_product = connector.fetch_document(product_filter, CollectionType.REAGENTS)
    if not existing_product:
        return None

    # Update the name if provided
    if "name" in product_data:
        update_set["name"] = product_data["name"]

    # Append a new version if oligos are provided
    if "oligos" in product_data:
        new_version = product_data["oligos"]

        # Validate oligo IDs without converting them to ObjectId instances
        for oligo_id in new_version:
            if not ObjectId.is_valid(oligo_id):
                raise ValueError(f"Invalid Oligo ID provided: {oligo_id}")

        # Store the oligo IDs as strings to maintain consistency
        update_push["versions"] = [str(oligo_id) for oligo_id in new_version]

        # Update the active_version_index
        new_active_version_index = len(existing_product["versions"])
        update_set["active_version_index"] = new_active_version_index

    # Build the update operations
    if update_set:
        update_operations["$set"] = update_set
    if update_push:
        update_operations["$push"] = update_push

    if not update_operations:
        # Nothing to update
        return existing_product

    # Perform the update
    result = connector.update_document(product_filter, update_operations, CollectionType.REAGENTS)

    # Fetch and return the updated document with oligo details
    updated_product = get_product_with_oligo_details(product_id)
    return updated_product




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
