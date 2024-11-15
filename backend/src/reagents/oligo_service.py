# oligo_service.py

from bson import ObjectId
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType
from .oligo import Oligo

connector = MongoDBConnector()

def create_oligo(oligo_data):
    # Existing code for creating an oligo
    oligo = Oligo(**oligo_data)
    document = oligo.to_document()
    return connector.upload_document(document, CollectionType.OLIGOS)

def archive_oligo(oligo_id):
    # Existing code for archiving an oligo
    oligo_filter = {"oligo_id": oligo_id}
    update = {"$set": {"archived": True}}
    return connector.update_document(oligo_filter, update, CollectionType.OLIGOS)

def get_all_active_oligos():
    """
    Fetches all oligos that are not archived.
    :return: List of active (non-archived) oligos.
    """
    query = {"archived": False}
    # Use fetch_all_documents to retrieve all non-archived oligos
    return list(connector.fetch_all_documents(CollectionType.OLIGOS, query))



def get_oligo_by_id(oligo_id):
    """
    Fetches a single oligo by its ID.
    :param oligo_id: The ID of the oligo to fetch.
    :return: The oligo document if found.
    """
    query = {"oligo_id": oligo_id}
    return connector.fetch_document(query, CollectionType.OLIGOS)
