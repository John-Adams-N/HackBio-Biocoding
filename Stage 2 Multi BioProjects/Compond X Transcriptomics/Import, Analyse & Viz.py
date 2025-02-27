# ==============================================
# Section 1: Downloading & Cleaning Datasets
# ==============================================

# ==============================================
# 1.1: Downloading dataset from URL
# ==============================================

# Import necessary libraries
import os
import io
import requests
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Define the dataset URL
dataset_url = "https://gist.githubusercontent.com/stephenturner/806e31fce55a8b7175af/raw/1a507c4c3f9f1baaa3a69187223ff3d3050628d4/results.txt"

# Get the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "transcriptomics_data.csv")

def download_and_process_dataset(url, save_path):
    """
    Downloads the dataset from the given URL, processes it into a structured CSV format,
    and saves it to the specified path.

    Parameters:
        url (str): The dataset URL.
        save_path (str): Path to save the processed CSV file.
    """
    try:
        # Download the dataset
        response = requests.get(url)
        response.raise_for_status()  # Raise an error if download fails

        # Convert content into a DataFrame
        data = pd.read_csv(io.StringIO(response.text), delim_whitespace=True)

        # Save as CSV
        data.to_csv(save_path, index=False)

        print(f"Dataset successfully saved to: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading dataset: {e}")
    except Exception as e:
        print(f"Error processing dataset: {e}")

# Run the function
download_and_process_dataset(dataset_url, csv_filename)

# ==============================================
# 1.2:  Extracting & Loading Datasets from CSV Files
# Ensuring Data Consistency   
# ==============================================

import pandas as pd

csv_file = "transcriptomics_data.csv"
try:
    df = pd.read_csv(csv_filename)
    print("Dataset successfully loaded!")
except FileNotFoundError:
    print(f"Error: {csv_file} not found. Please check the file path.")

# Display first few rows
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Check for missing values
missing_values = df.isnull().sum()
print("\nMissing values per column:")
print(missing_values)

# Ensure column names are correctly formatted (strip leading/trailing spaces)
df.columns = df.columns.str.strip()

# Verify column names
print("\nColumn names after formatting:")
print(df.columns)

# ==============================================
# 2:  Data Preprocessing & Exploration  
# ==============================================

import matplotlib.pyplot as plt
import seaborn as sns

# Convert p-value to -log10(p-value) for visualization
df["neg_log10_pvalue"] = -np.log10(df["pvalue"])

# Define significance thresholds
upregulated = (df["log2FoldChange"] > 1) & (df["pvalue"] < 0.01)
downregulated = (df["log2FoldChange"] < -1) & (df["pvalue"] < 0.01)

# ==============================================
# 3:  Filter and Save Significant Genes   
# ==============================================

# Filter upregulated genes (Log2FC > 1 & p-value < 0.01)
upregulated_genes = df[upregulated]

# Filter downregulated genes (Log2FC < -1 & p-value < 0.01)
downregulated_genes = df[downregulated]

# Display top genes
print("\nTop 5 Upregulated Genes:\n", upregulated_genes.head())
print("\nTop 5 Downregulated Genes:\n", downregulated_genes.head())

# Save results
upregulated_genes.to_csv(os.path.join(script_dir, "upregulated_genes.csv"), index=False)
downregulated_genes.to_csv(os.path.join(script_dir, "downregulated_genes.csv"), index=False)
print("\nSignificant genes saved successfully!")

# ==============================================
# 4: Visualizing Significant Genes
# ==============================================

# 4.1: Volcano Plot with Significance Thresholds

# Assign colors based on significance
df["color"] = "gray"  # Default: Non-significant
df.loc[upregulated, "color"] = "red"   # Upregulated
df.loc[downregulated, "color"] = "blue" # Downregulated

# Create the volcano plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df["log2FoldChange"], y=df["neg_log10_pvalue"], hue=df["color"], palette={"gray": "gray", "red": "red", "blue": "blue"}, alpha=0.7)
colors = df["color"].map({"gray": "gray", "red": "red", "blue": "blue"})
plt.scatter(x=df["log2FoldChange"], y=df["neg_log10_pvalue"], c=colors, alpha=0.7)
# Add labels and title
plt.axhline(-np.log10(0.01), linestyle="dashed", color="black", alpha=0.7)  # p-value threshold line
plt.axvline(1, linestyle="dashed", color="black", alpha=0.7)   # log2FC threshold for upregulation
plt.axvline(-1, linestyle="dashed", color="black", alpha=0.7)  # log2FC threshold for downregulation
plt.xlabel("Log2 Fold Change")
plt.ylabel("-log10(p-value)")
plt.legend(["Significant (p-value < 0.01)", "Upregulated (log2FC > 1)", "Downregulated (log2FC < -1)"], loc="upper right")
plt.legend(["p-value < 0.01", "log2FC > 1", "log2FC < -1"], loc="upper right")
plt.show()

# 4.2: Bar Plot of Top 20 Upregulated and Downregulated Genes
import matplotlib.pyplot as plt
import seaborn as sns

# Select top 20 upregulated and downregulated genes
top_up = upregulated_genes.nlargest(20, "log2FoldChange")
top_down = downregulated_genes.nsmallest(20, "log2FoldChange")

# Combine and sort for better visualization
top_genes = pd.concat([top_up, top_down]).sort_values(by="log2FoldChange")

# Set figure size
plt.figure(figsize=(12, 6))

# Bar plot
sns.barplot(y=top_genes["Gene"], x=top_genes["log2FoldChange"], 
            palette=["red" if x > 0 else "blue" for x in top_genes["log2FoldChange"]])

# Labels and styling
plt.axvline(0, color="black", linestyle="--", linewidth=1)  # Reference line at 0
plt.xlabel("Log2 Fold Change", fontsize=14)
plt.ylabel("Gene", fontsize=14)
plt.title("Top 20 Upregulated and Downregulated Genes (Bar Plot)", fontsize=16)
plt.grid(axis="x", linestyle="--", alpha=0.5)

plt.show()