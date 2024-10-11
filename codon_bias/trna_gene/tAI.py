import pandas as pd
import numpy as np

# 读取Excel文件
file_path = '/home/ug0167/zhouyi/codon_bias/trna_gene/trna_number.xlsx'
sheets = pd.ExcelFile(file_path).sheet_names

def calculate_ws(tRNA_counts, s_values=None, sking=1):
    if s_values is None:
        s_values = [0.0, 0.0, 0.0, 0.0, 0.41, 0.28, 0.9999, 0.68, 0.89]
    
    p = 1 - np.array(s_values)
    W = []
    
    for i in range(0, 61, 4):
        W.append(p[0] * tRNA_counts[i] + p[4] * tRNA_counts[i + 1])
        W.append(p[1] * tRNA_counts[i + 1] + p[5] * tRNA_counts[i])
        W.append(p[2] * tRNA_counts[i + 2] + p[6] * tRNA_counts[i])
        W.append(p[3] * tRNA_counts[i + 3] + p[7] * tRNA_counts[i + 2])
    
    W[36] = p[3] * tRNA_counts[36]
    
    if sking == 1:
        W[35] = p[8]
    
    W = np.array(W)
    W = np.delete(W, [11, 12, 15, 36])
    
    w = W / max(W)
    
    if np.any(w == 0):
        gm = np.exp(np.mean(np.log(w[w != 0])))
        w[w == 0] = gm
    
    return w

# 初始化一个空DataFrame来存储过滤后的数据
filtered_data = pd.DataFrame()
df_codon = pd.DataFrame()
# 循环遍历每个sheet并过滤数据
for sheet in sheets:
    print(sheet)
    df = pd.read_excel(file_path, sheet_name=sheet)
    df_filtered = df[(df['Anti_Codon'] != 'NNN') & (df['Note'] != 'pseudo')]
    filtered_data = pd.concat([filtered_data, df_filtered], ignore_index=True)
    # 计算每种反密码子的数量
    anticodon_counts = filtered_data['Anti_Codon'].value_counts().to_dict()
    df1 = pd.DataFrame(list(anticodon_counts.items()), columns=['Anti_Codon', 'counts'])
    
    # 给dataframe添加一列，存放物种名称
    df1["species"] = sheet
    
    # 把dataframe追加到df中
    df_codon = df_codon._append(df1)

df1 = df_codon.pivot(index="species", columns="Anti_Codon", values="counts")
df1.to_excel('/home/ug0167/zhouyi/codon_bias/trna_gene/anti_codon_counts.xlsx')

# 创建反密码子到密码子的映射关系
anticodon_to_codons = {
    'AAA': ['TTT'], 'GAA': ['TTT','TTC'], 'TAA': ['TTG','TTA'], 'CAA': ['TTG'],
    'AGA': ['TCT','TCC','TCA'], 'GGA': ['TCT','TCC'], 'TGA': ['TCA','TCG'], 'CGA': ['TCG'],
    'ATA': ['TAT'], 'GTA': ['TAT','TAC'], 'TTA': ['TAA'], 'CTA': ['TAG'],
    'ACA': ['TGT'], 'GCA': ['TGT','TGC'], 'CCA': ['TGG'],
    'AAG': ['CTT','CTC','CTA'], 'GAG': ['CTT','CTC','CTA'], 'TAG': ['CTA','CTG'], 'CAG': ['CTG'],
    'AGG': ['CCT','CCC','CCA'], 'GGG': ['CCT','CCC'], 'TGG': ['CCA','CCG'], 'CGG': ['CCG'],
    'ATG': ['CAT'], 'GTG': ['CAT','CAC'], 'TTG': ['CAA','CAG'], 'CTG': ['CAG'],
    'ACG':['CGT','CGC','CGA'],'GCG':['CGT','CGC'],'TCG':['CGA','CGG'],'CCG':['CGG'],
    'AAT':['ATT','ATC','ATA'],'GAT':['ATT','ATC','ATA'],'TAT':['ATA'],'CAT':['ATG'],
    'AGT': ['ACT','ACC','ACA'], 'GGT': ['ACT','ACC'], 'TGT': ['ACA','ACG'], 'CGT': ['ACG'],
    'ATT': ['AAT'], 'GTT': ['AAT','AAC'], 'TTT': ['AAA','AAG'], 'CTT': ['AAG'],
    'ACT':['AGT'],'GCT':['AGT','AGC'],'TCT':['AGA','AGG'],'CCT':['AGG'],
    'AAC': ['GTT','GTC','GTA'], 'GAC': ['GTT','GTC'], 'TAC': ['GTA','GTG'], 'CAC': ['GTG'],
    'AGC': ['GCT','GCC','GCA'], 'GGC': ['GCT','GCC'], 'TGC': ['GCA','GCG'], 'CGC': ['GCG'],
    'ATC':['GAT'],'GTC':['GAT','GAC'],'TTC':['GAA','GAG'],'CTC':['GAG'],
    'ACC':['GGT','GGC','GGA'],'GCC':['GGT','GGC'],'TCC':['GGA','GGG'],'CCC':['GGG']
}


for species, row in df.iterrows():
    print(species,row)
    codon_counts = {}
    for anticodon, count in row.items():
        if pd.notna(count):
            codons = anticodon_to_codons[anticodon]
            for codon in codons:
                if codon in codon_counts:
                    codon_counts[codon] += count
                else:
                    codon_counts[codon] = count

# 将反密码子转换为密码子并计算密码子的数量
codon_counts = {}
for anticodon, count in anticodon_counts.items():
    codons = anticodon_to_codons(anticodon)
    for codon in codons:
        if codon in codon_counts:
            codon_counts[codon] += count
        else:
            codon_counts[codon] = count
    codon_order = [
    "TTT", "TTC", "TTA", "TTG", "TCT", "TCC", "TCA", "TCG",
    "TAT", "TAC", "TAA","TAG","TGT", "TGC","TGA","TGG", "CTT", "CTC", "CTA",
    "CTG", "CCT", "CCC", "CCA", "CCG", "CAT", "CAC", "CAA",
    "CAG", "CGT", "CGC", "CGA", "CGG", "ATT", "ATC", "ATA",
    "ATG", "ACT", "ACC", "ACA", "ACG", "AAT", "AAC", "AAA",
    "AAG", "AGT", "AGC", "AGA", "AGG", "GTT", "GTC", "GTA",
    "GTG", "GCT", "GCC", "GCA", "GCG", "GAT", "GAC", "GAA",
    "GAG", "GGT", "GGC", "GGA", "GGG"]
    sorted_codon_counts = {codon: codon_counts.get(codon, 0) for codon in codon_order}
    # 计算相对适应性值
    ws = calculate_ws(sorted_codon_counts)
    print(ws)
