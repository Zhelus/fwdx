# oligo_service.py

from bson import ObjectId
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType
from .oligo import Oligo

connector = MongoDBConnector(force_ssl=True)

def create_oligo(oligo_data):
    return connector.upload_document(oligo_data, CollectionType.OLIGOS)


def archive_oligo(oligo_id):
    """
    Archives (soft deletes) an oligo by setting its 'archived' field to True.
    :param oligo_id: The ID of the oligo to archive.
    :return: A dictionary indicating the success of the operation and the number of documents modified.
    """
    try:
        oligo_filter = {"_id": ObjectId(oligo_id)}
        update = {"$set": {"archived": True}}
        result = connector.update_document(oligo_filter, update, CollectionType.OLIGOS)

        # Process the UpdateResult
        if result.matched_count == 0:
            return {"success": False, "message": f"Oligo with ID {oligo_id} not found"}
        elif result.modified_count == 0:
            return {"success": False, "message": f"Oligo with ID {oligo_id} was already archived"}
        else:
            return {"success": True, "message": f"Oligo with ID {oligo_id} archived successfully"}
    except Exception as e:
        raise RuntimeError(f"An error occurred while archiving the oligo: {str(e)}")


def get_all_active_oligos():
    """
    Fetches all oligos that are not archived.
    :return: List of active (non-archived) oligos.
    """
    query = {"archived": False}
    # Use fetch_all_documents to retrieve all non-archived oligos
    return list(connector.fetch_all_documents(CollectionType.OLIGOS, query))

def get_all_oligos():
    return list(connector.fetch_all_documents(CollectionType.OLIGOS))

def get_oligo_by_id(oligo_id):
    """
    Fetches a single oligo by its ID.
    :param oligo_id: The ID of the oligo to fetch.
    :return: The oligo document if found.
    """
    return connector.fetch_document({"_id": ObjectId(oligo_id)}, CollectionType.OLIGOS)

