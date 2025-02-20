# ==============================================
# Section 1: Importing & Loading Datasets from CSV Files
# ==============================================

# ==============================================
# 1.1: Importing Libraries & Setting Working Directory
# ==============================================

# impoting the necessary libraries
import pandas as pd
import os

# Define the path to your working directory
working_dir = r"C:\Users\Admin.DESKTOP-8TK90VT\HackBio-Biocoding\Stage 2"

# Define full file paths
sift_csv = os.path.join(working_dir, "sift_dataset.csv")
foldx_csv = os.path.join(working_dir, "foldx_dataset.csv")

# ==============================================
# 1.2: Loading Datasets and Ensuring Data Consistency
# ==============================================

# Load CSV files into Pandas DataFrames
sift_df = pd.read_csv(sift_csv)
foldx_df = pd.read_csv(foldx_csv)

# Ensure column names are correctly formatted (strip leading/trailing spaces if needed)
sift_df.columns = sift_df.columns.str.strip()
foldx_df.columns = foldx_df.columns.str.strip()

# ==============================================
# 2: Merging Datasets and Filtering Deleterious Mutations
# ==============================================

# Create 'specific_Protein_aa' column by concatenating 'Protein' and 'Amino_Acid'
sift_df["specific_Protein_aa"] = sift_df["Protein"] + "_" + sift_df["Amino_Acid"]
foldx_df["specific_Protein_aa"] = foldx_df["Protein"] + "_" + foldx_df["Amino_Acid"]

# Merge both datasets on 'specific_Protein_aa'
merged_df = pd.merge(sift_df, foldx_df, on="specific_Protein_aa", suffixes=('_sift', '_foldx'))

# Filter mutations that are deleterious in both function and structure
deleterious_mutations = merged_df[
    (merged_df["sift_Score"] < 0.05) & (merged_df["foldX_Score"] > 2)
]

# ==============================================
# 3: Analyzing Deleterious Mutations
# ==============================================

# Extract the first amino acid from the 'Amino_Acid' column
deleterious_mutations["First_AA"] = deleterious_mutations["Amino_Acid_sift"].str[0]

# Generate frequency table for amino acids
amino_freq = deleterious_mutations["First_AA"].value_counts()

# Display results
print("\nDeleterious Mutations:")
print(deleterious_mutations)

print("\nAmino Acid Frequency Table:")
print(amino_freq)

# ==============================================
# 4: Visualizing Results
# ==============================================

# Import necessary libraries for visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Assuming 'amino_acid_counts' is the frequency table from previous step
amino_acid_counts = {
    "G": 1307, "L": 739, "A": 640, "P": 470, "V": 380, "R": 227, "I": 212, 
    "Y": 172, "D": 171, "F": 169, "S": 158, "T": 126, "W": 108, "M": 87, 
    "C": 74, "N": 60, "E": 50, "H": 47, "Q": 40, "K": 24
}

# Convert dictionary to sorted lists
amino_acids = list(amino_acid_counts.keys())
counts = list(amino_acid_counts.values())

# Sort by frequency
amino_acids, counts = zip(*sorted(zip(amino_acids, counts), key=lambda x: x[1], reverse=True))

# Bar Plot
plt.figure(figsize=(12, 6))
sns.barplot(x=amino_acids, y=counts, palette="viridis")
plt.xlabel("Amino Acid", fontsize=14)
plt.ylabel("Frequency", fontsize=14)
plt.title("Frequency of Amino Acids in Deleterious Mutations", fontsize=16)
plt.xticks(rotation=45)
plt.show()

# Pie Chart
plt.figure(figsize=(10, 10))
plt.pie(counts, labels=amino_acids, autopct="%1.1f%%", colors=sns.color_palette("viridis", len(amino_acids)))
plt.title("Proportion of Amino Acids in Deleterious Mutations", fontsize=16)
plt.show()
