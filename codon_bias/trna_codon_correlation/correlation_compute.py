import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Load the datasets
rstu = pd.read_csv('/home/ug0167/zhouyi/codon_bias/rstu/rstu_rename.csv', index_col=0)
species_name = rstu.index
print(species_name)
rscu = pd.read_csv('/home/ug0167/zhouyi/codon_bias/rscu_value/rscu_merged_data.csv',index_col=0)
rstu = rstu.T
rscu = rscu.T

# Define the Monte Carlo test function
def monte_carlo_p_value(rstu, rscu, num_permutations=10000):
    observed_corr, p_value = stats.pearsonr(rstu, rscu)
    print("Observed correlation:", observed_corr)
    permuted_corrs = []

    for i in range(num_permutations):
        permuted_rscu = np.random.permutation(rscu)
        permuted_corr, _ = stats.pearsonr(rstu, permuted_rscu)
        permuted_corrs.append(permuted_corr)
                # Debug: Print some permuted correlations
        if i < 10:
            print(f"Permutation {i+1}: permuted_corr = {permuted_corr}")

    permuted_corrs = np.array(permuted_corrs)
    monte_carlo_p_value = np.sum(np.abs(permuted_corrs) >= np.abs(observed_corr)) / num_permutations

    return observed_corr, p_value, monte_carlo_p_value, permuted_corrs

results = []
for species in species_name:
    # Extract the columns for adjNc and tAI
    RSTU = rstu[species]
    RSCU = rscu[species]
    # Calculate the observed Pearson correlation
    observed_corr, _ = stats.pearsonr(RSTU, RSCU)
    print(f"Observed Pearson correlation: {observed_corr}")
    # Perform the Monte Carlo test
    observed_corr, p_value, monte_carlo_p, permuted_corrs = monte_carlo_p_value(RSTU, RSCU)
    print(f"Monte Carlo Pearson correlation: {observed_corr}, p-value: {monte_carlo_p:.2e}")
        # Save the results
    results.append({
        'Species': species,
        'Observed Correlation': observed_corr,
        'p_value': p_value,
        'Monte Carlo P-value': monte_carlo_p
    })

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(RSTU, RSCU, alpha=0.6, edgecolors='w', linewidth=0.5)
    plt.title(species, fontdict={'style': 'italic'})
    
    plt.xlabel('RSTU')
    plt.ylabel('RSCU')
    plt.grid(True)
 # 显示R方值
    def format_p_value(p):
        if p < 0.001:
            return "$p$ < 0.001"
        elif p < 0.01:
            return "$p$ < 0.01"
        elif p < 0.05:
            return "$p$ < 0.05"
        else:
            return f"$p$ = {p:.2f}"
    # Get the axis limits
    xlim = plt.gca().get_xlim()
    ylim = plt.gca().get_ylim()

# Fine-tune text placement by slightly adjusting coordinates
    x_text = xlim[1] - (xlim[1] - xlim[0]) * 0.05
    y_text = ylim[1] - (ylim[1] - ylim[0]) * 0.05

    # Set text in the upper right corner with fine-tuned placement
    plt.text(x_text, y_text, f"S = {observed_corr:.3f}, {format_p_value(monte_carlo_p)}",
            horizontalalignment='right',
            verticalalignment='top',
            bbox=dict(facecolor='white', alpha=0.5))

    plt.savefig(f"/home/ug0167/zhouyi/codon_bias/rscu_rstu_correlation/{species.replace(' ', '_')}_RSTU_RSCU_scatter_plot.tif", dpi=300, bbox_inches='tight')

    # plt.savefig(f"/home/ug0167/zhouyi/codon_bias/NC_tAI_correlation/{species.replace(" ", "_")}_orthologs_nc_tAI_scatter_plot.tif", dpi=300, bbox_inches='tight')



# Save the results to an Excel file
results_df = pd.DataFrame(results)
results_df.to_excel('/home/ug0167/zhouyi/codon_bias/rscu_rstu_correlation/RSTU_RSCU_correlation_results.xlsx', index=False)

print("All results and plots have been saved.")


