# 加载所需的库
library(tidyverse)
library(stats)
library(contrast)
library(dplyr)
library(readxl)
library(openxlsx)
library(MASS)

# 定义物种文件和名称的映射
species_files <- c(
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
  "/home/ug0167/zhouyi/codon_bias/enc_value/Cycas_panzhihuaensis_longest_orthologues_enc_ratio_results.xlsx"

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
)

species_names <- c(
  "Actinidia deliciosa",
  "Actinidia chinensis",
  "Actinidia arguta",
  "Actinidia eriantha",
  "Actinidia hemsleyana",
  "Actinidia rufa",
  "Actinidia zhejiangensis",
  "Rhododendron simsii",
  "Coffea arabica",
  "Arabidopsis thaliana",
  "Vitis vinifera",
  "Cycas panzhihuaensis"
)

# 读取所有物种的gc3s值并合并到一个数据框中
comp <- lapply(species_files, function(file) {
  df <- read_excel(file)
  species <- species_names[which(species_files == file)]
  data.frame(Species = species, GC3s = df$GC3s)
}) %>%
  bind_rows()

attach(comp)
names(comp)
Species <- factor(Species)
levels(Species)
# mat <- matrix(c(0, 1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                             -1,-1,6,-1,-1,-1,-1,0,0,0,0,0,
#                             -1,-1,-1,-1,-1,-1,-1,0,0,0,7,0,
#                             -1,-1,-1,-1,-1,-1,-1,8,0,0,-1,0,
#                             -1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,10,
#                             -1,-1,-1,-1,-1,-1,-1,-1,-1,11,-1,-1,
#                             5,-1,0,-1,-1,-1,-1,0,0,0,0,0
# 
#                                                         ),
#                                                       nrow = 7, ncol = 12, byrow = TRUE)
# print(mat)
# custom_contrast_matrix <- t(mat)
# print(custom_contrast_matrix)
# # Create custom contrasts object
# custom_contrasts <- custom_contrast_matrix
# # Use the custom contrasts object in the model
# model <- lm(GC3s ~ Species, data = comp, contrasts = list(Species = custom_contrasts))
# summary(model)
# summary_output <- summary(model)
# # 将模型摘要转换为字符向量
# summary_text <- capture.output(summary_output)
# # 转换为数据框
# df1 <- data.frame(Output = summary_text)
# write.xlsx(df1, file = "/home/ug0167/zhouyi_file/anova/gc3s_contrast_model.xlsx")
# # 转换为数据框
# # 进行单因素方差分析
# aov_model <- aov(GC3s ~ Species, data = comp)
# # 
# # 查看单因素方差分析结果
# aov_summary <- summary(aov_model)
# # 捕获输出到字符向量
# output <- capture.output(aov_summary)
# 
# # 转换为数据框
# df <- data.frame(Output = output)
# 
# # 将数据保存到Excel文件中
# write.xlsx(df, file = "/home/ug0167/zhouyi_file/anova/gc3s_aov_model.xlsx")

data1 <- subset(comp, Species == "Actinidia chinensis")
data2 <- subset(comp, Species == "Actinidia deliciosa")
data3 <- subset(comp, Species == "Actinidia arguta")
data4 <- subset(comp, Species == "Actinidia eriantha")
data5 <- subset(comp, Species == "Actinidia hemsleyana")
data6 <- subset(comp, Species == "Actinidia rufa")
data7 <- subset(comp, Species == "Actinidia zhejiangensis")
data8 <- subset(comp, Species == "Rhododendron simsii")
data9 <- subset(comp, Species == "Coffea arabica")
data10 <- subset(comp, Species == "Arabidopsis thaliana")
data11 <- subset(comp, Species == "Vitis vinifera")
data12 <- subset(comp, Species == "Cycas panzhihuaensis")

