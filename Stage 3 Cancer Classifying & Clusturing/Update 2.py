# ==============================================
# Section 2: Data Preprocessing
# ==============================================
# 2.1: Load and Debug Dataset
# ==============================================
# Importing required libraries
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score, precision_score, recall_score, silhouette_score, davies_bouldin_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from scipy.cluster.hierarchy import dendrogram, linkage

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

# ==============================================
# 2.2 Data Preprocessing
# ==============================================
# Drop rows with missing target values
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
# Section 3: Data Analysis and Model Building
# ==============================================
# 3.1 Apply PCA for Dimensionality Reduction
# ==============================================
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Variance explained by each component
print("\n🔍 PCA Explained Variance:", pca.explained_variance_ratio_)

# ==============================================
# 3.2 Visualize PCA Result
# ==============================================
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='coolwarm', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization of Cancer Data')
plt.colorbar(label='Diagnosis (0=Benign, 1=Malignant)')
plt.show()

# ==============================================
# Section 4: Clustering and Classification
# ==============================================
# 4.1 Apply K-Means Clustering
# ==============================================
# Determine optimal K using Elbow Method
wcss = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS (Within-cluster Sum of Squares)')
plt.title('Elbow Method for Optimal K')
plt.show()

#  ==============================================
# 4.2 Apply K-means with optimal K (assuming 2 based on domain knowledge)
# ==============================================
kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X_scaled)

# ==============================================
# 4.3 Visualize Clustering Result
# ==============================================
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=clusters, cmap='viridis', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('K-Means Clustering on PCA-Reduced Data')
plt.colorbar(label='Cluster')
plt.show()

# ==============================================
# Section 5: Train-Test Split, 
# Model Training, & Evaluation
# ==============================================
# 5: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 5.1: Model Selection and Training
model = LogisticRegression()
model.fit(X_train, y_train)

# 5.2: Model Evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1:.4f}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(classification_report(y_test, y_pred))

# ==============================================
# Section 6: Detecting Subclasses
# ==============================================
# Separate benign and malignant cases
benign_data = X_scaled[y == 0]
malignant_data = X_scaled[y == 1]

# Function to find optimal K for subclasses
def find_optimal_k(data, title):
    wcss = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(data)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(8, 6))
    plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
    plt.xlabel('Number of Clusters (K)')
    plt.ylabel('WCSS')
    plt.title(f'Elbow Method for {title}')
    plt.show()

# Determine optimal clusters for benign and malignant
find_optimal_k(benign_data, 'Benign Subclasses')
find_optimal_k(malignant_data, 'Malignant Subclasses')

# Apply K-means to find subclasses
optimal_k_benign = 2  # Adjust based on elbow method
optimal_k_malignant = 2  # Adjust based on elbow method

kmeans_benign = KMeans(n_clusters=optimal_k_benign, random_state=42, n_init=10)
kmeans_malignant = KMeans(n_clusters=optimal_k_malignant, random_state=42, n_init=10)

benign_clusters = kmeans_benign.fit_predict(benign_data)
malignant_clusters = kmeans_malignant.fit_predict(malignant_data)

# Visualize subclass distributions
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[y == 0, 0], X_pca[y == 0, 1], c=benign_clusters, cmap='coolwarm', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Benign Subclasses')
plt.colorbar(label='Subclass')
plt.show()

plt.figure(figsize=(8, 6))
plt.scatter(X_pca[y == 1, 0], X_pca[y == 1, 1], c=malignant_clusters, cmap='viridis', alpha=0.7)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Malignant Subclasses')
plt.colorbar(label='Subclass')
plt.show()

# ==============================================
# Section 7: Additional Analysis; Feature Importance
# ==============================================
# 7.1: Feature Importance in Logistic Regression Model
feature_importance = abs(model.coef_[0])
feature_names = df.drop(columns=['diagnosis']).columns

plt.figure(figsize=(10, 6))
sns.barplot(x=feature_importance, y=feature_names, palette='coolwarm')
plt.xlabel('Feature Importance')
plt.ylabel('Feature')
plt.title('Feature Importance in Logistic Regression Model')
plt.show()

# ==============================================
# Section 8: Additional Clustering Methods and Validation
# ==============================================
# 8.1: Apply Hierarchical Clustering
hierarchical = AgglomerativeClustering(n_clusters=2)
hierarchical_labels = hierarchical.fit_predict(X_scaled)

# 8.2: Visualize Hierarchical Clustering Result
linkage_matrix = linkage(X_scaled, method='ward')
plt.figure(figsize=(10, 5))
dendrogram(linkage_matrix)
plt.title("Hierarchical Clustering Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")
plt.show()

# 8.3: Cluster Validation
silhouette_avg = silhouette_score(X_scaled, clusters)
davies_bouldin = davies_bouldin_score(X_scaled, clusters)
print(f"Silhouette Score: {silhouette_avg}")
print(f"Davies-Bouldin Index: {davies_bouldin}")

# 8.4: Analyze Hierarchical Clustering Labels
unique_hierarchical_clusters = np.unique(hierarchical_labels)
for cluster in unique_hierarchical_clusters:
    subset = X_scaled[hierarchical_labels == cluster]
    print(f"Hierarchical Cluster {cluster} size: {len(subset)}")

# 8.5: Additional Analysis - Cluster Centroids & Distribution
centroids = kmeans.cluster_centers_
print("K-Means Centroids:")
print(centroids)

# Distribution of Clusters
plt.figure(figsize=(8, 6))
sns.histplot(clusters, bins=2, kde=True)
plt.title("Distribution of K-Means Clusters")
plt.xlabel("Cluster Label")
plt.ylabel("Count")
plt.show()