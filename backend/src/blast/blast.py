import os
import subprocess
import time


class Blast:

    def __init__(self, fasta_file: str, blast_database: str, db_type: str = "nucl"):
        self.fasta_file = fasta_file
        self.blast_database = "blast_database/" + blast_database
        self.db_type = db_type

        if os.path.exists(self.fasta_file):
           self.create_blast_db()
        else:
            print(f"Fasta file {self.fasta_file} does not exist")

    """
    The function of this method is to create a BLAST database to run out blast queries off of 
    """
    def create_blast_db(self):

        cmd = [
            'makeblastdb',
            '-in', self.fasta_file,
            '-dbtype', self.db_type,
            '-out', self.blast_database,
        ]

        print("Creating blast database...")
        start_time = time.perf_counter()
        subprocess.run(cmd, check=True)
        end_time = time.perf_counter()
        print(f"Blast database created in {end_time - start_time} seconds.")

    """
    The function of this method is to run BLAST cmd line queries to your BLAST database and output and XML file  
    
    :param oligos_file: This is your file of Forward/Reverse Primers and Probes
    :param output_file: This is the path to your output file where you want your XML to be stored 
    """
    def run_blast(self, oligos_file, output_file):

        cmd = [
            'blastn',
            '-query', oligos_file,
            '-db', self.blast_database,
            '-out', output_file,
            '-outfmt', '5',
            '-evalue', '0.001',
            '-word_size', '7'
        ]

        print("Running blast...")
        start_time = time.perf_counter()
        subprocess.run(cmd, check=True)
        end_time = time.perf_counter()
        print(f"Blast complete in {end_time - start_time} seconds.")

blast = Blast("fasta_files/all_genomes.fasta", "blast_db")
blast.create_blast_db()
blast.run_blast("fasta_files/omnicron_primer_probes.fasta", "XML_Outputs/omni_blast_results.xml")

