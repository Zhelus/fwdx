from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from backend.src.database.data_fetchers.ncbi_data_fetcher import NCBIDataFetcher
#
# 
#from backend.src.database.data_fetchers.gisaid_data_fetcher import GISAIDDataFetcher
#from backend.src.database.data_fetchers.bv_brc_data_fetcher import BV_BRCDataFetcher

class DataProcessor:
    """
    Orchestrates the process of fetching data from various databases and uploading it to MongoDB.
    """
    def __init__(self, source):
        self.source = source  # 'NCBI', 'GISAID', or 'BV-BRC'
        self.connector = MongoDBConnector()
        if self.connector.database is None:
            print("Failed to connect to MongoDB. Exiting the process.")
            exit(1)
    
    def process_and_upload(self, accession_id, table):
        """Fetch data using accession ID from the specified source and upload structured data to MongoDB."""
        try:
            # Fetch and parse data based on the source database
            data = self.fetch_data(accession_id)
            if not data:
                print(f"Failed to fetch data from {self.source} for accession ID '{accession_id}'.")
                return

            # Check for duplicates
            duplicate_status = self.check_for_duplicates(accession_id, data, table)

            if duplicate_status == 'exact_match':
                print(f"Duplicate entry found for accession ID '{accession_id}'.")
            elif duplicate_status == 'discrepancy':
                print(f"Discrepancy found for accession ID '{accession_id}'. Needs resolution.")
            elif duplicate_status == 'no_duplicate':
                # Insert data into MongoDB
                collection = self.connector.database[table]
                result = collection.insert_one(data)
                print(f"Data inserted with ID: {result.inserted_id}")
            else:
                print(f"An error occurred while checking duplicates for accession ID '{accession_id}'.")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def fetch_data(self, accession_id):
        """Fetch and parse data from the specified source."""
        if self.source == 'NCBI':
            return self.fetch_data_from_ncbi(accession_id)
        elif self.source == 'GISAID':
            return self.fetch_data_from_gisaid(accession_id)
        elif self.source == 'BV-BRC':
            return self.fetch_data_from_bv_brc(accession_id)
        else:
            print(f"Unknown source: {self.source}")
            return None

    def fetch_data_from_ncbi(self, accession_id):
        """Fetch and parse data from NCBI."""
        genbank_data = NCBIDataFetcher.fetch_all_data(accession_id)
        if not genbank_data:
            return None
        data = NCBIDataFetcher.parse_genbank(genbank_data)
        return data

    """
    def fetch_data_from_gisaid(self, accession_id):        
        # Placeholder implementation; replace with actual code
        gisaid_data = GISAIDDataFetcher.fetch_all_data(accession_id)
        if not gisaid_data:
            return None
        data = GISAIDDataFetcher.parse_data(gisaid_data)
        return data

    def fetch_data_from_bv_brc(self, accession_id):
        # Placeholder implementation; replace with actual code
        bv_brc_data = BV_BRCDataFetcher.fetch_all_data(accession_id)
        if not bv_brc_data:
            return None
        data = BV_BRCDataFetcher.parse_data(bv_brc_data)
        return data
    """

    def check_for_duplicates(self, accession_id, new_data, table):
        """Check for duplicates in the database and handle accordingly."""
        collection = self.connector.database[table]
        existing_entry = collection.find_one({'accessionID': accession_id})
        if existing_entry:
            if existing_entry['genomic_sequence'] == new_data['genomic_sequence']:
                # Sequences are exactly the same
                return 'exact_match'
            else:
                # Sequences differ
                return 'discrepancy'
        else:
            # No duplicate found
            return 'no_duplicate'