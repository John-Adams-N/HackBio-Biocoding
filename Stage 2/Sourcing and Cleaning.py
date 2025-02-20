# ==============================================
# Section 1: Downloading & Cleaning Datasets
# ==============================================

# ==============================================
# 1.1: Downloading SIFT dataset from URL
# ==============================================

import requests
import os

"""
    Downloads a TSV file from a given URL and saves it to the specified path.

    Parameters:
        url (str): The URL of the TSV dataset.
        filename (str): The full path to save the file.
    """

def download_tsv(url, filename):
   
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(filename, "wb") as file:
            file.write(response.content)

        print(f"File saved: {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {filename}: {e}")

# Define your desktop path
desktop_path = "/Users/Admin.DESKTOP-8TK90VT/Desktop"

# Define full paths for the files
sift_file = os.path.join(desktop_path, "sift_dataset.tsv")
foldx_file = os.path.join(desktop_path, "foldx_dataset.tsv")

# Download the files to Desktop (or directory of your choice)
download_tsv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/sift.tsv", sift_file)
download_tsv("https://raw.githubusercontent.com/HackBio-Internship/public_datasets/main/R/datasets/foldX.tsv", foldx_file)

# ==============================================
"""
    Manually converted TSV files to CSV format for easier loading.
    The CSV files are named:
    - sift_dataset.csv
    - foldx_dataset.csv

    The CSV files are saved in the working directory.
"""
# ==============================================

# ==============================================
# 1.2:  Extracting & Loading Datasets from CSV Files
# Ensuring Data Consistency   
# ==============================================

import pandas as pd
import os

# Define the path to your working directory
working_dir = r"C:\Users\Admin.DESKTOP-8TK90VT\HackBio-Biocoding\Stage 2"

# Define full file paths
sift_csv = os.path.join(working_dir, "sift_dataset.csv")
foldx_csv = os.path.join(working_dir, "foldx_dataset.csv")

# Load CSV files into Pandas DataFrames
sift_df = pd.read_csv(sift_csv)
foldx_df = pd.read_csv(foldx_csv)

# Display first few rows to confirm successful loading
print("SIFT Dataset Preview:")
print(sift_df.head())

print("\nFoldX Dataset Preview:")
print(foldx_df.head())
