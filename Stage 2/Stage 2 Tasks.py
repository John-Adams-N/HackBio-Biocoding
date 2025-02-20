# ==============================================
# Section 1: Importing & Loading Datasets
# ==============================================
# 1.1: Load the SIFT dataset from the given URL
# ==============================================

import pandas as pd

# Define dataset URLs
sift_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
foldx_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"

# Load datasets from URLs
sift_df = pd.read_csv(sift_url, sep="\t")  # SIFT dataset
foldx_df = pd.read_csv(foldx_url, sep="\t")  # FoldX dataset

# Display first few rows
print(sift_df.head())
print(foldx_df.head())

# Print column names to debug
print("SIFT DataFrame Columns:", sift_df.columns)
print("FoldX DataFrame Columns:", foldx_df.columns)

# ==============================================
# 1.2 Loading Datasets
# ==============================================

# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the datasets from the given URLs
sift_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv"
foldx_url = "https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv"

# Read the datasets using pandas
sift_df = pd.read_csv(sift_url, sep="\t")  # SIFT dataset (Functional impact)
foldx_df = pd.read_csv(foldx_url, sep="\t")  # FoldX dataset (Structural impact)

# Step 2: Inspect the data structure
print("SIFT Dataset Sample:\n", sift_df.head())
print("\nFoldX Dataset Sample:\n", foldx_df.head())

# Step 3: Create a unique identifier for merging (Protein_AminoAcid combination)
sift_df["specific_Protein_aa"] = sift_df["Protein"] + "_" + sift_df["Amino_acid"]
foldx_df["specific_Protein_aa"] = foldx_df["Protein"] + "_" + foldx_df["Amino_acid"]

# Step 4: Merge datasets on the specific_Protein_aa column
merged_df = pd.merge(sift_df, foldx_df, on="specific_Protein_aa", suffixes=("_sift", "_foldx"))

# Step 5: Filter for mutations that impact both function and structure
deleterious_mutations = merged_df[
    (merged_df["SIFT_score"] < 0.05) & (merged_df["FoldX_score"] > 2)
]

print("\nDeleterious Mutations (Affect Both Structure & Function):\n", deleterious_mutations.head())

# Step 6: Extract the original amino acid from the mutation notation
# Example: If "E63D", extract "E" (original amino acid)
deleterious_mutations["Original_Amino"] = deleterious_mutations["Amino_acid"].str[0]

# Step 7: Generate a frequency table of high-impact amino acids
amino_acid_counts = deleterious_mutations["Original_Amino"].value_counts()
print("\nFrequency Table of High-Impact Amino Acids:\n", amino_acid_counts)

# Step 8: Visualization
# Bar plot
plt.figure(figsize=(10, 5))
amino_acid_counts.plot(kind="bar", color="royalblue", edgecolor="black")
plt.xlabel("Amino Acid")
plt.ylabel("Frequency")
plt.title("High-Impact Amino Acids (Structure & Function)")
plt.xticks(rotation=0)
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
amino_acid_counts.plot(kind="pie", autopct="%1.1f%%", colors=plt.cm.Paired.colors)
plt.ylabel("")  # Hide y-label
plt.title("Distribution of High-Impact Amino Acids")
plt.show()
