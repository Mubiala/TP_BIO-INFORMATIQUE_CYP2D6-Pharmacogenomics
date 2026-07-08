"""
=========================================================
06_recommendations.py

Génération des recommandations thérapeutiques
à partir des phénotypes CYP2D6
=========================================================
"""

import pandas as pd
from pathlib import Path

# -------------------------------------------------------
# Définition des dossiers
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = BASE_DIR / "results"

# -------------------------------------------------------
# Tableau des recommandations
# -------------------------------------------------------

recommendations = pd.DataFrame({

    "Phenotype":[
        "Poor Metabolizer",
        "Intermediate Metabolizer",
        "Normal Metabolizer",
        "Ultrarapid Metabolizer"
    ],

    "Example_Diplotype":[
        "*4/*4",
        "*1/*4",
        "*1/*1",
        "*1x2/*2"
    ],

    "Medication":[
        "Codeine",
        "Tramadol",
        "Tamoxifen",
        "Codeine"
    ],

    "Clinical_Interpretation":[
        "Very low CYP2D6 activity",
        "Reduced CYP2D6 activity",
        "Normal CYP2D6 activity",
        "Very high CYP2D6 activity"
    ],

    "Recommendation":[
        "Avoid codeine; use an alternative analgesic.",
        "Monitor efficacy; dose adjustment may be necessary.",
        "Use the standard recommended dose.",
        "Avoid codeine because of toxicity risk."
    ]

})

# -------------------------------------------------------
# Sauvegarde
# -------------------------------------------------------

output_file = RESULTS_DIR / "therapeutic_recommendations.csv"

recommendations.to_csv(output_file, index=False)

print("===== Recommandations thérapeutiques =====")
print(recommendations)

print("\nTableau enregistré dans :")
print(output_file)
