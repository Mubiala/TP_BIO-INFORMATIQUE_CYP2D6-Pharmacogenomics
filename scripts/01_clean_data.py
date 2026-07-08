"""
=========================================================
01_clean_data.py

Bioinformatics Project
CYP2D6 Pharmacogenomics Pipeline

EXCEL -> NETTOYAGE -> CSV
=========================================================
"""

import pandas as pd
from pathlib import Path


# -------------------------------------------------------
# Définition des dossiers
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
RESULTS_DIR = BASE_DIR / "results"

RESULTS_DIR.mkdir(exist_ok=True)


# -------------------------------------------------------
# Lecture du fichier Excel
# -------------------------------------------------------

excel_file = DATA_DIR / "CYP2D6_allele_functionality_reference.xlsx"

print("Lecture du fichier Excel...")

df = pd.read_excel(excel_file)

print("Nombre de lignes :", len(df))
print("Nombre de colonnes :", len(df.columns))


# -------------------------------------------------------
# Renommage des colonnes
# -------------------------------------------------------

df.columns = [
    "Allele",
    "Activity",
    "Functional_Status",
    "Clinical_Status",
    "Substrate",
    "PMID",
    "Evidence",
    "Findings",
    "Comments"
]

print("Colonnes renommées.")


# -------------------------------------------------------
# Sauvegarde
# -------------------------------------------------------

output_file = RESULTS_DIR / "CYP2D6_clean.csv"

df.to_csv(output_file, index=False)

print("Fichier enregistré dans :", output_file)

print("Nettoyage terminé.")
