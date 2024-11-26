import os
import subprocess
import time

"""
This is the main blast class that is responsible for creating the blast database and doing blast analysis. Subject to be split into multiple files 

Last uploaded: Carson Freeman 
Date: 2024/11/19
"""

class Blast:

    def __init__(self, fasta_file: str, blast_database: str, db_type: str = "nucl"):
        self.fasta_file = fasta_file
        self.blast_database = "blast_database/" + blast_database
        self.db_type = db_type

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
            '-evalue', "0.001", # can mess with this value to get more stingy on what is considered a match
            '-word_size', '7'
        ]

        print("Running blast...")
        start_time = time.perf_counter()
        subprocess.run(cmd, check=True)
        end_time = time.perf_counter()
        print(f"Blast complete in {end_time - start_time} seconds.")

blast = Blast("fasta_files/all_genomes.fasta", "blast_db")
# blast.create_blast_db()
blast.run_blast("fasta_files/jc_virus_primer_probes.fasta", "XML_Outputs/jc.xml")

