from backend.src.pathogens.dataprocessor import DataProcessor

def main():
    """
    Entry point for prompting user input and triggering the data processing pipeline.
    """
    print("Welcome to the Genomic Data Processing Interface")

    # Prompt for the required GCF identifier
    gcf_number = input("Enter the GCF number (required): ").strip()
    if not gcf_number:
        print("Error: GCF number is mandatory. Please provide a valid identifier.")
        return

    # Prompt for optional parameters
    table = input("Enter the table name (optional, default is 'Pathogens'): ").strip() or "Pathogens"
    entry_id = input("Enter the entry ID (optional, default will use taxonomic ID): ").strip() or None
    element_to_parse = input("Enter the element to parse (optional, default is 'sequence'): ").strip() or "sequence"

    # Instantiate and run the processor
    processor = DataProcessor()
    processor.process_and_upload(gcf_number, table, entry_id, element_to_parse)

if __name__ == "__main__":
    main()