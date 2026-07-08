"""
=========================================================
03_variant_analysis.py

Analyse des variants du gène CYP2D6
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------------------------------
# Définition des dossiers
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = BASE_DIR / "results"
FIGURES_DIR = BASE_DIR / "figures"

FIGURES_DIR.mkdir(exist_ok=True)

# -------------------------------------------------------
# Lecture des données préparées
# -------------------------------------------------------

input_file = RESULTS_DIR / "prepared_dataset.csv"

df = pd.read_csv(input_file)

print("===== Analyse des variants =====")

# -------------------------------------------------------
# Nombre total d'allèles
# -------------------------------------------------------

print(f"\nNombre total d'allèles : {len(df)}")

# -------------------------------------------------------
# Nombre d'allèles uniques
# -------------------------------------------------------

print(f"Nombre d'allèles uniques : {df['Allele'].nunique()}")

# -------------------------------------------------------
# Comptage des fonctions cliniques
# -------------------------------------------------------

clinical_counts = df["Clinical_Status"].value_counts()

print("\nRépartition des fonctions cliniques :")

print(clinical_counts)

# -------------------------------------------------------
# Sauvegarde des statistiques
# -------------------------------------------------------

clinical_counts.to_csv(
    RESULTS_DIR / "clinical_status_distribution.csv"
)

# -------------------------------------------------------
# Graphique
# -------------------------------------------------------

plt.figure(figsize=(8,5))

clinical_counts.plot(kind="bar")

plt.title("Distribution des fonctions cliniques")

plt.xlabel("Fonction clinique")

plt.ylabel("Nombre d'allèles")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "clinical_status_distribution.png",
    dpi=300
)

print("\nGraphique enregistré.")
print("\nAnalyse des variants terminée avec succès.")