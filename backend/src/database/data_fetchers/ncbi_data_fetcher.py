import requests
import time
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

class NCBIDataFetcher:
    """
    Handles HTTP requests to the NCBI database and parsing of genomic data.
    """

    API_KEY = os.getenv('NCBI_API_KEY')  # Set your NCBI API key in the environment variables
    REQUEST_DELAY = 0.1  # Adjust the delay as needed (in seconds)

    @staticmethod
    def make_request_with_retries(url, params, max_retries=3):
        delay = NCBIDataFetcher.REQUEST_DELAY
        for attempt in range(max_retries):
            try:
                response = requests.get(url, params=params)
                if response.status_code == 429:
                    print("Rate limit exceeded. Retrying after delay...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                    continue
                response.raise_for_status()
                time.sleep(NCBIDataFetcher.REQUEST_DELAY)  # Rate limiting
                return response
            except requests.exceptions.HTTPError as e:
                print(f"HTTP error occurred: {e}")
                return None
            except Exception as e:
                print(f"An error occurred: {e}")
                return None
        print("Max retries exceeded.")
        return None

    @staticmethod
    def fetch_all_data(accession_id):
        """Fetch all required data using minimal API calls."""
        try:
            # Fetch the GenBank record, which contains sequence and rich metadata
            efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            efetch_params = {
                "db": "nuccore",
                "id": accession_id,
                "rettype": "gbwithparts",
                "retmode": "text",
                "api_key": NCBIDataFetcher.API_KEY
            }
            response = NCBIDataFetcher.make_request_with_retries(efetch_url, efetch_params)
            if not response:
                print("Failed to fetch data from NCBI.")
                return None
            genbank_data = response.text
            print(f"GenBank data fetched for accession ID {accession_id}.")
            return genbank_data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    @staticmethod
    def parse_genbank(genbank_data):
        """Parse GenBank data to extract required information."""
        try:
            data = {
                "taxonomicID": None,
                "accessionID": "",
                "genomic_sequence": "",                
                "common_name": "",
                "gcf": "",
#                "source": "",
                "collection_date": "",
                "fwdxdatabase_import_date": ""
            }

            lines = genbank_data.splitlines()
            sequence_lines = []
            in_origin = False
            in_source_feature = False
            for i, line in enumerate(lines):
                line = line.rstrip()
                if line.startswith("ACCESSION"):
                    parts = line.split()
                    if len(parts) > 1:
                        data["accessionID"] = parts[1]
                elif line.startswith("VERSION"):
                    parts = line.split()
                    if len(parts) > 1:
                        data["accessionID"] = parts[1]
                elif line.startswith("SOURCE"):
                    data["common_name"] = line[12:].strip()
                    
                    """    
                elif line.startswith("  ORGANISM"):
                    # Fetch taxonomic ID from the following lines
                    
                    for j in range(i+1, len(lines)):
                        if "db_xref=\"taxon:" in lines[j]:
                            idx = lines[j].find("taxon:")
                            taxid = lines[j][idx+6:].strip()
                            if taxid.endswith('"'):
                                taxid = taxid[:-1]
                            data["taxonomicID"] = int(taxid)
                            break
                        elif not lines[j].startswith(" "):
                            break
                    """    
#                elif line.strip() == "FEATURES             Location/Qualifiers":
#                    in_features = True

                elif line.strip().startswith("source"):
                    in_source_feature = True
                elif in_source_feature:
                    if line.strip().startswith("/"):
                        qualifier = line.strip()
                        if qualifier.startswith("/organism="):
                            data["organism"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/mol_type="):
                            data["mol_type"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/isolate="):
                            data["isolate"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/strain="):
                            data["strain"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/isolation_source="):
                            data["isolation_source"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/host="):
                            data["host"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/db_xref=") and "taxon:" in qualifier:
                            taxid = qualifier.split(":")[1].strip('"')
                            data["taxonomicID"] = int(taxid)
                        elif qualifier.startswith("/geo_loc_name="):
                            data["geo_loc_name"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/collection_date="):
                            data["collection_date"] = qualifier.split("=")[1].strip('"')
                        elif qualifier.startswith("/note="):
                            data["note"] = qualifier.split("=")[1].strip('"')
                    else:
                        in_source_feature = False
                elif line.startswith("ORIGIN"):
                    in_origin = True
                elif in_origin:
                    if line.startswith("//"):
                        in_origin = False
                        continue
                    # Remove line numbers and spaces
                    seq_line = ''.join(line.strip().split()[1:])
                    sequence_lines.append(seq_line)

            data["genomic_sequence"] = ''.join(sequence_lines)
            data["fwdxdatabase_import_date"] = datetime.now().strftime("%Y-%m-%d")
            

            # Fetch GCF number separately
            #data["gcf"] = NCBIDataFetcher.fetch_gcf_number(data["accessionID"]) or ""


            return data
        except Exception as e:
            print(f"Error parsing GenBank data: {e}")
            return None




    @staticmethod
    def fetch_gcf_number(accession_id):
        """Fetch the GCF number associated with an accession ID."""
        try:
            elink_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
            params = {
                "dbfrom": "nuccore",
                "db": "assembly",
                "id": accession_id,
                "retmode": "json",
                "api_key": NCBIDataFetcher.API_KEY
            }
            response = NCBIDataFetcher.make_request_with_retries(elink_url, params)
            if not response:
                return None
            data = response.json()
            linksets = data.get('linksets', [])
            if not linksets:
                return None
            linksetdbs = linksets[0].get('linksetdbs', [])
            if not linksetdbs:
                return None
            assembly_uids = linksetdbs[0].get('links', [])
            if not assembly_uids:
                return None
            assembly_uid = assembly_uids[0]

            # Fetch the assembly accession (GCF number)
            esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            esummary_params = {
                "db": "assembly",
                "id": assembly_uid,
                "retmode": "json",
                "api_key": NCBIDataFetcher.API_KEY
            }
            esummary_response = NCBIDataFetcher.make_request_with_retries(esummary_url, esummary_params)
            if not esummary_response:
                return None
            esummary_data = esummary_response.json()

            gcf_number = esummary_data['result'][assembly_uid]['assemblyaccession']
            return gcf_number
        except Exception as e:
            print(f"Error fetching GCF number: {e}")
            return None
