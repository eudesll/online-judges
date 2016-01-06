"""
Rosalind
Problem Name: Transcribing DNA into RNA
"""


def transcipt_to_rna(dna):
    return dna.replace('T', 'U').replace('\n', '')

dna = '''
TCAGTGGTTCTGGGCCACAGCCGCGTGGAGATCGCAGCTCAAATGGCGCT
TTCATGACCATTTCTTCCAACGTTGCCCATGATGTCCCCAGTGGTGGACT
ATTACGTCGGTTTAACTGCCAGTGACAGATTAAGCTGTTTTTAGTACTGA
ACAACAGTTTCAGCCTTACACCGTTCAATATGTCTTTGAGCTCGGCTTCG
CCTCGCGCATTGAAGATTGGGGGCGGCTAGGTCCCAGAATCCGTTCCCTT
CATCACCGCGCCCTACCTGGGTTTCTGTCACAGAAGCCATGTCGAGTTAT
CTACTGCCTAGAGATGCGCCTTAATACTTAAGAATCAAGCGTGAGCCAGT
ATGTTACCTGGGCGTTCAGCCCTGCTTATGGGGCCATCCCGGTCATTAGT
AAGATTGGTAGCAAAGATCTTGCATTGGAGGTGCAGTCTTCTTTGATTGG
AAGGTTTATTCACCCGCCATGATAAATCCTTATTAGGTCTGGAAGTCGGG
TACTTATAACGTGTTGAGGCGTAATTCTGAGATGCCCAATCGGTAGTCTG
TGGTCGAAGTATCGGCCGCCCCCCTCTAGTCGATAACTGTGCTTTTAGTT
TTTGCGAGTTTGTAGGCGACTGATGCGGTACGCCGCGGCAGTCTGTGATT
TCTGCTATCATACGATTTCGTCCAGGATTATCGCCAACTGCATTCGTCAA
ATAGGTGCTAGCATATACCTCATGTAGCATCGGCCGCCGAACAAGAACGG
TCAGGAAAAGTCTCCCCCTTTATGGTGCGTCACCTCGAGTGCAGCTAATG
CAGGTAGAGTGATCTAGATTCTAGTACTAGATGATGCATGAGTTGGTTCC
GGGATTGGTGGTTGTTCGGGACGAAAAAGTCGGGCTCTGGGTGATGGTAT
CCCTCGTGCCTGAACAGGTGTGGACGAGGTGCAAGGCTCCA
'''
print(transcipt_to_rna(dna))
