"""
This code builds the NCBI search quiery, processes the request, and prepares the strings for dataprocessor.py
Last uploaded: Kyle Stagner
Date: 2024/11/3
"""

import os
import requests

class NCBIDataFetcher:
    """
    Handles HTTP requests to the NCBI database and parsing of genomic data.
    """

    @staticmethod
    def fetch_genomic_data(identifier):
        """Fetch data from NCBI using an identifier (e.g., GCF number) and save it as a file."""
        try:
            # First, get the assembly UID using the GCF number
            base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            params = {
                "db": "assembly",
                "term": identifier,
                "retmode": "json"
            }

            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            uid_list = data.get('esearchresult', {}).get('idlist', [])
            if not uid_list:
                print(f"No assembly found for identifier '{identifier}'.")
                return None
            assembly_uid = uid_list[0]

            # Get linked nucleotide records
            link_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi"
            link_params = {
                "dbfrom": "assembly",
                "db": "nuccore",
                "id": assembly_uid,
                "retmode": "json"
            }
            link_response = requests.get(link_url, params=link_params)
            link_response.raise_for_status()
            link_data = link_response.json()
            linksets = link_data.get('linksets', [])
            if not linksets or 'linksetdbs' not in linksets[0]:
                print(f"No nucleotide records linked to assembly '{identifier}'.")
                return None
            nuccore_ids = linksets[0]['linksetdbs'][0].get('links', [])
            if not nuccore_ids:
                print(f"No nucleotide records linked to assembly '{identifier}'.")
                return None

            # Fetch the sequence data
            efetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
            efetch_params = {
                "db": "nuccore",
                "id": ','.join(nuccore_ids),
                "rettype": "fasta",
                "retmode": "text"
            }
            efetch_response = requests.get(efetch_url, params=efetch_params)
            efetch_response.raise_for_status()

            # Save fetched data to a designated directory
            os.makedirs('data', exist_ok=True)
            file_path = os.path.join('data', f"{identifier}_data.fasta")
            with open(file_path, 'w') as file:
                file.write(efetch_response.text)
            print(f"Data fetched and saved to {file_path}")
            return file_path

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred while fetching data: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred while fetching data: {e}")
            return None
        except ValueError as e:
            print(f"JSON decoding failed: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    @staticmethod
    def parse_fasta(file_path):
        """Parse a FASTA formatted file and return a dictionary with parsed data."""
        try:
            with open(file_path, 'r') as file:
                fasta_data = file.read()
            lines = fasta_data.splitlines()
            if not lines:
                print(f"The FASTA file '{file_path}' is empty.")
                return None
            header = lines[0]
            sequence = ''.join(lines[1:])
            print(f"Parsed sequence header: {header}")
            return {"header": header, "sequence": sequence}
        except FileNotFoundError:
            print(f"File not found: '{file_path}'.")
            return None
        except Exception as e:
            print(f"An error occurred while parsing the FASTA file: {e}")
            return None

    @staticmethod
    def fetch_taxonomic_id(identifier):
        """Fetch taxonomic ID from NCBI using an assembly identifier (e.g., GCF number)."""
        try:
            # First, get the assembly UID using the GCF number
            esearch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
            esearch_params = {
                "db": "assembly",
                "term": identifier,
                "retmode": "json"
            }
            esearch_response = requests.get(esearch_url, params=esearch_params)
            esearch_response.raise_for_status()
            esearch_data = esearch_response.json()
            uid_list = esearch_data.get('esearchresult', {}).get('idlist', [])
            if not uid_list:
                print(f"No assembly found for identifier '{identifier}'.")
                return None
            assembly_uid = uid_list[0]

            # Fetch summary to get the taxonomic ID
            esummary_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
            esummary_params = {
                "db": "assembly",
                "id": assembly_uid,
                "retmode": "json"
            }
            esummary_response = requests.get(esummary_url, params=esummary_params)
            esummary_response.raise_for_status()
            esummary_data = esummary_response.json()
            result = esummary_data.get('result', {})
            assembly_info = result.get(assembly_uid, {})
            taxid = assembly_info.get('taxid')
            if not taxid:
                print(f"Taxonomic ID not found for assembly '{identifier}'.")
                return None
            print(f"Taxonomic ID fetched: {taxid}")
            return str(taxid)

        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred while fetching taxonomic ID: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Request error occurred while fetching taxonomic ID: {e}")
            return None
        except ValueError as e:
            print(f"JSON decoding failed: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None