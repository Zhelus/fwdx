"""
This class represents a Pathogen object which should have fields corresponding to the
fields we want to save into MongoDB.
"""
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType


class Pathogen:
    """
    By default, I did not make any of these fields "required" in the constructor besides taxonomy_id. We will have to
    determine what makes the most sense to strictly enforce later.
    """

    def __init__(self, taxonomy_id: str, scientific_name: str = None, source_db: str = None,
                 genomic_sequence: str = None):
        self.taxonomy_id = taxonomy_id
        self.scientific_name = scientific_name
        self.source_db = source_db
        self.genomic_sequence = genomic_sequence

    def to_document(self):
        document = {'taxonomy_id': self.taxonomy_id, 'scientific_name': self.scientific_name,
                    'source_db': self.source_db, 'genomic_sequence': self.genomic_sequence}

        return document
