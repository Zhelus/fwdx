from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType


class Oligo:
    """
    Represents an oligo within a reagent product.
    Each oligo is uniquely identified by oligo_id and contains details about its sequence.
    """

    def __init__(self, oligo_id: str, oligo_name: str, oligo_sequence: str, dna_strand_positive: bool):
        self.oligo_id = oligo_id
        self.oligo_name = oligo_name
        self.oligo_sequence = oligo_sequence
        self.dna_strand_positive = dna_strand_positive

    def to_document(self):
        document = {
            'oligo_id': self.oligo_id,
            'oligo_name': self.oligo_name,
            'oligo_sequence': self.oligo_sequence,
            'dna_strand_positive': self.dna_strand_positive
        }
        return document
