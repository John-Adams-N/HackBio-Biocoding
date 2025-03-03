import os
import pandas as pd

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "cancer_transcriptomics_cleaned.csv")

def load_and_process_dataset(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"❌ Error: '{filename}' not found. Please check the file path.")

        # Load dataset
        df = pd.read_csv(filename, dtype=str)  # Load everything as string initially
        print(f"✅ Dataset successfully loaded from: {filename}")
        print(f"📊 Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()

        # Convert categorical column (diagnosis) to numeric
        if 'diagnosis' in df.columns:
            df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})
            print("🔄 Converted 'diagnosis' column to numeric (M → 1, B → 0)")

        # Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.any():
            print("\n⚠️ Missing values detected, filling with column mean:")
            print(missing_values[missing_values > 0])
            df.fillna(df.mean(), inplace=True)

        # Remove duplicate rows
        duplicate_count = df.duplicated().sum()
        if duplicate_count > 0:
            print(f"\n⚠️ {duplicate_count} duplicate rows found. Removing duplicates.")
            df.drop_duplicates(inplace=True)

        # Identify columns with non-numeric data
        non_numeric_columns = []
        for col in df.columns:
            try:
                df[col] = pd.to_numeric(df[col], errors='raise')
            except ValueError:
                non_numeric_columns.append(col)

        if non_numeric_columns:
            print(f"\n⚠️ Warning: The following columns contain non-numeric values: {', '.join(non_numeric_columns)}")
            print("🔍 Inspecting first problematic values per column:")
            for col in non_numeric_columns:
                print(f"  ➡️ Column: {col}, First problematic value: {df[col].iloc[0]}")

        # Convert all valid columns to numeric
        df = df.apply(pd.to_numeric, errors='coerce')

        # Final check
        print("\n✅ Data processing complete. Ready for analysis.")

        return df

    except Exception as e:
        print(f"❌ An error occurred while processing the dataset: {e}")
        return None

# Load and process dataset
df = load_and_process_dataset(csv_filename)