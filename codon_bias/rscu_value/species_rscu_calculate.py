from Bio import SeqIO
import Bio
import pandas as pd
import re
import collections
from collections import Counter  # Import Counter

codon_table = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "**",
    "TGT": "C", "TGC": "C", "TGA": "***", "TGG": "W",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}

def get_synonymous_codons(amino_acid):
    """
    根据氨基酸获取同义密码子。

    :param amino_acid: 氨基酸。
    :return: 同义密码子。
    """

    synonymous_codons = []
    for codon, amino_acid_in_codon in codon_table.items():
        if amino_acid_in_codon == amino_acid:
            synonymous_codons.append(codon)
    return synonymous_codons
    

def get_amino_acid_from_codon(codon):
    """
    根据密码子获取氨基酸。

    :param codon: 密码子。
    :return: 氨基酸。
    """

    

    if codon in codon_table:
        return codon_table[codon]
    return None


def calculate_rscu_from_fasta(fasta_file):
    """
    利用基因组序列计算同义密码子的 rscu 值。

    :param fasta_file: FASTA 文件。
    :return: 包含同义密码子、密码子数量、氨基酸和 rscu 值的 DataFrame。
    """

    # 读取 FASTA 文件。
    sequences = SeqIO.parse(fasta_file, "fasta")
    genome = ''.join([str(record.seq) for record in sequences])  

    # 提取所有密码子。
    codons = re.findall(r"[ATGC]{3}", genome)
    print("Extracted Codons (first 10):", codons[:10]) # 仅打印前10个密码子 
    codon_counts = Counter(codons)
    # 将所有密码子按氨基酸进行分组。
    codon_groups = collections.defaultdict(list)
    for codon in codons:
        amino_acid = get_amino_acid_from_codon(codon)
        codon_groups[amino_acid].append(codon)
    print("Codon Groups for first amino acid (first 3 rows):", codon_groups[next(iter(codon_groups))][:3])
    # 计算每个氨基酸的同义密码子使用频率。
    codon_frequencies = {}
    for amino_acid, codons in codon_groups.items():
        codon_frequencies[amino_acid] = len(codons)
    print(f"Amino acid: {amino_acid}, Frequency: {codon_frequencies}")
    # 计算每个氨基酸的同义密码子 RSCU 值。
    rSCU_values = {}
    for codon in codon_table:
        amino_acid = get_amino_acid_from_codon(codon)
        synonymous_codons = get_synonymous_codons(amino_acid)
        print(synonymous_codons)
        if synonymous_codons:  # 检查列表是否为空
            expected_frequency = 1 / len(synonymous_codons)
            print(expected_frequency) 
            codon_count = codon_counts[codon]
            print(codon_count)
            amino_count = codon_frequencies[amino_acid]
            print(amino_count)
            rSCU_values[codon] =  codon_count / amino_count / expected_frequency
            print("列表不为空")  # 不会执行
        else:
            # 处理没有同义密码子的情况
            rSCU_values[codon] = None  # 或者设置为其他值
            print("列表为空")  # 不会执行

    # 创建包含同义密码子、密码子数量、氨基酸和 rscu 值的 DataFrame。
    df = pd.DataFrame({
        "codon": list(rSCU_values.keys()),
        "Amino Acid": [get_amino_acid_from_codon(codon) for codon in rSCU_values.keys()],
        "Codon Count": [codon_counts[codon] for codon in rSCU_values.keys()],
        "RSCU Value": list(rSCU_values.values())
    })

    return df



# def calculate_rscu_for_multiple_species(fasta_files):
#     """
#     计算多个物种的同义密码子 rscu 值，并将结果保存到不同的 Excel 文件。

#     :param fasta_files: 包含多个 FASTA 文件路径的列表。
#     """

#     for fasta_file in fasta_files:
#         result_df = calculate_rscu_from_fasta(fasta_file)

#         # 将结果保存到 Excel 文件
#         output_excel_path = f"/home/ug0167/zhouyi_file/species_rscu/{fasta_file.split('/')[-1]}_rscu_results.xlsx"
#         result_df.to_excel(output_excel_path, index=False)
#         print(f"rSCU results have been saved to {output_excel_path}")

# 多个物种的 FASTA 文件列表
fasta_files = [
    "/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_deliciosa_longest_orthologues.fasta",
        "/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_arguta_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_chinensis_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_eriantha_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_hemsleyana_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_rufa_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Actinidia_zhejiangensis_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Arabidopsis_thaliana_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Coffea_arabica_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Cycas_panzhihuaensis_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Rhododendron_simsii_longest_orthologues.fasta",
"/home/ug0167/zhouyi/codon_bias/longest_orthologues/Vitis_vinifera_longest_orthologues.fasta"
    # "/home/ug0167/zhouyi/delicio/delicio_cds_filter.fasta",
    # "/home/ug0167/zhouyi/hongyang4/hongyang4_CDS_filter.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_eriantha_cds.fasta",  # 替换为你的输入 fasta 文件路径1
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_hemsleyana_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_rufa_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_zhejiangensis_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Rhododendron_simsii_cds.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Coffea_arabica_cds.fna",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_arabidopsis_thaliana_cds.fna",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Vitis_vinifera_cds.fa",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_napus.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_oleracea.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_rapa.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_oleracea_Brassica_rapa.fasta",  
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_arguta_cds.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Cycas_panzhihuaensis_genome_cds.fasta" 
    ]

for fasta_file in fasta_files:
    result_df = calculate_rscu_from_fasta(fasta_file)
    output_excel_path = f"/home/ug0167/zhouyi/codon_bias/rscu_value/{fasta_file.split('/')[-1].split('.')[0]}_rscu_results.xlsx"
    result_df.to_excel(output_excel_path, index=False)
    print(f"rscu results have been saved to {output_excel_path}")


       

    