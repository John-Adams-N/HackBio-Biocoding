import os
import pandas as pd
import logging
from io import StringIO

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_and_debug_dataset(filename, target_col='diagnosis', drop_id=True, encoding='utf-8'):
    """
    Loads, cleans, and debugs a CSV dataset with advanced checks.
    """
    try:
        logging.info(f"Loading dataset from: {filename}")
        if not os.path.exists(filename):
            raise FileNotFoundError(f"❌ Error: '{filename}' not found. Please check the file path.")

        df = pd.read_csv(filename, encoding=encoding)
        logging.info(f"Dataset successfully loaded. Shape: {df.shape}")

        df.columns = df.columns.str.strip().str.lower()

        if drop_id and 'id' in df.columns:
            df = df.drop(columns=['id'])
            logging.info("Dropped 'id' column.")

        numeric_cols = df.columns.difference([target_col])
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

        # Basic Data Validation
        logging.info("Starting data validation.")
        logging.info(f"Duplicate rows: {df.duplicated().sum()}")
        logging.info(f"Null values per column:\n{df.isnull().sum()}")

        # Outlier Detection (Example using IQR)
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
            if not outliers.empty:
                logging.warning(f"Outliers found in column '{col}': {len(outliers)}")

        # Null Handling (Example: Impute with median)
        for col in numeric_cols:
            if df[col].isnull().any():
                median_val = df[col].median()
                df[col].fillna(median_val, inplace=True)
                logging.info(f"Null values in '{col}' imputed with median ({median_val}).")

        # Data Type Consistency Checks
        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(df[col]):
                logging.error(f"Column '{col}' is not numeric after conversion.")

        # Range Checks (Example: Assuming radius_mean should be within a certain range)
        if 'radius_mean' in df.columns:
            min_radius = 0
            max_radius = 100 # Adjust as needed
            invalid_radii = df[(df['radius_mean'] < min_radius) | (df['radius_mean'] > max_radius)]
            if not invalid_radii.empty:
                logging.warning(f"Invalid 'radius_mean' values found: {len(invalid_radii)}")

        logging.info("Data validation and cleaning completed.")
        
        # Capture DataFrame info as a string and log it
        buffer = StringIO()
        df.info(buf=buffer)
        info_str = buffer.getvalue()
        logging.info(info_str)

        return df

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)
        return None

# Example usage:
csv_filename = "cancer_transcriptomics_cleaned.csv"
df = load_and_debug_dataset(csv_filename)