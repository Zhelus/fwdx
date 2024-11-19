from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.helper.collection_type import CollectionType

connector = MongoDBConnector()
collection = connector.fetch_all_documents(CollectionType.PATHOGENS)

with open("fasta_files/all_genomes.fasta", "w") as fasta_file:
    print("Reading documents...")
    for document in collection:
        common_name = document.get("common_name")
        genomic_sequence = document.get("genomic_sequence").upper()

        if common_name and genomic_sequence:
            fasta_file.write(f">{common_name}\n")
            fasta_file.write(f"{genomic_sequence}\n")

