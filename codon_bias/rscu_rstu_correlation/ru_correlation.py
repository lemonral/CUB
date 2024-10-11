import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the first dataset
data1 = pd.read_csv('/home/ug0167/zhouyi/codon_bias/rstu/rstu_rename.csv')
# Load the second dataset
data2 = pd.read_csv('/home/ug0167/zhouyi/codon_bias/rscu_value/rscu_merged_data.csv')

# Rename columns to differentiate between the two datasets
data1.columns = ['species'] + [col + '_1' for col in data1.columns if col != 'species']
data2.columns = ['species'] + [col + '_2' for col in data2.columns if col != 'species']

# Merge the two datasets on the 'species' column
merged_data = pd.merge(data1, data2, on='species')

# Drop the 'species' column to calculate correlation only for numerical data
correlation_matrix = merged_data.drop('species', axis=1).corr()

# Save the correlation matrix to a CSV file
correlation_matrix.to_csv('/home/ug0167/zhouyi/codon_bias/rscu_rstu_correlation/correlation_matrix.csv')

# Display the correlation matrix
print(correlation_matrix)

# Plot the heatmap for the correlation matrix
plt.figure(figsize=(20, 15))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix Heatmap')
plt.savefig('/home/ug0167/zhouyi/codon_bias/rscu_rstu_correlation/correlation_plot.tif', dpi=300, bbox_inches='tight')
plt.show()
