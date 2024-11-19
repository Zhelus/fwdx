from Bio.Blast import NCBIWWW
from Bio import SeqIO

# Read the query sequence from your FASTA file
with open("test_data.fasta", "r") as fasta_file:
    record = next(SeqIO.parse(fasta_file, "fasta"))

# Perform the BLAST search
print("Performing BLAST search...")
result_handle = NCBIWWW.qblast("blastn", "nt", record.seq, megablast=True)

# Save the results to a file
with open("blast_results.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

print("BLAST search complete. Results saved to 'blast_results.xml'")