# 从数据框中提取GC3s列
gc3s_data1 <- data1$GC3s
gc3s_data2 <- data2$GC3s
gc3s_data3 <- data3$GC3s
gc3s_data4 <- data4$GC3s
gc3s_data5 <- data5$GC3s
gc3s_data6 <- data6$GC3s
gc3s_data7 <- data7$GC3s
gc3s_data8 <- data8$GC3s
gc3s_data9 <- data9$GC3s
gc3s_data10 <- data10$GC3s
gc3s_data11 <- data11$GC3s
gc3s_data12 <- data12$GC3s
combined_data1 <- rbind(gc3s_data1,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7)
combined_data2 <- rbind(gc3s_data1,gc3s_data3,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7)
combined_data3 <- rbind(gc3s_data1,gc3s_data2,gc3s_data3,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7)
combined_data4 <- rbind(gc3s_data1,gc3s_data2,gc3s_data3,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7,gc3s_data8)
combined_data5 <- rbind(gc3s_data1,gc3s_data2,gc3s_data3,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7,gc3s_data8,gc3s_data9,gc3s_data10)
combined_data6 <- rbind(gc3s_data1,gc3s_data2,gc3s_data3,gc3s_data4, gc3s_data5, gc3s_data6,gc3s_data7,gc3s_data8,gc3s_data9,gc3s_data10,gc3s_data11)
# 进行独立样本t检验
# t_test_result <- t.test(gc3s_data1, gc3s_data2)
wilcox_test_result1 <- wilcox.test(gc3s_data1, gc3s_data2, exact = TRUE)
wilcox_test_result2<- wilcox.test(gc3s_data3, combined_data1, exact = TRUE)
wilcox_test_result3 <- wilcox.test(gc3s_data2, combined_data2, exact = TRUE)
wilcox_test_result4 <- wilcox.test(gc3s_data8, combined_data3, exact = TRUE)
wilcox_test_result5 <- wilcox.test(gc3s_data10, combined_data4, exact = TRUE)
wilcox_test_result6 <- wilcox.test(gc3s_data11, combined_data5, exact = TRUE)
wilcox_test_result7 <- wilcox.test(gc3s_data12, combined_data6, exact = TRUE)
# Store results in a data frame
results_df <- data.frame(
  Test_ID = 1:7,
  Comparison = c("Actinidia chinensis vs Actinidia deliciosa",
                 "Actinidia arguta vs Combined Group 1",
                 "Actinidia deliciosa vs Combined Group 2",
                 "Rhododendron simsii vs Combined Group 3",
                 "Arabidopsis thaliana vs Combined Group 4",
                 "Vitis vinifera vs Combined Group 5",
                 "Cycas panzhihuaensis vs Combined Group 6"),
  P_Value = c(wilcox_test_result1$p.value,
              wilcox_test_result2$p.value,
              wilcox_test_result3$p.value,
              wilcox_test_result4$p.value,
              wilcox_test_result5$p.value,
              wilcox_test_result6$p.value,
              wilcox_test_result7$p.value)
)

# Optionally, add more columns if necessary, e.g., test statistics, method used
print(results_df)
write.xlsx(results_df, file = "/home/ug0167/zhouyi/codon_bias/significance_test/gc3s_u_tests.xlsx")

# 
# # 进行contrast检验，比较不同物种之间的差异
# # 这里以Actinidia deliciosa为参考组，比较其他物种与Actinidia deliciosa之间的差异
# print(species_names)
# contrast_matrix <- contr.sum(length(species_names))
# 
# # contrast_matrix <- matrix(c(-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, # Actinidia deliciosa vs Actinidia chinensis
#                           #   0, -1, 1, 0, 0, 0, 0, 0, 0, 0, # Actinidia eriantha vs Actinidia hemsleyana
#                           #   0, 0, -1, 1, 0, 0, 0, 0, 0, 0, # Actinidia rufa vs Actinidia zhejiangensis
#                           #   0, 0, 0, -1, 1, 0, 0, 0, 0, 0, # Rhododendron simsii vs Coffea arabica
#                           #   0, 0, 0, 0, -1, 1, 0, 0, 0, 0,
#                           #   0, 0, 0, 0, 0, -1, 1, 0, 0, 0,
#                           #   0, 0, 0, 0, 0, 0, -1, 1, 0, 0,
#                           #   0, 0, 0, 0, 0, 0, 0, -1, 1, 0,
#                           #   0, 0, 0, 0, 0, 0, 0, 0, -1, 1
#                           #   ), 
#                           # nrow = 10, ncol = 9, byrow = TRUE)
# print(contrast_matrix)
# 
# 
# # 逆转矩阵的行
# # reversed_matrix <- rev(contrast_matrix)
# 
# # 打印逆转后的矩阵
# # print("逆转后的矩阵：")
# # print(reversed_matrix)
# contrast_results <- contrast(aov_model, contrast_matrix)
# 
# colnames(contrast_results) <- paste0("vs_", species_names[1])
# all_species_df1 <- cbind(all_species_df, contrast_results)
# 
# # 查看contrast检验结果
# all_species_df1
