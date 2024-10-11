# 导入需要的模块
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re



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

# 遍历每个物种的Excel文件，读取gc3s值，并将其追加到all_species_df中
for excel_file in species_files:
    # 读取Excel文件中的数据，假设第一列是基因ID，第二列是gc3s
    df = pd.read_excel(excel_file)
    # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
    species = species_names[excel_file]
    # 获取gc3s的值，转换为numpy数组
    y = df["A3/(A3+T3)"]
    x = df["G3/(G3+C3)"]
    # Plot the pr2 scatterplot
    plt.figure(figsize=(10, 6))
    plt.xlabel("G3/(G3+C3)")
    plt.ylabel("A3/(A3+T3)")
    plt.scatter(x, y, color="black",s = 0.1)
    # 限制 x 和 y 轴刻度
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    if species == "Brassica napus (merged)":
        formatted_species = r"\textit{Brassica napus} (merged)"
        plt.title(formatted_species, fontdict={'usetex': True})
    else:
        plt.title(species,fontdict={'style': 'italic'})
    # formatted_species = r"\textit{Brassica napus} (merged)"
    # plt.title(formatted_species, fontdict={'usetex': True})
    # plt.title(species, fontdict={'style': 'italic'})
    # 添加 x=0.5，y=0.5 的中轴线
    plt.axhline(0.5, color="black", linestyle="--")
    plt.axvline(0.5, color="black", linestyle="--")
    plt.savefig(f"/home/ug0167/zhouyi/codon_bias/pr2_plot/{species}pr2_plot.png", dpi=300, bbox_inches='tight')
    print(f"{species}pr2_plot has been saved")