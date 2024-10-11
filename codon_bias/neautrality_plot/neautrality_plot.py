# 导入需要的模块
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import linregress

species_files = [
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_eriantha_longest_orthologues_gene_parameters.xlsx",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_hemsleyana_longest_orthologues_gene_parameters.xlsx",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_rufa_longest_orthologues_gene_parameters.xlsx",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_zhejiangensis_longest_orthologues_gene_parameters.xlsx",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_arguta_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_chinensis_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_deliciosa_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Arabidopsis_thaliana_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Coffea_arabica_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Cycas_panzhihuaensis_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Rhododendron_simsii_longest_orthologues_gene_parameters.xlsx",
"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Vitis_vinifera_longest_orthologues_gene_parameters.xlsx"
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_eriantha_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_hemsleyana_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_rufa_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_zhejiangensis_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_arabidopsis_thaliana_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Coffea_arabica_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Rhododendron_simsii_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Vitis_vinifera_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/delicio_cds_filter_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/hongyang4_CDS_filter_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_napus_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_Brassica_rapa_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_rapa_gene_parameters.xlsx"
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_arguta_cds_gene_parameters.xlsx",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Cycas_panzhihuaensis_genome_cds_gene_parameters.xlsx"

]

species_names = {
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_deliciosa_longest_orthologues_gene_parameters.xlsx":"Actinidia deliciosa",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_eriantha_longest_orthologues_gene_parameters.xlsx":"Actinidia eriantha",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_hemsleyana_longest_orthologues_gene_parameters.xlsx":"Actinidia hemsleyana",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_rufa_longest_orthologues_gene_parameters.xlsx": "Actinidia rufa",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_zhejiangensis_longest_orthologues_gene_parameters.xlsx": "Actinidia zhejiangensis",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Arabidopsis_thaliana_longest_orthologues_gene_parameters.xlsx": "Arabidopsis thaliana",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Coffea_arabica_longest_orthologues_gene_parameters.xlsx": "Coffea arabica",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Rhododendron_simsii_longest_orthologues_gene_parameters.xlsx": "Rhododendron simsii",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Vitis_vinifera_longest_orthologues_gene_parameters.xlsx": "Vitis vinifera",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_chinensis_longest_orthologues_gene_parameters.xlsx":"Actinidia chinensis",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_napus_gene_parameters.xlsx": "Brassica napus",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_Brassica_rapa_gene_parameters.xlsx":"Brassica napus (merged)",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_gene_parameters.xlsx":"Brassica oleracea",
    # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_rapa_gene_parameters.xlsx": "Brassica rapa"
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Actinidia_arguta_longest_orthologues_gene_parameters.xlsx":"Actinidia arguta",
    "/home/ug0167/zhouyi/codon_bias/species_gene_parameter/Cycas_panzhihuaensis_longest_orthologues_gene_parameters.xlsx":"Cycas panzhihuaensis"
    }


# species_files = [
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_eriantha_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_hemsleyana_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_rufa_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_zhejiangensis_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_arabidopsis_thaliana_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Coffea_arabica_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Rhododendron_simsii_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Vitis_vinifera_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/delicio_cds_filter_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/hongyang4_CDS_filter_gene_parameters.xlsx",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_napus_gene_parameters.xlsx",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_Brassica_rapa_gene_parameters.xlsx",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_gene_parameters.xlsx",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_rapa_gene_parameters.xlsx"  
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_arguta_cds_gene_parameters.xlsx",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Cycas_panzhihuaensis_genome_cds_gene_parameters.xlsx"  
# ]

