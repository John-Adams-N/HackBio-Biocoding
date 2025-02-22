# Stage-1: HackBio Biocoding Internship

Task Description
The goal of Stage-1 was to complete the assigned bioinformatics task, implement the solution in a script, and upload the results to the repository.

Steps Completed:

Implemented the solution in Stage 1 Implementation.py using Python.
Processed and analyzed the provided dataset.
Generated the required output files.
Uploaded the solution files to the stage-one folder.
Updated the README to document the process.

Files Included:
Stage 1 Implementation.py – Contains the implementation of the solution.
README.md – Documents the task and workflow.

Section 1: DNA to Protein Translation

This section of the code translates a given DNA sequence into a protein sequence using the standard genetic code.

Steps:

Define the Genetic Code: The dictionary CODON_TABLE maps each codon (three-letter DNA sequence) to its corresponding amino acid.

Define the Translation Function:

Convert the DNA sequence to uppercase.

Split it into codons (three-letter segments).

Translate each codon to its corresponding amino acid using CODON_TABLE.

Stop translation when encountering a stop codon (TAA, TAG, or TGA).

Example Usage:

A sample DNA sequence is translated into a protein sequence and printed.

Section 2: Logistic Population Growth

This section simulates logistic growth with randomized lag and exponential phases.

Steps:

Define the Logistic Growth Function:

Randomize lag and exponential phases using a normal distribution.

Initialize population and simulate growth using the logistic equation.

The function returns a list of time points and population sizes.

Example Usage:

Growth parameters are defined (carrying capacity K, initial population P0, growth rate r, etc.).

The logistic growth function is called, and the results are printed as a time vs. population table.

Section 3: Generate Multiple Growth Curves

This section generates 100 different logistic growth curves with varying lag and exponential phases.

Steps:

Define a Function to Generate Growth Curves:

Calls logistic_growth multiple times and stores results in a Pandas DataFrame.

Determine Time to 80% of Carrying Capacity:

Iterates through each growth curve and finds the time when population reaches 80% of K.

Plot Growth Curves:

Generates a line plot showing the growth curves.

Creates a histogram showing the distribution of times to reach 80% of carrying capacity.

Section 4: Calculating the Hamming Distance

This section calculates the Hamming distance between two strings, which measures the number of differing characters at each position.

Steps:

Define the Hamming Distance Function:

Pad the shorter string to match the length of the longer one.

Count positions where characters differ.

Example Usage:

Computes the Hamming distance between a Slack username and a LinkedIn handle.

Github Repository

The full implementation is available on GitHub:
HackBio-Biocoding Repository.
