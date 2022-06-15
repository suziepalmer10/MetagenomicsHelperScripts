import pandas as pd
import sys

"""
Used to read in calculate relative abundances from qiime2. 
Suzette Palmer
06-15-2023

#To use: python relative_abundance.py <path to level-5.csv> <output file path/name>
#Example path: "/home2/s180020/Desktop/Gut_BSI_16S_Data/OutputFile_noclinda7/level-5.csv"

Example command: python relative_abundance.py /home2/s180020/Desktop/Gut_BSI_16S_Data/OutputFile_noclinda7/level-5.csv /home2/s180020/Desktop/outfile.csv
read in level-5.csv file from https://view.qiime2.org/

"""

#this should be taken from the barplot.qzv output
#Path = sys.argv[0]
df = pd.DataFrame(pd.read_csv(str(sys.argv[1]), header =0, index_col='index'))
#transpose df and remove group name
df_T = df.T
df_T = df_T[:-1]
#calculate relative abundance
df2 = pd.DataFrame(df_T/df_T.sum(axis=0))
#export to csv
df2.to_csv(str(sys.argv[2]))
print("Success! Check your output file.")