# species_names = {
#     "/home/ug0167/zhouyi_file/species_genome_parameter/delicio_cds_filter_gene_parameters.xlsx":"Actinidia deliciosa",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_eriantha_cds_gene_parameters.xlsx":"Actinidia eriantha",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_hemsleyana_cds_gene_parameters.xlsx":"Actinidia hemsleyana",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_rufa_cds_gene_parameters.xlsx": "Actinidia rufa",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_zhejiangensis_cds_gene_parameters.xlsx": "Actinidia zhejiangensis",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_arabidopsis_thaliana_cds_gene_parameters.xlsx": "Arabidopsis thaliana",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Coffea_arabica_cds_gene_parameters.xlsx": "Coffea arabica",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Rhododendron_simsii_cds_gene_parameters.xlsx": "Rhododendron simsii",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Vitis_vinifera_cds_gene_parameters.xlsx": "Vitis vinifera",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/hongyang4_CDS_filter_gene_parameters.xlsx":"Actinidia chinensis",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_napus_gene_parameters.xlsx": "Brassica napus",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_Brassica_rapa_gene_parameters.xlsx":"Brassica napus (merged)",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_oleracea_gene_parameters.xlsx":"Brassica oleracea",
#     # "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Brassica_rapa_gene_parameters.xlsx": "Brassica rapa"
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Actinidia_arguta_cds_gene_parameters.xlsx":"Actinidia arguta",
#     "/home/ug0167/zhouyi_file/species_genome_parameter/filtered_Cycas_panzhihuaensis_genome_cds_gene_parameters.xlsx":"Cycas panzhihuaensis"
#     }

# 遍历每个物种的Excel文件，读取gc3s值，并将其追加到all_species_df中
for excel_file in species_files:
    # 读取Excel文件中的数据，假设第一列是基因ID，第二列是gc3s
    df = pd.read_excel(excel_file)
    # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
    species = species_names[excel_file]
    # 获取gc3s的值，转换为numpy数组
    y = df["GC12"]
    x = df["GC3"]
    # Plot the pr2 scatterplot
    plt.figure(figsize=(10, 6))
    plt.xlabel("GC3)")
    plt.ylabel("GC12")
     # 绘制散点图和拟合曲线
    g = sns.regplot(x=x, y=y, color='black', scatter_kws={'s': 0.1}, line_kws={'color': 'blue'}) # 使用sns.regplot()函数
    z = np.polyfit(x, y, 1) # 计算一次多项式的系数
    plt.xlim(0, 1)
    plt.ylim(0, 1)

    if species == "Brassica napus (merged)":
        formatted_species = r"\textit{Brassica napus} (merged)"
        plt.title(formatted_species, fontdict={'usetex': True})
    else:
        plt.title(species,fontdict={'style': 'italic'})

    plt.plot(x, np.poly1d(z)(x), color='blue') # 绘制拟合曲线
    plt.text(0.75, 0.9, f"y = {z[0]:.2f}x + {z[1]:.2f}", fontsize=12) # 显示拟合公式
    # 计算和显示R方值
    r = np.corrcoef(x, y)[0, 1]**2 # 计算R方值
    plt.text(0.75, 0.85, f"R^2 = {r:.2f}", fontsize=12) # 显示R方值
    # 计算拟合线的p值
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    def format_p_value(p):
        if p < 0.001:
            return "$p$ < 0.001"
        elif p < 0.01:
            return "$p$ < 0.01"
        elif p < 0.05:
            return "$p$ < 0.05"
        else:
            return f"$p$ = {p:.2f}"
    plt.text(0.75, 0.8, format_p_value(p_value), fontsize=12)  # 显示p值
    # 添加拟合公式
    # z = g.get_lines()[0].get_data()[1] # 获取拟合曲线的y值
    # 计算和显示R方值
    # r = np.corrcoef(x, y)[0, 1]**2 # 计算R方值
    # plt.text(0.8, 0.8, f"y = {z[1]-z[0]:.2f}x + {z[0]:.2f}", f"R^2 = {r:.2f}",fontsize=12) # 显示拟合公式
    # plt.text(0.8, 0.7, f"R^2 = {r:.2f}", fontsize=12) # 显示R方值
    plt.savefig(f"/home/ug0167/zhouyi/codon_bias/neautrality_plot/{species}Neutrality_plot.tif", dpi=300, bbox_inches='tight')
    print(f"{species}ne2_plot has been saved")