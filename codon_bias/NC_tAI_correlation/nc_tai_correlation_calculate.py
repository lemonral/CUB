import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

species_files = [  
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_deliciosa_longest_orthologues_enc_ratio_results.xlsx",
 "/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_chinensis_longest_orthologues_enc_ratio_results.xlsx",
    "/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_arguta_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_eriantha_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_hemsleyana_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_rufa_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_zhejiangensis_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Rhododendron_simsii_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Coffea_arabica_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Arabidopsis_thaliana_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Cycas_panzhihuaensis_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Vitis_vinifera_longest_orthologues_enc_ratio_results.xlsx",
]

species_names = {
    "/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_deliciosa_longest_orthologues_enc_ratio_results.xlsx":"Actinidia deliciosa",
 "/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_chinensis_longest_orthologues_enc_ratio_results.xlsx":"Actinidia chinensis",
    "/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_arguta_longest_orthologues_enc_ratio_results.xlsx":"Actinidia arguta",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_eriantha_longest_orthologues_enc_ratio_results.xlsx":"Actinidia eriantha",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_hemsleyana_longest_orthologues_enc_ratio_results.xlsx":"Actinidia hemsleyana",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_rufa_longest_orthologues_enc_ratio_results.xlsx": "Actinidia rufa",
"/home/ug0167/zhouyi/codon_bias/enc_value/Actinidia_zhejiangensis_longest_orthologues_enc_ratio_results.xlsx": "Actinidia zhejiangensis",
"/home/ug0167/zhouyi/codon_bias/enc_value/Rhododendron_simsii_longest_orthologues_enc_ratio_results.xlsx": "Rhododendron simsii",
"/home/ug0167/zhouyi/codon_bias/enc_value/Coffea_arabica_longest_orthologues_enc_ratio_results.xlsx": "Coffea arabica",
"/home/ug0167/zhouyi/codon_bias/enc_value/Arabidopsis_thaliana_longest_orthologues_enc_ratio_results.xlsx": "Arabidopsis thaliana",
"/home/ug0167/zhouyi/codon_bias/enc_value/Cycas_panzhihuaensis_longest_orthologues_enc_ratio_results.xlsx":"Cycas panzhihuaensis",
"/home/ug0167/zhouyi/codon_bias/enc_value/Vitis_vinifera_longest_orthologues_enc_ratio_results.xlsx":"Vitis vinifera",
}

# Define the Monte Carlo test function
def monte_carlo_p_value(adjNc, tAI, num_permutations=10000):
    observed_corr, p_value = stats.pearsonr(adjNc, tAI)
    print("Observed correlation:", observed_corr)
    permuted_corrs = []

    for i in range(num_permutations):
        permuted_tAI = np.random.permutation(tAI)
        permuted_corr, _ = stats.pearsonr(adjNc, permuted_tAI)
        permuted_corrs.append(permuted_corr)
                # Debug: Print some permuted correlations
        if i < 10:
            print(f"Permutation {i+1}: permuted_corr = {permuted_corr}")

    permuted_corrs = np.array(permuted_corrs)
    monte_carlo_p_value = np.sum(np.abs(permuted_corrs) >= np.abs(observed_corr)) / num_permutations

    return observed_corr, p_value, monte_carlo_p_value, permuted_corrs

results = []
for excel_file in species_files:
    
    df = pd.read_excel(excel_file)
   
    species = species_names[excel_file]
    # Extract the columns for adjNc and tAI
    adjNc = df['adjNc'].values
    tAI = df['tAI'].values
    ENC = df['ENC']
    # Calculate the observed Pearson correlation
    observed_corr, _ = stats.pearsonr(adjNc, tAI)
    print(f"Observed Pearson correlation: {observed_corr}")
    # Perform the Monte Carlo test
    observed_corr, p_value, monte_carlo_p, permuted_corrs = monte_carlo_p_value(adjNc, tAI)
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
    plt.scatter(ENC, tAI, alpha=0.6, edgecolors='w', linewidth=0.5)
    plt.title(species, fontdict={'style': 'italic'})
    
    plt.xlabel('ENC')
    plt.ylabel('tAI')
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

    plt.savefig(f"/home/ug0167/zhouyi/codon_bias/NC_tAI_correlation/{species.replace(' ', '_')}_orthologs_nc_tAI_scatter_plot.tif", dpi=300, bbox_inches='tight')

    # plt.savefig(f"/home/ug0167/zhouyi/codon_bias/NC_tAI_correlation/{species.replace(" ", "_")}_orthologs_nc_tAI_scatter_plot.tif", dpi=300, bbox_inches='tight')



# Save the results to an Excel file
results_df = pd.DataFrame(results)
results_df.to_excel('/home/ug0167/zhouyi/codon_bias/NC_tAI_correlation/adjNC_tAI_correlation_results.xlsx', index=False)

print("All results and plots have been saved.")

