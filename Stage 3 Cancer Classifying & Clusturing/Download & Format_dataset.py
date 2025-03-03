# ==============================================
# Section 1: Downloading & Cleaning Datasets
# ==============================================

# ==============================================
# 1.1: Downloading dataset from URL
# ==============================================

import os
import io
import requests
import pandas as pd

def download_dataset(url, filename="cancer_transcriptomics.csv"):
    """
    Downloads a dataset from a given URL and saves it as a CSV file
    in the current working directory.

    Parameters:
        url (str): The dataset URL.
        filename (str): Name of the file to save the dataset as.
    
    Returns:
        str: The full path of the saved dataset.
    """
    try:
        # Get the script's current directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        # Download the dataset
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for failed downloads

        # Read the dataset into a Pandas DataFrame
        data = pd.read_csv(io.StringIO(response.text), delim_whitespace=True)

        # Save DataFrame as CSV
        data.to_csv(file_path, index=False)

        print(f"Dataset successfully saved to: {file_path}")
        return file_path

    except requests.exceptions.RequestException as e:
        print(f"Error downloading dataset: {e}")
    except Exception as e:
        print(f"Error processing dataset: {e}")

# Example usage
dataset_url = "https://raw.githubusercontent.com/PacktPublishing/Machine-Learning-in-Biotechnology-and-Life-Sciences/refs/heads/main/datasets/dataset_wisc_sd.csv"
download_dataset(dataset_url, "cancer_transcriptomics.csv")

# ==============================================
# 1.2: Cleaning & Formating Dataset
# ==============================================

import os
import pandas as pd

# Get the script's directory and construct the CSV path
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "cancer_transcriptomics.csv")
cleaned_csv_filename = os.path.join(script_dir, "cancer_transcriptomics_cleaned.csv")

def clean_dataset(filename, output_filename):
    """Fix dataset formatting issues and save a cleaned version."""
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"❌ Error: '{filename}' not found. Please check the file path.")

        # Read file as raw text to process formatting issues
        with open(filename, "r") as f:
            lines = f.readlines()

        # Step 1: Clean header
        header = lines[0].strip().replace('"', '')  # Remove quotes
        header_columns = header.split(",")

        # Step 2: Read first data row to get actual column count
        first_data_row = lines[1].strip().replace('"', '').rstrip(",")
        first_data_columns = first_data_row.split(",")

        actual_col_count = len(first_data_columns)

        if len(header_columns) != actual_col_count:
            print(f"⚠️ Header has {len(header_columns)} columns, but first data row has {actual_col_count} columns.")
            print("🔄 Adjusting header to match actual column count.")

            if len(header_columns) > actual_col_count:
                header_columns = header_columns[:actual_col_count]  # Trim extra columns
            else:
                header_columns += [f"extra_col_{i}" for i in range(actual_col_count - len(header_columns))]  # Add missing columns

        # Step 3: Clean data rows and ensure alignment
        cleaned_rows = []
        for line in lines[1:]:
            cleaned_line = line.strip().replace('"', '')  # Remove quotes
            cleaned_line = cleaned_line.rstrip(",")  # Remove trailing commas
            row_data = cleaned_line.split(",")

            if len(row_data) > actual_col_count:
                row_data = row_data[:actual_col_count]  # Trim extra columns
            elif len(row_data) < actual_col_count:
                row_data += [""] * (actual_col_count - len(row_data))  # Fill missing values

            cleaned_rows.append(row_data)

        # Step 4: Create DataFrame
        df = pd.DataFrame(cleaned_rows, columns=header_columns)

        # Step 5: Drop completely empty columns (if any)
        df = df.dropna(axis=1, how="all")

        # Step 6: Rename duplicate columns
        seen = {}
        new_columns = []
        for col in df.columns:
            if col in seen:
                seen[col] += 1
                new_columns.append(f"{col}_{seen[col]}")  # Append suffix to duplicates
            else:
                seen[col] = 0
                new_columns.append(col)
        df.columns = new_columns

        # Step 7: Save cleaned dataset
        df.to_csv(output_filename, index=False)

        print(f"✅ Cleaned dataset saved to: {output_filename}")
        print(f"📊 New dataset shape: {df.shape[0]} rows, {df.shape[1]} columns")

        return df

    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"❌ An error occurred while cleaning the dataset: {e}")
        return None

# Run the cleaning function
df_cleaned = clean_dataset(csv_filename, cleaned_csv_filename)