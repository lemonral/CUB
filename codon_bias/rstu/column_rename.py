import pandas as pd
df = pd.read_excel("/home/ug0167/zhouyi/codon_bias/rstu/rstu_results.xlsx",index_col=0)
print(df)
# Convert index to string and replace underscores with spaces
df.index = df.index.str.replace('_', ' ')
print("\nIndex after replacing underscores:")
print(df.index)

codon_to_amino_acid_ordered = {
    'TTA': 'Leu', 'TTG': 'Leu', 'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
    'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser', 'AGT': 'Ser', 'AGC': 'Ser',
    'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
    'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
    'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile',
    'TTT': 'Phe', 'TTC': 'Phe',
    'TAT': 'Tyr', 'TAC': 'Tyr',
    'CAT': 'His', 'CAC': 'His',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AAT': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys',
    'GAT': 'Asp', 'GAC': 'Asp',
    'GAA': 'Glu', 'GAG': 'Glu',
    'TGT': 'Cys', 'TGC': 'Cys',
     
}
# Create a new dictionary for renaming
new_column_names = {codon: f"{codon}({amino_acid})" for codon, amino_acid in codon_to_amino_acid_ordered.items()}

# Add 'species' to the new column names to maintain it
# new_column_names['species'] = 'species'

# Rename columns
df.rename(columns=new_column_names, inplace=True)

# Reorder columns
column_order = [f"{codon}({amino_acid})" for codon, amino_acid in codon_to_amino_acid_ordered.items()]
df = df[column_order]
print(df)
df.to_csv('/home/ug0167/zhouyi/codon_bias/rstu/rstu_rename.csv')