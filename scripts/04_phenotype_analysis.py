"""
=========================================================
04_phenotype_analysis.py

Détermination des phénotypes métaboliques CYP2D6
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
# Lecture des données
# -------------------------------------------------------

input_file = RESULTS_DIR / "prepared_dataset.csv"

df = pd.read_csv(input_file)

print("===== Analyse des phénotypes =====")

# -------------------------------------------------------
# Fonction de conversion
# -------------------------------------------------------

def phenotype(status):

    if status == "No function":
        return "Poor Metabolizer"

    elif status == "Decreased function":
        return "Intermediate Metabolizer"

    elif status == "Normal function":
        return "Normal Metabolizer"

    elif status == "Increased function":
        return "Ultrarapid Metabolizer"

    else:
        return "Unknown"

# -------------------------------------------------------
# Création de la colonne Phenotype
# -------------------------------------------------------

df["Phenotype"] = df["Clinical_Status"].apply(phenotype)

# -------------------------------------------------------
# Comptage
# -------------------------------------------------------

phenotype_counts = df["Phenotype"].value_counts()

print("\nDistribution des phénotypes :")

print(phenotype_counts)

# -------------------------------------------------------
# Sauvegarde
# -------------------------------------------------------

phenotype_counts.to_csv(
    RESULTS_DIR / "phenotype_distribution.csv"
)

# -------------------------------------------------------
# Graphique
# -------------------------------------------------------

plt.figure(figsize=(8,5))

phenotype_counts.plot(kind="bar")

plt.title("Distribution des phénotypes CYP2D6")

plt.xlabel("Phénotype")

plt.ylabel("Nombre d'allèles")

plt.xticks(rotation=25)

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "phenotype_distribution.png",
    dpi=300
)

print("\nGraphique enregistré.")

print("\nAnalyse des phénotypes terminée.")
