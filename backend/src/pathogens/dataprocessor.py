"""
this python code is used to process data fetched and parsed by ncbi_fetch.py 
Last uploaded: Kyle Stagner
Date: 2024/11/3
"""

from backend.src.database.db_connection import MongoDBConnector
from backend.src.pathogens.ncbi_fetch import NCBIDataFetcher

class DataProcessor:
    """
    Orchestrates the process of fetching data from NCBI, parsing it, and uploading it to MongoDB.
    """
    def __init__(self):
        self.connector = MongoDBConnector()

    def process_and_upload(self, identifier, table, entry_id, element_to_parse):
        """Fetch, parse, and upload data to MongoDB under a specified table and entry ID."""
        try:
            # Step 1: Fetch data
            file_path = NCBIDataFetcher.fetch_genomic_data(identifier)
            if not file_path:
                print("Fetch step failed.")
                return

            # Step 2: Parse data
            parsed_data = NCBIDataFetcher.parse_fasta(file_path)
            if not parsed_data or element_to_parse not in parsed_data:
                print(f"Parse step failed: '{element_to_parse}' not found.")
                return

            parsed_string = parsed_data[element_to_parse]

            # If entry_id is not provided, fetch the taxonomic ID
            if not entry_id:
                entry_id = NCBIDataFetcher.fetch_taxonomic_id(identifier)
                if not entry_id:
                    print("Failed to fetch taxonomic ID.")
                    return
                else:
                    print(f"Using taxonomic ID '{entry_id}' as entry ID.")

            # Step 3: Upload data to MongoDB
            collection = self.connector.db[table]
            result = collection.update_one(
                {"_id": entry_id},
                {"$set": {element_to_parse: parsed_string}},
                upsert=True
            )

            if result.modified_count > 0:
                print(f"Document with ID '{entry_id}' in '{table}' updated successfully.")
            elif result.upserted_id:
                print(f"Document with ID '{entry_id}' inserted into '{table}' successfully.")
            else:
                print(f"No changes made to the document with ID '{entry_id}' in '{table}'.")

        finally:
            # Close connection
            self.connector.close_connection()