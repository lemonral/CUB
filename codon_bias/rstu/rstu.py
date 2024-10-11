from Bio import SeqIO

import pandas as pd

# Read the Excel file
file_path = '/home/ug0167/zhouyi/codon_bias/trna_gene/ws_values.xlsx'
df = pd.read_excel(file_path, index_col=0)
df = df.drop(columns=['TGG'])
codon_table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", 
    "TGT": "C", "TGC": "C", 
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", 
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


# Transpose the DataFrame for easier manipulation
df = df.transpose()

# Initialize a DataFrame to store the normalized values
normalized_df = pd.DataFrame(index=df.index, columns=df.columns)

# Calculate the sum of tAI values for each amino acid for each species
amino_acid_sums = {species: {} for species in df.columns}

for codon, amino_acid in codon_table.items():
    if codon in df.index:
        for species in df.columns:
            if amino_acid not in amino_acid_sums[species]:
                amino_acid_sums[species][amino_acid] = 0
            amino_acid_sums[species][amino_acid] += df.at[codon, species]

# Normalize each codon's tAI value by the corresponding amino acid's tAI sum
for codon, amino_acid in codon_table.items():
    if codon in df.index:
        for species in df.columns:
            normalized_df.at[codon, species] = df.at[codon, species] / amino_acid_sums[species][amino_acid]

# Transpose the normalized DataFrame back to the original format
normalized_df = normalized_df.transpose()

print("Normalized DataFrame:")
print(normalized_df)
def get_synonymous_codons(amino_acid):

    synonymous_codons = []
    for codon, amino_acid_in_codon in codon_table.items():
        if amino_acid_in_codon == amino_acid:
            synonymous_codons.append(codon)
    return synonymous_codons
    


# Define the function to calculate the divisor based on the column name
def calculate_divisor(column_name):
    amino_acid = codon_table[column_name]
    synonymous_codons = get_synonymous_codons(amino_acid)
    divisor = 1 / len(synonymous_codons)
    # Example calculation: custom logic based on the column name
    return divisor

# Function to divide each column by its corresponding divisor
def divide_by_column(column):
    divisor = calculate_divisor(column.name)
    return column / divisor

# Apply the function to each column
new_df = normalized_df.apply(divide_by_column)

print("New DataFrame after division using apply:")
print(new_df)
output_excel_path = f"/home/ug0167/zhouyi/codon_bias/rstu/rstu_results.xlsx"

new_df.to_excel(output_excel_path, index=True)

