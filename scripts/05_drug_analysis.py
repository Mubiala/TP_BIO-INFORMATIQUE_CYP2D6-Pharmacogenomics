"""
=========================================================
05_drug_analysis.py

Analyse des médicaments associés aux variants CYP2D6
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import re
from pathlib import Path
from collections import Counter

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

print("===== Analyse des médicaments =====")

# -------------------------------------------------------
# Extraction des médicaments
# -------------------------------------------------------

drug_counter = Counter()

for text in df["Findings"].dropna():

    # Découpage des différentes références
    parts = text.split(";")

    for part in parts:

        # On récupère le texte après le :
        if ":" in part:
            drug = part.split(":")[1]

            # Suppression de "(in vivo)" et "(in vitro)"
            drug = re.sub(r"\(.*?\)", "", drug)

            # Nettoyage
            drug = drug.strip().lower()

            # On ne garde pas les textes trop longs
            if len(drug) < 40 and len(drug) > 2:

                drug_counter[drug] += 1

# -------------------------------------------------------
# Top 10 médicaments
# -------------------------------------------------------

top10 = drug_counter.most_common(10)

drug_df = pd.DataFrame(
    top10,
    columns=["Medication", "Frequency"]
)

print(drug_df)

# -------------------------------------------------------
# Sauvegarde
# -------------------------------------------------------

drug_df.to_csv(
    RESULTS_DIR / "drug_frequency.csv",
    index=False
)

# -------------------------------------------------------
# Graphique
# -------------------------------------------------------

plt.figure(figsize=(9,5))

plt.bar(drug_df["Medication"], drug_df["Frequency"])

plt.xticks(rotation=45, ha="right")

plt.title("Top 10 des médicaments étudiés")

plt.xlabel("Médicaments")

plt.ylabel("Fréquence")

plt.tight_layout()

plt.savefig(
    FIGURES_DIR / "drug_frequency.png",
    dpi=300
)

print("\nAnalyse des médicaments terminée.")
