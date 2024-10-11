
import pandas as pd
import numpy as np
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
    # "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx"
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
    # "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx":"Actinidia deliciosa",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx":"Actinidia eriantha",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx":"Actinidia hemsleyana",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx": "Actinidia rufa",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx": "Actinidia zhejiangensis",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx": "Arabidopsis thaliana",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx": "Coffea arabica",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx": "Rhododendron simsii",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx":"Vitis vinifera",
    # "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx":"Actinidia chinensis",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx":"Actinidia arguta",
    # "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx":"Cycas panzhihuaensis"
}

# species_files = [
#     # "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_napus_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_Brassica_rapa_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_rapa_enc_ratio_results.xlsx"
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx"
# ]

# species_names = {
#     # "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx":"Actinidia deliciosa",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx":"Actinidia eriantha",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx":"Actinidia hemsleyana",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx": "Actinidia rufa",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx": "Actinidia zhejiangensis",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx": "Arabidopsis thaliana",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx": "Coffea arabica",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx": "Rhododendron simsii",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx":"Vitis vinifera",
#     # "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx":"Actinidia chinensis",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_napus_enc_ratio_results.xlsx":"Brassica napus",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_Brassica_rapa_enc_ratio_results.xlsx":"Brassica napus (merged)",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_enc_ratio_results.xlsx":"Brassica oleracea",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_rapa_enc_ratio_results.xlsx":"Brassica rapa"
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx":"Cycas panzhihuaensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx":"Actinidia arguta"
#     }

# 遍历每个物种的Excel文件，读取gc3s值，并将其追加到all_species_df中
for excel_file in species_files:
    # 读取Excel文件中的数据，假设第一列是基因ID，第二列是gc3s
    df = pd.read_excel(excel_file)
    # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
    species = species_names[excel_file]
    # 获取gc3s的值，转换为numpy数组
    GC3s = df["GC3s"]
    ENC = df['ENC']

    # Plot the ENC-GC3 scatterplot
    plt.figure(figsize=(10, 6))
    # 获取唯一的GC3s值
    unique_GC3s = np.unique(GC3s)
    
    # 计算已知函数的值，这里使用unique_GC3s作为x坐标
    enc_expected = 2 + unique_GC3s + 29 / (unique_GC3s**2 + (1 - unique_GC3s)**2)

    # Calculate y values for the fitted curve
    # y_fit = quadratic(x_fit, *popt)
    plt.xlabel("GC3s")
    plt.ylabel("ENC")
    plt.scatter(GC3s, ENC, color="black",s = 0.1)
    plt.plot(unique_GC3s, enc_expected,linewidth=1,color='blue')
    # formatted_species = r"\textit{Brassica napus} (merged)"
    # plt.title(formatted_species, fontdict={'usetex': True})
    plt.title(species, fontdict={'style': 'italic'})
    plt.show()
    plt.savefig(f"/home/ug0167/zhouyi/codon_bias/enc_gc3_plot/{species}_orthologue_enc_gc3_plot.png", dpi=300, bbox_inches='tight')

# # Import libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# # from scipy.optimize import curve_fit

# species_files = [
#     "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx",
    
# ]

# species_names = {"/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx":"Actinidia deliciosa",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx":"Actinidia eriantha",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx":"Actinidia hemsleyana",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx": "Actinidia rufa",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx": "Actinidia zhejiangensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx": "Arabidopsis thaliana",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx": "Coffea arabica",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx": "Rhododendron simsii",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx":"Vitis vinifera",
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx":"Actinidia chinensis"}

# # 预先分配内存空间，假设每个物种有1000个基因 # 修改
# GC3s = np.zeros((len(species_files), 1000)) # 创建一个二维数组，存储每个物种的GC3s值
# ENC = np.zeros((len(species_files), 1000)) # 创建一个二维数组，存储每个物种的ENC值
# species = [] # 创建一个列表，存储每个物种的名称

# # 遍历每个物种的Excel文件，读取gc3s和enc值，并存储到相应的数组中 # 修改
# for i, excel_file in enumerate(species_files):
#     # 读取Excel文件中的数据，假设第一列是基因ID，第二列是gc3s，第三列是enc
#     df = pd.read_excel(excel_file)
#     # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
#     species_name = species_names[excel_file]
#     # 将物种的名称追加到列表中
#     species.append(species_name)
#     # 获取gc3s和enc的值，转换为numpy数组
#     GC3s[i] = df["GC3s"].to_numpy() # 将第i个物种的GC3s值存储到第i行
#     ENC[i] = df['ENC'].to_numpy() # 将第i个物种的ENC值存储到第i行

# # Plot the ENC-GC3 scatterplot
# # 使用一个figure对象，创建多个子图，每个子图绘制一个物种的散点图 # 修改
# fig, axes = plt.subplots(nrows=5, ncols=2, figsize=(20, 30)) # 创建一个包含10个子图的figure对象
# # 获取唯一的GC3s值，使用向量化的方法，而不是循环 # 修改
# unique_GC3s = np.unique(GC3s) # 使用numpy.unique函数，获取所有物种的GC3s值的唯一值
# # 计算已知函数的值，这里使用unique_GC3s作为x坐标
# enc_expected = 2 + unique_GC3s + 29 / (unique_GC3s**2 + (1 - unique_GC3s)**2)

# # 遍历每个物种，绘制散点图和拟合曲线 # 修改
# for i, ax in enumerate(axes.flat): # 遍历每个子图对象
#     ax.set_xlabel("GC3s") # 设置x轴标签
#     ax.set_ylabel("ENC") # 设置y轴标签
#     ax.scatter(GC3s[i], ENC[i], color="black", s = 0.1) # 绘制第i个物种的散点图
#     ax.plot(unique_GC3s, enc_expected, linewidth=1, color='blue') # 绘制拟合曲线
#     ax.set_title(species[i], fontdict={'style': 'italic'}) # 设置子图标题为第i个物种的名称

# plt.show() # 显示所有子图
# plt.savefig("/home/ug0167/zhouyi_file/species_comparison/all_species_enc_gc3_plot.png", dpi=300, bbox_inches='tight') # 保存所有子图为一个图片文件
