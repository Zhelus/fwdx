"""
Uploading a long genomic sequence is crashing mongosh, this code is an attempt to solve this issue.
Last uploaded: Kyle Stagner
Date: 2024/11/3
"""

from backend.src.database.mongodb.mongodb_connector import MongoDBConnector

# Instantiate the MongoDB connector
connector = MongoDBConnector()
connector.ping()

# Connect to the 'Pathogens' collection
collection = connector.database['Pathogens']

# Long string to insert
long_string = "GCCTCGGCCTCCTGTATATATAAAAAAAAGGGAAGGGATGGCTGCCAGCCAAGCATGAGCTCATACCTAGGGAGCCAACCAGCTAACAGCCAGTAAACAAAGCACAAGGCTGTATATATAAAAAAAAGGGAAGGGATGGCTGCCAGCCAAGCATGAGCTCATACCTAGGGAGCCAACCAGCTAACAGCCAGTAAACAAAGCACAAGGGGAAGTGGAAAGCAGCCAAGGGAACATGTTTTGCGAGCCAGAGCTGTTTTGGCTTGTCACCAGCTGGCCATGGTTCTTCGCCAGCTGTCACGTAAGGCTTCTGTGAAAGTTAGTAAAACCTGGAGTGGAACTAAAAAAAGAGCTCAAAGGATTTTAATTTTTTTGTTAGAATTTTTGCTGGACTTTTGCACAGGTGAAGACAGTGTAGACGGGAAAAAAAGACAGAGACACAGTGGTTTGACTGAGCAGACATACAGTGCTTTGCCTGAACCAAAAGCTACATAGGTAAGTAATGTTTTTTTTTGTGTTTTCAGGTTCATGGGTGCCGCACTTGCACTTTTGGGGGACCTAGTTGCTACTGTTTCTGAGGCTGCTGCTGCCACAGGATTTTCAGTAGCTGAAATTGCTGCTGGAGAGGCTGCTGCTACTATAGAAGTTGAAATTGCATCCCTTGCTACTGTAGAGGGGATTACAAGTACCTCTGAGGCTATAGCTGCTATAGGCCTTACTCCTGAAACATATGCTGTAATAACTGGAGCTCCGGGGGCTGTAGCTGGGTTTGCTGCATTGGTTCAAACTGTAACTGGTGGTAGTGCTATTGCTCAGTTGGGATATAGATTTTTTGCTGACTGGGATCATAAAGTTTCAACAGTTGGGCTTTTTCAGCAGCCAGCTATGGCTTTACAATTATTTAATCCAGAAGACTACTATGATATTTTATTTCCTGGAGTGAATGCCTTTGTTAACAATATTCACTATTTAGATCCTAGACATTGGGGCCCGTCCTTGTTCTCCACAATCTCCCAGGCTTTTTGGAATCTTGTTAGAGATGATTTGCCAGCCTTAACCTCTCAGGAAATTCAGAGAAGAACCCAAAAACTATTTGTTGAAAGTTTAGCAAGGTTTTTGGAAGAAACTACTTGGGCAATAGTTAATTCACCAGCTAACTTATATAATTATATTTCAGACTATTATTCTAGATTGTCTCCAGTTAGGCCCTCTATGGTAAGGCAAGTTGCCCAAAGGGAGGGAACCTATATTTCTTTTGGCCACTCATACACCCAAAGTATAGATGATGCAGACAGCATTCAAGAAGTTACCCAAAGGCTAGATTTAAAAACCCCAAATGTGCAATCTGGTGAATTTATAGAAAGAAGTATTGCACCAGGAGGTGCAAATCAAAGATCTGCTCCTCAATGGATGTTGCCTTTACTTTTAGGGTTGTACGGGACTGTAACACCTGCTCTTGAAGCATATGAAGATGGCCCCAACAAAAAGAAAAGGAGAAAGGAAGGACCCCGTGCAAGTTCCAAAACTTCTTATAAGAGGAGGAGTAGAAGTTCTAGAAGTTAAAACTGGGGTTGACTCAATTACAGAGGTAGAATGCTTTTTAACTCCAGAAATGGGTGACCCAGATGAGCATCTTAGGGGTTTTAGTAAGTCAATATCTATATCAGATACATTTGAAAGTGACTCCCCAAATAGGGACATGCTTCCTTGTTACAGTGTGGCCAGAATTCCACTACCCAATCTAAATGAGGATCTAACCTGTGGAAATATACTCATGTGGGAGGCTGTGACCTTAAAAACTGAGGTTATAGGGGTGACAAGTTTGATGAATGTGCACTCTAATGGGCAAGCAACTCATGACAATGGTGCAGGGAAGCCAGTGCAGGGCACCAGCTTTCATTTTTTTTCTGTTGGGGGGGAGGCTTTAGAATTACAGGGGGTGCTTTTTAATTACAGAACAAAGTACCCAGATGGAACAATTTTTCCAAAGAATGCCACAGTGCAATCTCAAGTCATGAACACAGAGCACAAGGCGTACCTAGATAAGAACAAAGCATATCCTGTTGAATGTTGGGTTCCTGATCCCACCAGAAATGAAAACACAAGATATTTTGGGACACTAACAGGAGGAGAAAATGTTCCTCCAGTTCTTCATATAACAAACACTGCCACAACAGTGTTGCTTGATGAATTTGGTGTTGGGCCACTTTGCAAAGGTGACAACTTATACTTGTCAGCTGTTGATGTCTGTGGCATGTTTACAAACAGGTCTGGTTCCCAGCAGTGGAGAGGACTCTCCAGATATTTTAAGGTGCAGCTAAGGAAAAGGAGGGTTAAAAACCCCTACCCAATTTCTTTCCTTCTTACTGATTTAATTAACAGAAGGACTCCTAGAGTTGATGGGCAGCCTATGTATGGCATGGATGCTCAAGTAGAGGAGGTTAGAGTTTTTGAGGGAACAGAGGAGCTTCCAGGGGACCCAGACATGATGAGATACGTTGACAAATATGGACAGTTGCAGACAAAAATGCTGTAATCAAAAGCCTTTATTGTAATATGCAGTACATTTTAATAAAGTATAACCAGCTTTACTTAACAGTTGCAGTTATTTTGGGGGAGGGGTCTTTGGTTTTTTGAAACATTGAAAGCCTTTACAGATGTGAAAAGTGCAGTTTTCCTGTGTGTCTGCACCAGAGGCTTCTGAGACCTGGGAAAAGCATTGTGATTGTGATTCAGTGCTTGATCCATGTCCAGAGTCTTCTGCTTCAGAATCTTCCTCTCTAGGAAAGTCAAGAATGGGTCTCCCCATACCAACATTAGCTTTCATAGTAGAAAATGTATACATGCTTATTTCTAAATCCAGCCTTTCTTTCCACTGCACAATCCTCTCATGAATGGCAGCTGCAAAGTCAGCAACTGGCCTAAACCAGATTAAAAGCAAAAGCAAAGTCATACCACTTTGCAAAATCCTTTTTTCTAGCAAATACTCAGAGCAGCTTAGTGATTTTCTCAGGTAGGCCTTTGGTCTAAAATCTATCTGCCTTACAAATCTGGCCTGTAAAGTTCTAGGCACTGAATATTCATTCATGGTTACAATTCCAGGTGGAAACACCTGTGTTCTTTTGTTTTGGTGTTTTCTCTCTAAATTAACTTTTACACTTCCATCTAAGTAATCTCTTAAGCAATCAAGGTTGCTTATGCCATGCCCTGAAGGTAAATCCCTTGACTCTGCACCAGTGCCTTTTACATCCTCAAATACAACCATAAACTGATCTATACCCACTCCTAATTCAAAGTTTAATCTTTCTAATGGCATATTAACATTTAATGACTTTCCCCCACAGAGATCAAGTAAAGCTGCAGCTAAAGTAGTTTTGCCACTGTCTATTGGCCCCTTGAATAGCCAGTACCTTTTTTTTGGAATGTTTAATACAATGCATTTTAGAAAGTCATAAATAACAGTGTCCATTTGAGGCAGCAAGCAATGAATCCAGGCCACCCCAGCCATATATTGCTCTAAAACAGCATTGCCATGTGCCCCAAAAATTAAGTCCATTTTATCAAGCAAGAAATTAAACCTTTCAACTAACATTTCTTCTCTGGTCATGTGGATGCTGTCAACCCTTTGTTTGGCTGCTACAGTATCAACAGCCTGCTGGCAAATGCTTTTTTGATTTTTGCTATCTGCAAAAATTTGGGCATTATAATAGTGTTTTTCATGATGGTTAAAGTGATTTGGCTGATCCTTTTTTTCACATTTTTTGCATTGCTGTGGGTTTTCCTGAAAGTCTAAGTACATGCCCATAAGCAAAAAAACATCCTCACACTTGGTTTCCAAGGCATACTGTGTAACTAATTTCCATGAAACCTGCTTAGTTTCTTCTGGTTCTTCTGGGTTAAAGTCATGCTCCTTAAGGCCCCCCTGAATACTTTCTTCCACTACTGCATATGGCTGTCTACACAGGGCACTATAAAACAAGTATTCCTTATTCACACCTTTACAAATTAAAAAACTAAAGGTACATAGTTTTTGACAGTAGTTATTAATTGCTGACACTCTATGTCTATGTGGTGTTAAGAAAAACAAAATATTATGACCCCCAAAACCATGTCTACTTATAAAAGTTACAGAATATTTTTCCATAAGTTTCTTATATAAAATTTGAGCTTTTTCTTTAGTGGTATACACAGCAAAAGAAGCAACAGTTCTATTACTAAACACAGCTTGACTGAGGAATGCATGCAGATCTACAGGAAAGTCTTTAGGGTCTTCTACCTTTTTTTTCTTTTTAGGTGGGGTAGAGTGTTGGGATCCTGTGTTTTCATCATCACTGGCAAACATTTCTTCATGGCAAAACAGGTCTTCATCCCACTTCTCATTAAATGTATTCCACCAGGATTCCCATTCATCTGTTCCATAGGTTGGCACCTAAAAAAAAACAATTAAGTTTATTGTAAAAAACAAAATGCCCTGCAAAAGAAAAATAGTGGTTTACCTTAAAGCTTTAGATCCCTGTAGGGGGTGTCTCCAAGAACTTTCTCCCAGCAATGAAGAGCTTCTTGGGTTAAGTCACACCCAAACCATTGTCTGAAGCAATCAAAGCAATAGCAATCTATCCACACAAGTGGGCTGCTTCTTAAAAATTTTCTGTTTCTATGCCTTAATTTTAGCATGCACATTAAACAGGGGCAATGCACTGAAGGATTAGTGGCACAGTTAGGCCATTCCTTGCAATAAAGGGTATCAGAATTAGGAGGAAAATCACAACCAACCTCTGAACTATTCCATGTACCAAAATCAGGCTGATGAGCAACTTTTACACCTTGTTCCATTTTTTTATATAAAAAATTCATTCTCTTCATCTTGTCTTCGTCCCCACCTTTATCAGGGTGGAGTTCTTTGCATTTTTTCAGATAAGCTTTTCTCATGACAGGAATGTTCCCCCATGCAGACCTATCAAGGCCTAATAAATCCATAAGCTCCATGGATTCCTCCCTATTCAGCACTTTGTCCATTTTAGCTTTTTGCAGCAAAAAATTACTGCAAAAAAGGGAAAAACAAGGGAATTTCCCTGGCCTCCTAAAAAGCCTCCACGCCCTTACTACTTCTGAGTAAGCTTGGAGGCGGAGGCG"

# Update the document
result = collection.update_one(
    {"TaxonomyID": "10632"},
    {"$set": {"genomicSequence": long_string}}
)

if result.modified_count > 0:
    print("Document updated successfully.")
else:
    print("No document matched the query.")

# Close the database connection
del connector.client