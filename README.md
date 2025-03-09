# HackBio-Biocoding Internship🧬

This repository contains scripts for a Bioinformatics internship program organized in different stages.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Welcome to the HackBio-Biocoding repository! This repository contains a collection of scripts and resources used during the bioinformatics internship program. The program is divided into different stages, each focusing on a specific aspect of bioinformatics.

## Project Structure

The repository is organized as follows:

HackBio-Biocoding:
## Stage 0: Biodata submission

## Stage 1: DNA to Protein translation & Population growth curve generation and analysis
Summary of Stage 1
DNA to Protein Translation
Logistic Growth Model
Multiple Growth Curve Generation
Finding Time to Reach 80% of Carrying Capacity
Example Usage for demonstration

## Stage 2: (a) Amino acid Mutation analysis
Step 1: Data Importation
Load both datasets: SIFT Dataset and FoldX Dataset into a data processing environment (e.g., Python using Pandas).
Step 2: Data Cleaning & Preparation
Identify relevant columns in both datasets (Protein, Amino_acid, SIFT Score, FoldX Score).
Create a new column, specific_Protein_aa, in both datasets.
This column should be a concatenation of Protein and Amino_acid (e.g., "A5A607_E63D").
Ensure the new column has a consistent format (no trailing spaces, missing values, or inconsistent capitalization).
Step 3: Data Merging
Merge the two datasets using the specific_Protein_aa column as a key.
The resulting dataset should contain:
Protein, Amino_acid, SIFT Score, FoldX Score, and specific_Protein_aa.
Step 4: Identify Deleterious Mutations
Filter for mutations that:
Have a SIFT Score below 0.05 (Functionally deleterious).
Have a FoldX Score above 2 kCal/mol (Structurally destabilizing).
Store this filtered dataset separately for further analysis.
Step 5: Investigate Amino Acid Impact
Extract the first amino acid from the Amino_acid column (e.g., from "E63D", extract "E").
Count how frequently each amino acid appears in the deleterious mutations.
Identify the amino acid with the most occurrences.
Step 6: Generate Frequency Analysis
Create a frequency table for all amino acids based on their impact.
Summarize the total occurrences for each amino acid.
Step 7: Data Visualization
Use the frequency table to generate:
A bar plot showing the frequency of each amino acid.
A pie chart visualizing the distribution of amino acid impacts.   
##          (b) Pharmacokinetics RNA Seq Data Analysis
Summary of Transcriptomics Analysis
1. Introduction
The dataset contains data from an RNA-seq experiment between a diseased cell line and diseased cell lines treated with compound X.
Objective: Analyze RNA-seq gene expression data to assess the impact of Compound X on diseased cell lines.
Dataset: Includes gene expression data (log2FoldChange, p-value, and adjusted p-value (padj)).
3. Data Processing & Cleaning
Data Import: Fetched dataset from an online source and converted it from TXT to CSV for better readability.
Loading & Inspection: Checked the dataset structure, missing values, and column names.
Key Findings:
No missing values were detected.
The dataset contained 4 columns: Gene, log2FoldChange, p-value, and padj.
4. Differential Gene Expression Analysis 
Upregulated Genes: Genes with log2FoldChange > 1 and p-value < 0.01.
Downregulated Genes: Genes with log2FoldChange < -1 and p-value < 0.01.
Key Findings:
Identified several significantly upregulated and downregulated genes.
Saved these genes to separate CSV files for further exploration.
5. Visualization & Interpretation
Volcano Plot: Showed significantly upregulated and downregulated genes.
Bar Plot: Compared gene expression changes.
Density Plot: Visualized the distribution of log2FoldChange values.
6. Biological Insights & Next Steps
Top genes (e.g., DOK6, TBX5, SLC32A1, IFITM1) were analyzed using GeneCards for their biological roles.
Insights from this analysis could inform potential therapeutic targets and further research directions.
🚀 Conclusion: Successfully processed, analyzed, and visualized transcriptomics data, revealing key genes affected by Compound X!

## Stage 3: Machine Learning for Cancer type classification

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

## Contact

If you have any questions or suggestions, feel free to contact us at johnadams9644@gmail.com

---

Thank you for your interest in the HackBio-Biocoding project!
```

