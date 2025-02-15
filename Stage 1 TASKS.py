
# Standard genetic code (codon to amino acid mapping)
CODON_TABLE = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
    'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'
}

def translate_dna_to_protein(dna_sequence):
    # Step 1: Convert DNA to uppercase
    dna_sequence = dna_sequence.upper()
    
    # Step 2: Split into codons
    codons = [dna_sequence[i:i+3] for i in range(0, len(dna_sequence), 3)]
    
    # Step 3: Translate codons to amino acids
    protein_sequence = ''
    for codon in codons:
        if len(codon) == 3:  # Ensure it's a complete codon
            amino_acid = CODON_TABLE.get(codon, '?')  # Use '?' for unknown codons
            if amino_acid == '_':  # Stop codon
                break
            protein_sequence += amino_acid
    
    return protein_sequence

# Example DNA sequence
dna_sequence = "ATGGCCATTGTAATGGGCCGCTGAA"

# Translate to protein
protein_sequence = translate_dna_to_protein(dna_sequence)
print(f"DNA: {dna_sequence}")
print(f"Protein: {protein_sequence}")
