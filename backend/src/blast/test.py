
import time
from backend.src.database.mongodb.mongodb_connector import MongoDBConnector
from Bio import SeqIO
import xml.etree.ElementTree as ET
from xml.dom import minidom

from backend.src.helper.collection_type import CollectionType

"""
The purpose of this function is to take in the fasta file we give it and it returns the genome sequence into a list
this might not be necessary for passing a singular genome to the function but 
"""
def read_genome(fasta_file):
    genome_sequences = []
    for record in SeqIO.parse(fasta_file, "fasta"):
        genome_sequences.append(str(record.seq))  # Collect all sequences
    return genome_sequences

"""
The purpose of this function is to take in the list of primers/probes, and the current sequence we are checking 
then if we find a mismatch between the two we mark this down in the mismatch_lines with a "X" otherwise it is a 
match and we mark it with a "|" this is for our XML output and later for our report 
"""
def highlight_mismatches(primer, genome):
    """Highlight mismatches between primer and genome."""
    highlighted_genome = []
    mismatch_positions = []
    mismatch_lines = []

    # Compare sequences
    for i in range(len(primer)):
        if i < len(genome):
            if primer[i] != genome[i]:
                mismatch_positions.append(i)
                highlighted_genome.append(genome[i])  # Highlight mismatch
                mismatch_lines.append("X")
            else:
                highlighted_genome.append(genome[i])
                mismatch_lines.append("|")
        else:
            highlighted_genome.append(genome[i])  # If genome is longer than primer

    highlighted_genome_str = ''.join(highlighted_genome)
    mismatch_indices_str = ', '.join(map(str, mismatch_positions))
    mismatch_lines_str = ''.join(mismatch_lines)

    return highlighted_genome_str, mismatch_indices_str, mismatch_lines_str

"""
The purpose of this function is to find the best match for that primer/probe we do this by comparing it the number of 
mismatches for that sequence and keep track of a best_match variable. 

Note: This also is taking into account that we are passing in multiple genomic sequences in our fasta file 
"""
def find_best_match(primer, genome):
    """Find the best match for a primer in the genomic sequence."""
    best_match = None
    least_mismatches = float('inf')

    for start in range(len(genome) - len(primer) + 1):  # Ensure we don't go out of bounds
        subsequence = genome[start:start + len(primer)]
        highlighted_sequence, mismatches, mismatch_lines = highlight_mismatches(primer, subsequence)
        num_mismatches = len(mismatches.split(', ')) if mismatches else 0

        if num_mismatches < least_mismatches:
            least_mismatches = num_mismatches
            best_match = {
                "mismatch_lines": mismatch_lines,
                "highlighted_sequence": highlighted_sequence,
                "mismatches": mismatches,
                "num_mismatches": num_mismatches,
                "genomic_subsequence": subsequence,
                "genomic_position": start
            }

    return best_match

"""
The purpose of this function simply is to create a pretty XML output that we can easily translate to a pretty frontend
"""
def generate_xml_output(results, output_file):
    """Generate a pretty-printed XML file from the results."""
    root = ET.Element("PrimerMatches")

    for result in results:
        match_element = ET.SubElement(root, "Match")

        primer_element = ET.SubElement(match_element, "Primer")
        primer_element.text = result["primer"]

        mismatch_line_element = ET.SubElement(match_element, "MismatchLines")
        mismatch_line_element.text = result["mismatch_lines"]

        highlighted_sequence_element = ET.SubElement(match_element, "HighlightedSequence")
        highlighted_sequence_element.text = result["highlighted_sequence"]

        mismatches_element = ET.SubElement(match_element, "Mismatches")
        mismatches_element.text = result["mismatches"]

        num_mismatches_element = ET.SubElement(match_element, "NumMismatches")
        num_mismatches_element.text = str(result["num_mismatches"])

        genomic_position_element = ET.SubElement(match_element, "GenomicPosition")
        genomic_position_element.text = str(result["genomic_position"])

        genomic_subsequence_element = ET.SubElement(match_element, "GenomicSubsequence")
        genomic_subsequence_element.text = result["genomic_subsequence"]

    # Convert to a string and pretty-print it
    xml_str = ET.tostring(root, encoding='utf-8', xml_declaration=True).decode('utf-8')

    # Use minidom to format the XML string
    pretty_xml_str = minidom.parseString(xml_str).toprettyxml(indent="   ")

    # Write the pretty-printed XML to a file
    with open(output_file, 'w') as f:
        f.write(pretty_xml_str)


def compare_primers_to_genome(primers, genome, output_file):
    """Compare primers against genomes and output results to XML."""

    results = []

    for primer in primers:
        best_match = find_best_match(primer, genome)
        if best_match:
            best_match["primer"] = primer  # Add primer info to match result
            results.append(best_match)

    generate_xml_output(results, output_file)

connector = MongoDBConnector()
jc_virus = connector.fetch_document({"taxonomicID":10632}, CollectionType.PATHOGENS)
sars_cov_2 = connector.fetch_document({"organism":"SARS-CoV-2"}, CollectionType.PATHOGENS)
print(sars_cov_2)
genome = jc_virus['genomic_sequence']

# Example usage
# fasta_file_path = "testing_data.fasta"  # Update this path to your FASTA file

output_xml_path = "XML_Outputs/primer_matches.xml"  # Specify your desired output XML file path

start_time = time.perf_counter()
#compare_primers_to_genome(primer_list, genome.upper(), output_xml_path)
end_time = time.perf_counter()

print(f"Took {end_time - start_time} seconds")
print(f"Results have been written to {output_xml_path}")
