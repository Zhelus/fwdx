from Bio.Blast import NCBIWWW
from Bio import SeqIO
from Bio.Blast import NCBIXML
import xml.etree.ElementTree as ET
from xml.dom import minidom

""" 
Primers
FWDX00183 AAT GCA ACA GTG CAA TCT CA

FWDX00184 GGC CCA ACA CCA AAT TCATC

FWDX00185 TTG GGT TCC TGA TCC CAC CAG

FWDX00186 AAG TAC ATG CCC ATA AGC AA

FWDX00187 AGA CAGCCATATGCAGTAG

FWDX00188 AAA CCT GCT TAG TTT CTT CTG GTT CTT  
"""


# Read the query sequence from your FASTA file
with open("test_data.fasta", "r") as fasta_file:
    record = next(SeqIO.parse(fasta_file, "fasta"))

# Perform the BLAST search
print("Performing BLAST search...")
result_handle = NCBIWWW.qblast("blastn", "nr", record.seq,
                               entrez_query="Homo sapiens[organism]",
                               megablast=True)

# Parse the results
blast_records = NCBIXML.parse(result_handle)

# Create the root element
root = ET.Element("BlastResults")

# Iterate through the blast records
for blast_record in blast_records:
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            # Create an alignment element
            alignment_elem = ET.SubElement(root, "Alignment")

            # Add child elements with the requested information
            ET.SubElement(alignment_elem, "Sequence").text = alignment.title
            ET.SubElement(alignment_elem, "Length").text = str(alignment.length)
            ET.SubElement(alignment_elem, "E-value").text = str(hsp.expect)
            ET.SubElement(alignment_elem, "Score").text = str(hsp.score)
            ET.SubElement(alignment_elem, "Identities").text = str(hsp.identities)
            ET.SubElement(alignment_elem, "AlignmentLength").text = str(hsp.align_length)
            ET.SubElement(alignment_elem, "Score").text = str(hsp.score)
            ET.SubElement(alignment_elem, "Mismatches").text = str(hsp.align_length - hsp.identities)
            ET.SubElement(alignment_elem, "Gaps").text = str(hsp.gaps)
            ET.SubElement(alignment_elem, "QuerySequence").text = hsp.query
            ET.SubElement(alignment_elem, "MatchSequence").text = hsp.match
            ET.SubElement(alignment_elem, "SubjectSequence").text = hsp.sbjct

# Convert the ElementTree to a string and pretty print it
xml_string = ET.tostring(root, encoding='unicode')
pretty_xml = minidom.parseString(xml_string).toprettyxml(indent="  ")

# Write the pretty-printed XML to a file
with open("XML_Outputs/blast_results.xml", "w") as xml_file:
    xml_file.write(pretty_xml)

print("BLAST search complete. Results saved to 'blast_results.xml'")

# Close the result handle
result_handle.close()