# 🧬 HackBio-Biocoding Internship

## Table of Contents 🚀

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the HackBio-Biocoding repository! This repository contains a collection of scripts and resources used during the bioinformatics internship program. The program is divided into different stages, each focusing on a specific aspect of bioinformatics.

## 📜 Project Structure

The repository is organized as follows:

HackBio-Biocoding:
## 🥼 Stage 0: Biodata submission
Contains emails, short description and LinkedIn handles

## 🧫 Stage 1: DNA to Protein translation & Population growth curve generation and analysis
The process of DNA to protein translation is a crucial step in gene expression, where the genetic information stored in DNA is converted into functional proteins. This process begins with transcription, where DNA is transcribed into messenger RNA (mRNA). The mRNA then undergoes translation in the ribosome, where transfer RNA (tRNA) molecules bring specific amino acids corresponding to the three-letter codons on the mRNA. Each amino acid is represented by a three-letter abbreviation and a full name, such as Met (Methionine), Gly (Glycine), Leu (Leucine), and Phe (Phenylalanine). The amino acids are linked together in a polypeptide chain, which then folds into a functional protein.

In biological systems, growth often follows the logistic growth curve, an S-shaped (sigmoidal) model that describes population expansion under resource-limited conditions. It consists of three main phases: the lag phase (slow initial growth as cells adapt), the exponential phase (rapid division due to abundant resources), and the stationary phase (growth slows as resources become scarce, reaching the carrying capacity). This model is widely applied in cell culture studies, microbial growth analysis, and ecological population dynamics.

Together, the study of DNA to protein translation and logistic growth models enhances our understanding of molecular biology, genetics, and population behavior, providing fundamental insights for fields like biotechnology, medicine, and evolutionary studies.

## 🧪 Stage 2: (a) Amino acid Mutation analysis
This project aimed to analyze the effects of amino acid mutations on protein structure and function, focusing on stability, functionality, and potential disease associations. The analysis began with dataset processing, where mutation data from SIFT and FoldX was loaded, cleaned, and checked for consistency. SIFT scores were used to predict whether a mutation was tolerated or damaging, while FoldX energy changes (ΔΔG) helped assess the impact of mutations on protein structural stability.

The findings revealed that certain amino acids had a higher impact on protein stability, particularly those with more than 100 occurrences, which were often structurally conserved and functionally significant. To enhance interpretation, various visualizations were generated, effectively illustrating mutation distributions and the correlation between mutation frequency and structural importance.

Overall, this analysis provided valuable insights into how mutations influence protein behavior, which is essential for predicting disease-associated mutations, understanding drug resistance mechanisms, and advancing protein engineering. The results can be applied in biomedical research and therapeutic design to identify and potentially mitigate mutations that significantly alter protein function.

##  💊 (b) Pharmacokinetics RNA Seq Data Analysis
This project focused on analyzing RNA-seq data to investigate the effects of Compound X on gene expression in a diseased cell line. The dataset contained log2 fold change (Log2FC) values representing differential expression levels between untreated and treated cells, along with statistical significance indicators (p-values and adjusted p-values).

The analysis began with data preprocessing, ensuring proper formatting and consistency. A volcano plot was generated to visualize significant gene expression changes, highlighting both upregulated (Log2FC > 1, p-value < 0.01) and downregulated (Log2FC < -1, p-value < 0.01) genes. Further filtering identified key differentially expressed genes, which were categorized and saved for interpretation.

Additionally, alternative visualizations such as density plots and bar plots provided deeper insights into expression patterns. The biological functions of the top five upregulated and downregulated genes were explored using GeneCards, helping to understand the molecular pathways affected by Compound X.

This study offers crucial insights into the pharmacological effects of Compound X, aiding in the identification of potential therapeutic targets and mechanisms of action, which could be useful for drug development and precision medicine applications.

## 🎗 Stage 3: Unsupervised Machine Learning for Breast Cancer Classification and Subtype Discovery Using PCA and K-Means Clustering
Breast cancer is a leading cause of mortality worldwide, necessitating improved diagnostic techniques to classify and analyze tumor subtypes. This project explores unsupervised machine learning methods, specifically Principal Component Analysis (PCA), K-Means clustering, and Hierarchical Clustering, to classify breast cancer cases into benign and malignant categories while identifying potential subclasses within each group.

The dataset undergoes preprocessing, including standardization, missing value imputation, and dimensionality reduction via PCA, to enhance clustering accuracy. The Elbow Method is applied to determine the optimal number of clusters for K-Means, while silhouette scores and Davies-Bouldin indices evaluate cluster quality. Additionally, hierarchical clustering and dendrogram analysis further reveal fine-grained tumor subtypes.

Findings indicate that the dataset effectively separates into two primary clusters, corresponding to benign and malignant tumors. Moreover, subclasses exist within each category, suggesting further biological or pathological distinctions that warrant deeper investigation. These insights can contribute to personalized treatment strategies by highlighting tumor heterogeneity.

Finally, the project integrates logistic regression for supervised classification, evaluating model performance using accuracy, precision, recall, and F1 scores. The feature importance analysis provides insights into the most influential biomarkers for classification.

This study underscores the potential of machine learning in cancer diagnostics, demonstrating how unsupervised clustering can aid in tumor classification and subtype discovery, paving the way for more targeted and effective treatment approaches.

## Installation

To run the scripts in this repository, you need to have Python installed on your machine. You can download and install Python from [python.org](https://www.python.org/).

You may also need to install some additional Python packages. You can install the required packages using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Each stage contains a set of scripts that perform specific bioinformatics tasks. To run a script, navigate to the appropriate stage directory and execute the script using Python. For example:

```bash
cd Stage1
python Script1.py
```

## Contributing

We welcome contributions to this project! If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact 📧

If you have any questions or suggestions, feel free to contact me at johnadams9644@gmail.com

---

Thank you for your interest in the HackBio-Biocoding project!
```
