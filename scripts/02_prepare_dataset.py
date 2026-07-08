"""
=========================================================
02_prepare_dataset.py

Préparation du jeu de données pour les analyses
=========================================================
"""

import pandas as pd
from pathlib import Path

# -----------------------------
# Définition des dossiers
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = BASE_DIR / "results"

# -----------------------------
# Lecture du fichier nettoyé
# -----------------------------
input_file = RESULTS_DIR / "CYP2D6_clean.csv"

print("Lecture du fichier nettoyé...")

df = pd.read_csv(input_file)

# -----------------------------
# Sélection des colonnes utiles
# -----------------------------
cyp2d6 = df[[
    "Allele",
    "Activity",
    "Clinical_Status",
    "Findings",
    "PMID"
]].copy()

print("Colonnes conservées :")
print(cyp2d6.columns)

print("\nAperçu des données :")
print(cyp2d6.head())

# -----------------------------
# Sauvegarde
# -----------------------------
output_file = RESULTS_DIR / "prepared_dataset.csv"

cyp2d6.to_csv(output_file, index=False)

print("\nJeu de données préparé enregistré.")
