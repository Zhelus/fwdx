from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

"""
This is a helper class to convert documents -> fasta files 

Last uploaded: Carson Freeman 
Date: 2024/11/19
"""

class DocumentToFastaConverter:

    def __init__(self):
       self.connector = MongoDBConnector()

    """
    The purpose of this helper function is to convert all pathogens to a single fasta file that we can pass to blast to make a blast database 
    
    :param output_file_name: This is the name of the output fasta file 
    """
    def all_pathogen_to_fasta(self, output_file_name: str):
        collection = self.connector.fetch_all_documents(CollectionType.PATHOGENS)

        # Upload the documents to the file
        with open("fasta_files/" + output_file_name + ".fasta", "w") as fasta_file:
            for document in collection:
                common_name = document.get("common_name")
                genomic_sequence = document.get("genomic_sequence").upper()

                if common_name and genomic_sequence:
                    fasta_file.write(f">{common_name}\n")
                    fasta_file.write(f"{genomic_sequence}\n")

    """
    Not sure this is how we want this function to work, or if we would want to pass a list of Oligos we want to convert into a fasta 
    1. User picks the oligos it wants 
    2. We fetch all of those Oligos from some unique identifier 
    3. Convert into a fasta file 
    4. Pass the fasta file to blast 
    """
    def all_oligo_to_fasta(self, output_file_name: str):
        collection = self.connector.fetch_all_documents(CollectionType.OLIGOS)

        # Upload the documents to the file
        with open("fasta_files/" + output_file_name + ".fasta", "w") as fasta_file:
            for document in collection:
                common_name = document.get("name")
                oligo = document.get("sequence")

                if common_name and oligo:
                    fasta_file.write(f">{common_name}\n")
                    fasta_file.write(f"{oligo}\n")
