# 导入需要的模块
import pandas as pd
import numpy as np

# 定义一个函数，根据enc_ratio值的区间，计算每个区间的频率
def calculate_frequency(enc_ratio, bins_array):
    # bins_array是一个列表，表示enc_ratio值的分组区间，例如[-0.15, -0.05, 0.05, 0.15, 0.25, 0.35]
    # 创建一个空的字典，用于存储每个区间的频率
    frequency_dict = {}
    # 遍历bins_array中的每个区间
    for i in range(len(bins_array) - 1):
        # 获取区间的左右端点
        left = bins_array[i]
        right = bins_array[i + 1]
        # 计算enc_ratio中落在该区间的值的个数
        count = np.sum((enc_ratio > left) & (enc_ratio <= right))
        # 计算该区间的频率，即个数除以总数
        frequency = count / len(enc_ratio)
        # 将区间和频率存入字典中，以字符串的形式表示区间
        frequency_dict[f"{left}~{right}"] = frequency
    # 返回字典
    return frequency_dict

# 定义一个函数，读取Excel文件中的数据，计算每个物种的enc_ratio值和频率分布，并返回一个数据框
def read_species_data(excel_file, bins_array):
    # excel_file是一个字符串，表示Excel文件的路径，例如"speciesA.xlsx"
    # bins_array是一个列表，表示enc_ratio值的分组区间，例如[-0.15, -0.05, 0.05, 0.15, 0.25, 0.35]
    # 读取Excel文件中的数据，假设第一列是基因ID，第二列是GC3s，第三列是ENC_Expected
    df = pd.read_excel(excel_file)
    # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
    species = species_names[excel_file]
    # 获取ENC_Expected的值，转换为numpy数组
    enc_ratio = df['enc_ratio'].to_numpy()
    # 计算每个区间的频率
    frequency_dict = calculate_frequency(enc_ratio, bins_array)
    # 创建一个新的数据框，用于存储物种的名称和每个区间的频率
    new_df = pd.DataFrame({"Species": species, **frequency_dict}, index=[0])
    # 返回数据框
    print(new_df)
    return new_df

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

# # 定义一个列表，存储不同物种的Excel文件的路径
# species_files = [
#     "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx"
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_napus_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_Brassica_rapa_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_enc_ratio_results.xlsx",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_rapa_enc_ratio_results.xlsx"
# ]

# species_names = {"/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx":"Actinidia deliciosa",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx":"Actinidia eriantha",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx":"Actinidia arguta",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx":"Actinidia hemsleyana",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx": "Actinidia rufa",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx": "Actinidia zhejiangensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx": "Arabidopsis thaliana",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx": "Coffea arabica",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx": "Rhododendron simsii",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx":"Vitis vinifera",
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx":"Actinidia chinensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx":"Cycas panzhihuaensis"
    
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_napus_enc_ratio_results.xlsx":"Brassica napus",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_Brassica_rapa_enc_ratio_results.xlsx":"Brassica napus (merged)",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_oleracea_enc_ratio_results.xlsx":"Brassica oleracea",
#     # "/home/ug0167/zhouyi_file/species_enc/filtered_Brassica_rapa_enc_ratio_results.xlsx":"Brassica rapa"
#     }
# 定义一个列表，存储enc_ratio值的分组区间
bins_array = [
    # -0.25,
              -0.15, -0.05, 0.05, 0.15, 0.25,0.35
              ,0.45
              ,0.55
            # ,0.65,0.75,0.85,0.95
              ]

# 创建一个空的数据框，用于存储所有物种的数据
all_species_df = pd.DataFrame()

# 遍历每个物种的Excel文件，调用read_species_data函数读取数据，并将数据框追加到all_species_df中
for excel_file in species_files:
    species_df = read_species_data(excel_file, bins_array)
    all_species_df = all_species_df._append(species_df)
print(all_species_df)
# 保存all_species_df到一个新的Excel文件中，文件名为"all_species_frequency.xlsx"
all_species_df.to_excel("/home/ug0167/zhouyi/codon_bias/enc_value_distribution/species_orthologs_enc_ratio_frequency.xlsx", index=False)
# 打印提示信息
print(f"All species data have been processed and saved to all_species_enc_ratio_frequency.xlsx.")
