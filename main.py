import pandas as pd
import numpy as np

# read in the data from an Excel file
df = pd.read_excel('model_data.xlsx')

# get a list of all the genotypes in the dataset
# change 'GENOTYPE' to match your column which has genotypes name
genotypes = df['GENOTYPE'].unique()

# get a list of all the characters in the dataset
# this removes the GENOTYPE and REPLICATION column and get the remaining columns
characters = df.columns[2:]

# storing the result in an empty list
results = []

# loop through each genotype and character and calculate the mean across the 3 replications
for genotype in genotypes:
    for character in characters:
        selected_rows = df[df['GENOTYPE'] == genotype]
        mean_df = selected_rows.groupby('REPLICATION').agg({character: np.mean})
        overall_mean = round(mean_df[character].mean(),2)
        results.append((genotype, character, overall_mean))

# convert the results to a DataFrame and write to a new Excel file
results_df = pd.DataFrame(results, columns=['GENOTYPE', 'CHARACTER', 'MEAN'])
results_pivot = results_df.pivot(index='GENOTYPE', columns='CHARACTER', values='MEAN')

# write to a new Excel file
results_pivot.to_excel('mean_genotype_data.xlsx')

#results_df.to_excel('merged_data.xlsx', index=False)
