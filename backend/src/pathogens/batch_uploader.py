from backend.src.database.dataprocessor import DataProcessor

def read_accession_ids(file_path):
    """
    Reads accession IDs from a file, one per line, and returns a list.
    """
    accession_ids = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                accession_id = line.strip()
                if accession_id:
                    accession_ids.append(accession_id)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return accession_ids

def main():
    """
    Main function to process a list of accession IDs.
    """
    print("Batch Accession ID Processor")
    file_path = input("Enter the path to the file containing accession IDs: ").strip()
    source = input("Enter the Source Database name (optional, default is 'NCBI'): ").strip() or "NCBI"
    table = input("Enter the table name (optional, default is 'Pathogens'): ").strip() or "Pathogens"

    accession_ids = read_accession_ids(file_path)
    if not accession_ids:
        print("No accession IDs to process.")
        return
    

    processor = DataProcessor(source)
    for accession_id in accession_ids:
        print(f"\nProcessing accession ID: {accession_id}")
        try:
            processor.process_and_upload(accession_id, table)
        except Exception as e:
            print(f"An error occurred while processing {accession_id}: {e}")


    print("\nBatch processing completed.")
    processor.connector.close_connection()

if __name__ == "__main__":
    main()