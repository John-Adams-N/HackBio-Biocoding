# ==============================================
# Section 2: Data Preprocessing
# ==============================================

# ==============================================
# 2.1: Load and Debug Dataset
# ==============================================

# Importing required libraries
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.impute import SimpleImputer

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(script_dir, "cancer_transcriptomics_cleaned.csv")

print(f"🔍 Looking for file at: {csv_filename}")

def load_and_debug_dataset(filename):
    try:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"❌ Error: '{filename}' not found. Please check the file path.")

        # Load dataset
        df = pd.read_csv(filename)
        print(f"✅ Dataset successfully loaded from: {filename}")
        print(f"📊 Dataset Shape: {df.shape[0]} rows, {df.shape[1]} columns")

        # Inspect first few rows
        print("\n🔍 Raw Data Sample (First 5 rows):")
        print(df.head())

        # Standardize column names
        df.columns = df.columns.str.strip().str.lower()
        
        # Drop 'id' column if it exists (since it's not useful for ML)
        if 'id' in df.columns:
            df = df.drop(columns=['id'])
        
        # Convert numeric columns (excluding diagnosis) to proper types
        numeric_cols = df.columns.difference(['diagnosis'])
        df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
        
        # Display dataset info after conversion
        print("\n📌 Dataset Info After Processing:")
        print(df.info())

        return df

    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return None
    except pd.errors.EmptyDataError:
        print("❌ Error: The file is empty. Please provide a valid dataset.")
        return None
    except pd.errors.ParserError:
        print("❌ Error: The file could not be parsed. Please check the file format.")
        return None
    except Exception as e:
        print(f"❌ An error occurred while processing the dataset: {e}")
        return None

# Run the debugging function
df = load_and_debug_dataset(csv_filename)

# 1. Data Preprocessing
X = df.drop('diagnosis', axis=1) # Features
y = df['diagnosis'] # Target

# Encode 'diagnosis' as numerical (0 = benign, 1 = malignant)
y = y.map({'B': 0, 'M': 1})

# Handle missing values
imputer = SimpleImputer(strategy='mean')
X = imputer.fit_transform(X)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ==============================================
# 2.2: Apply PCA
# ==============================================

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Variance explained by each component
print("\n🔍 PCA Explained Variance:", pca.explained_variance_ratio_)

# ==============================================
# 2.3: Visualize PCA Result
# ==============================================

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization of Cancer Data')
plt.colorbar(label='Diagnosis (0=Benign, 1=Malignant)')
plt.show()

# ==============================================
# 2.4: Apply K-means Clustering
# ==============================================

kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X_pca)
labels = kmeans.labels_

# ==============================================
# 2.5: Visualize Clustering Result
# ==============================================

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('K-Means Clustering of Cancer Data (PCA Reduced)')
plt.colorbar(label='Cluster Label')
plt.show()

# ==============================================
# 2.6: Data Splitting
# ==============================================

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# ==============================================
# 2.7: Model Selection and Training
# ==============================================

model = LogisticRegression()
model.fit(X_train, y_train)

# ==============================================
# 2.8: Model Evaluation
# ==============================================

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")
