## CYP2D6 Pharmacogenomics Analysis Pipeline

## Project Overview

This project was developed as part of a Bioinformatics practical assignment.

The objective is to analyze CYP2D6 genetic variants using pharmacogenomic data from PharmGKB and interpret their clinical impact on drug metabolism.

---

## Objectives

- Import and clean CYP2D6 allele data
- Analyze clinical functions of CYP2D6 variants
- Predict metabolizer phenotypes
- Identify the most frequently studied drugs
- Generate therapeutic recommendations
- Organize the analysis into a reproducible Nextflow pipeline

---

## Dataset

Source:

PharmGKB

Dataset:

CYP2D6_allele_functionality_reference.xlsx

---

## Technologies

- Python 3
- Pandas
- Matplotlib
- Nextflow
- Git
- GitHub
- Google Colab

---

## Project Structure

```
.
├── data/
├── notebooks/
├── scripts/
├── figures/
├── results/
├── main.nf
├── nextflow.config
└── README.md
```

---

## Workflow

```
Raw Excel Data
        │
        ▼
01_clean_data.py
        │
        ▼
02_prepare_dataset.py
        │
        ▼
03_variant_analysis.py
        │
        ▼
04_phenotype_analysis.py
        │
        ▼
05_drug_analysis.py
        │
        ▼
06_recommendations.py
```

---

## Main Results

The pipeline produces:

- Clean dataset
- Variant statistics
- Phenotype distribution
- Drug frequency analysis
- Therapeutic recommendations
- Publication-quality figures

---

## Author

Samuel Mubiala

Master 2 – Computer Science

Bioinformatics Practical Work

2026 TP_BIO-INFORMATIQUE_CYP2D6-Pharmacogenomics
Mini bioinformatics pipeline for CYP2D6 pharmacogenomic variant interpretation using Python and Nextflow
