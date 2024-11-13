from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType


class Product:
    """
    Represents a reagent product with multiple versions, each containing oligos.
    Each version contains a list of oligos, and there is an active version index.
    Only the product_id is strictly enforced for now.
    """

    def __init__(self, product_id: str, name: str = None, versions: list = None, active_version_index: int = 0):
        self.product_id = product_id
        self.name = name
        self.active_version_index = active_version_index
        # Each version is a list of oligos with fields: oligo_name, oligo_id, oligo_sequence, dna_strand_positive
        self.versions = versions if versions is not None else []

    def add_version(self, oligos: list):
        """
        Adds a new version to the product with the provided oligos.
        :param oligos: A list of dictionaries, each representing an oligo with fields: oligo_name, oligo_id, oligo_sequence, dna_strand_positive.
        """
        self.versions.append(oligos)

    def to_document(self):
        document = {
            'product_id': self.product_id,
            'name': self.name,
            'active_version_index': self.active_version_index,
            'versions': self.versions
        }
        return document
