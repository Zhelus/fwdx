from backend.src.database.dataprocessor import DataProcessor

def main():
    """
    Entry point for prompting user input and triggering the data processing pipeline.
    """
    print("Welcome to the Genomic Data Processing Interface")

    # Prompt for the required accession ID
    accession_id = input("Enter the accession ID (required): ").strip()
    if not accession_id:
        print("Error: Accession ID is mandatory. Please provide a valid identifier.")
        return

    # Prompt for optional table name
    table = input("Enter the table name (optional, default is 'Pathogens'): ").strip() or "Pathogens"
    source = input("Enter the Source Database name (optional, default is 'NCBI'): ").strip() or "NCBI"
    # Instantiate and run the processor
  
    processor = DataProcessor(source)
    processor.process_and_upload(accession_id, table)
    processor.connector.close_connection()

if __name__ == "__main__":
    main()