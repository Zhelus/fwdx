# oligo.py
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

class Oligo:
    """
    Represents an individual oligo with its relevant details.
    """
    def __init__(self, oligo_id: str, dna_strand_positive: bool, sequence: str, name: str, archived: bool = False):
        self.oligo_id = oligo_id
        self.dna_strand_positive = dna_strand_positive
        self.sequence = sequence
        self.name = name
        self.archived = archived

    def to_document(self):
        """
        Converts the Oligo instance to a document for MongoDB.
        """
        return {
            "oligo_id": self.oligo_id,
            "dna_strand_positive": self.dna_strand_positive,
            "sequence": self.sequence,
            "name": self.name,
            "archived": self.archived
        }
