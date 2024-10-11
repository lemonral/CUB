# 导入需要的模块
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
"/home/ug0167/zhouyi/codon_bias/enc_value/Vitis_vinifera_longest_orthologues_enc_ratio_results.xlsx",
"/home/ug0167/zhouyi/codon_bias/enc_value/Cycas_panzhihuaensis_longest_orthologues_enc_ratio_results.xlsx",

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
"/home/ug0167/zhouyi/codon_bias/enc_value/Vitis_vinifera_longest_orthologues_enc_ratio_results.xlsx":"Vitis vinifera",
"/home/ug0167/zhouyi/codon_bias/enc_value/Cycas_panzhihuaensis_longest_orthologues_enc_ratio_results.xlsx":"Cycas panzhihuaensis",

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
#     "/home/ug0167/zhouyi_file/species_enc/delicio_cds_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_eriantha_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_hemsleyana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_rufa_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_zhejiangensis_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Rhododendron_simsii_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Coffea_arabica_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_arabidopsis_thaliana_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Vitis_vinifera_cds_enc_ratio_results.xlsx",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx"
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
#     "/home/ug0167/zhouyi_file/species_enc/hongyang4_CDS_filter_enc_ratio_results.xlsx":"Actinidia chinensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx":"Cycas panzhihuaensis",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Actinidia_arguta_cds_enc_ratio_results.xlsx":"Actinidia arguta",
#     "/home/ug0167/zhouyi_file/species_enc/filtered_Cycas_panzhihuaensis_genome_cds_enc_ratio_results.xlsx":"Cycas panzhihuaensis"

# }

# 创建一个空的数据框，用于存储所有物种的gc3s值
all_species_df = pd.DataFrame()

# 遍历每个物种的Excel文件，读取gc3s值，并将其追加到all_species_df中
for excel_file in species_files:
    # 读取Excel文件中的数据，假设第一列是基因ID，第二列是gc3s
    df = pd.read_excel(excel_file)
    # 获取物种的名称，假设文件名的第一个单词是物种的名称，例如"speciesA.xlsx"中的"speciesA"
    species = species_names[excel_file]
    # 获取gc3s的值，转换为numpy数组
    gc3s = df["GC3s"].to_numpy()
    # 创建一个新的数据框，用于存储物种的名称和gc3s值
    new_df = pd.DataFrame({"Species": species, "gc3s": gc3s})
    # 将新的数据框追加到all_species_df中
    all_species_df = all_species_df._append(new_df)

# 设置绘图风格
sns.set_style("whitegrid")
sns.set_context("paper")
# 创建一个小提琴图，显示不同物种的gc3s值的分布
sns.violinplot(x="Species", y="gc3s", data=all_species_df, #inner="quartile",  
               # 显示四分位数
    palette="pastel"  # 设置配色
    )
plt.xticks(rotation=45, ha="right",fontsize=8)
# 添加标题和坐标轴标签
#plt.title("GC3s values for different species")
plt.xlabel("")
plt.ylabel("GC3s")
# 显示图形
plt.show()
plt.savefig('/home/ug0167/zhouyi/codon_bias/gc3s_violin_plot/gc3s_violin_new_result_plot.png', dpi=300, bbox_inches='tight')
print("Picture has been saved")