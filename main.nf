nextflow.enable.dsl = 2

workflow {

    cleaned = CLEAN_DATA()

    dataset = PREPARE_DATASET(cleaned)

    variants = VARIANT_ANALYSIS(dataset)

    phenotypes = PHENOTYPE_ANALYSIS(variants)

    drugs = DRUG_ANALYSIS(phenotypes)

    RECOMMENDATIONS(drugs)
}

/*
==============================
Process 1 : Nettoyage
==============================
*/

process CLEAN_DATA {

    publishDir "results"

    output:
    path "CYP2D6_clean.csv"

    script:
    """
    python scripts/01_clean_data.py
    """
}

/*
==============================
Process 2 : Préparation
==============================
*/

process PREPARE_DATASET {

    input:
    path clean

    output:
    path "prepared_dataset.csv"

    script:
    """
    python scripts/02_prepare_dataset.py
    """
}

/*
==============================
Process 3 : Analyse des variants
==============================
*/

process VARIANT_ANALYSIS {

    input:
    path dataset

    output:
    path "variant_results.csv"

    script:
    """
    python scripts/03_variant_analysis.py
    """
}

/*
==============================
Process 4 : Analyse des phénotypes
==============================
*/

process PHENOTYPE_ANALYSIS {

    input:
    path variants

    output:
    path "phenotype_results.csv"

    script:
    """
    python scripts/04_phenotype_analysis.py
    """
}

/*
==============================
Process 5 : Analyse des médicaments
==============================
*/

process DRUG_ANALYSIS {

    input:
    path phenotype

    output:
    path "drug_results.csv"

    script:
    """
    python scripts/05_drug_analysis.py
    """
}

/*
==============================
Process 6 : Recommandations
==============================
*/

process RECOMMENDATIONS {

    input:
    path drugs

    output:
    path "therapeutic_recommendations.csv"

    script:
    """
    python scripts/06_recommendations.py
    """
}