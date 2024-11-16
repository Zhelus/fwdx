class Oligo:
    """
    Represents an individual oligo with its relevant details.
    """
    def __init__(self, dna_strand_positive: bool, sequence: str, name: str, archived: bool = False):
        self.dna_strand_positive = dna_strand_positive
        self.sequence = sequence
        self.name = name
        self.archived = archived

    def to_document(self):
        """
        Converts the Oligo instance to a document for MongoDB.
        """
        return {
            "dna_strand_positive": self.dna_strand_positive,
            "sequence": self.sequence,
            "name": self.name,
            "archived": self.archived
        }
