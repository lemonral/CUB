from Bio import SeqIO
from Bio.SeqUtils import CodonAdaptationIndex
from openpyxl import Workbook

# Function to calculate GC content
def calculate_gc_content(seq):
    gc_count = seq.count("G") + seq.count("C")
    return gc_count / len(seq) if len(seq) > 0 else 0

# Function to calculate GC content for each codon position
def calculate_gc1_gc2_gc3(seq):
    gc1 = calculate_gc_content(seq[::3])
    gc2 = calculate_gc_content(seq[1::3])
    gc3 = calculate_gc_content(seq[2::3])
    return gc1, gc2, gc3

# Function to calculate G3/(G3+C3) and A3/(A3+T3) ratios
def calculate_ratios(seq):
    g3_count = seq[2::3].count("G")
    c3_count = seq[2::3].count("C")
    a3_count = seq[2::3].count("A")
    t3_count = seq[2::3].count("T")

    g3_ratio = g3_count / (g3_count + c3_count)
    a3_ratio = a3_count / (a3_count + t3_count)
    return g3_ratio, a3_ratio

# Function to validate sequences for valid codons
def validate_sequence(seq):
    valid_bases = {'A', 'T', 'G', 'C'}
    seq = seq.upper()
    return all(seq[i:i+3] in valid_bases for i in range(0, len(seq), 3))

def calculate_g3s(seq):
    # 定义需要排除的密码子集合
    excluded_codons = {"ATG", "TGG", "TAA", "TAG", "TGA"}
    
    # 计算排除了Met、Trp和终止密码子后的GC3s频率
    codon_count = 0
    g3_count = 0
    
    # 遍历序列，并计算GC3s的数量和总密码子数量
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon not in excluded_codons:
            codon_count += 1
            if codon[2] in {"G"}:
                g3_count += 1
    
    # 计算GC3s频率
    g3s = g3_count / codon_count if codon_count > 0 else 0
    return g3s

def calculate_c3s(seq):
    # 定义需要排除的密码子集合
    excluded_codons = {"ATG", "TGG", "TAA", "TAG", "TGA"}
    
    # 计算排除了Met、Trp和终止密码子后的GC3s频率
    codon_count = 0
    c3_count = 0
    
    # 遍历序列，并计算GC3s的数量和总密码子数量
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon not in excluded_codons:
            codon_count += 1
            if codon[2] in {"C"}:
                c3_count += 1
    
    # 计算GC3s频率
    c3s = c3_count / codon_count if codon_count > 0 else 0
    return c3s

def calculate_a3s(seq):
    # 定义需要排除的密码子集合
    excluded_codons = {"ATG", "TGG", "TAA", "TAG", "TGA"}
    
    # 计算排除了Met、Trp和终止密码子后的GC3s频率
    codon_count = 0
    a3_count = 0
    
    # 遍历序列，并计算GC3s的数量和总密码子数量
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon not in excluded_codons:
            codon_count += 1
            if codon[2] in {"A"}:
                a3_count += 1
    
    # 计算GC3s频率
    a3s = a3_count / codon_count if codon_count > 0 else 0
    return a3s

def calculate_t3s(seq):
    # 定义需要排除的密码子集合
    excluded_codons = {"ATG", "TGG", "TAA", "TAG", "TGA"}
    
    # 计算排除了Met、Trp和终止密码子后的GC3s频率
    codon_count = 0
    t3_count = 0
    
    # 遍历序列，并计算GC3s的数量和总密码子数量
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon not in excluded_codons:
            codon_count += 1
            if codon[2] in {"T"}:
                t3_count += 1
    
    # 计算GC3s频率
    t3s = t3_count / codon_count if codon_count > 0 else 0
    return t3s

def calculate_gc3s(seq):
    # 定义需要排除的密码子集合
    excluded_codons = {"ATG", "TGG", "TAA", "TAG", "TGA"}
    
    # 计算排除了Met、Trp和终止密码子后的GC3s频率
    codon_count = 0
    gc3_count = 0
    
    # 遍历序列，并计算GC3s的数量和总密码子数量
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon not in excluded_codons:
            codon_count += 1
            if codon[2] in {"G", "C"}:
                gc3_count += 1
    
    # 计算GC3s频率
    gc3s = gc3_count / codon_count if codon_count > 0 else 0
    return gc3s

def process_fasta_file(input_file):
# Read FASTA file and store sequences
    sequences = []
    for record in SeqIO.parse(input_file, "fasta"):
        sequences.append(str(record.seq))

    # Create an Excel workbook
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(["Gene ID", "GC1", "GC2", "GC3", "GC12", "G3/(G3+C3)", "A3/(A3+T3)", "A3s", "T3s", "C3s", "G3s", "GC3s", "GC"])

    # Calculate parameters for each sequence
    for record in SeqIO.parse(input_file, "fasta"):
        gene_id = record.id
        sequence = str(record.seq)

        gc1, gc2, gc3 = calculate_gc1_gc2_gc3(sequence)
        gc12 = (gc1 + gc2) / 2
        g3_c3_ratio, a3_t3_ratio = calculate_ratios(sequence)
        a3s = calculate_a3s(sequence)
        t3s = calculate_t3s(sequence)
        c3s = calculate_c3s(sequence)
        g3s = calculate_g3s(sequence)
        gc3s = calculate_gc3s(sequence)
        gc = (gc1 + gc2 + gc3) / 3


        sheet.append([gene_id, gc1, gc2, gc3, gc12, g3_c3_ratio, a3_t3_ratio, a3s, t3s, c3s, g3s, gc3s, gc])

    output_file = f"/home/ug0167/zhouyi/codon_bias/species_gene_parameter/{input_file.split('/')[-1].split('.')[0]}_gene_parameters.xlsx"
    workbook.save(output_file)
    print(f"Gene parameters for {input_file} have been calculated and saved to {output_file}.")

# 处理多个FASTA文件
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
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_eriantha_cds.fasta",  # 替换为你的输入 fasta 文件路径1
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_hemsleyana_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_rufa_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_zhejiangensis_cds.fasta", 
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_arabidopsis_thaliana_cds.fna",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Coffea_arabica_cds.fna",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Rhododendron_simsii_cds.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Vitis_vinifera_cds.fa", 
    # "/home/ug0167/zhouyi/hongyang4/hongyang4_CDS_filter.fasta",
    # "/home/ug0167/zhouyi/delicio/delicio_cds_filter.fasta",# 替换为你的输入 fasta 文件路径2
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_napus.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_oleracea_Brassica_rapa.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_oleracea.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Brassica_rapa.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Actinidia_arguta_cds.fasta",
    # "/home/ug0167/zhouyi_file/spcies_filterd_genome/filtered_Cycas_panzhihuaensis_genome_cds.fasta"
    ]

for fasta_file in fasta_files:
    process_fasta_file(fasta_file)