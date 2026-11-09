---
name: cheminformatics-drug-discovery
description: >
  Use for computational chemistry and early drug discovery data analysis:
  SMILES standardization, RDKit workflows, ChEMBL or PubChem bioactivity
  curation, descriptors, fingerprints, similarity, scaffold-aware data splits,
  QSAR models, ADMET-style property prediction, docking interpretation, and
  hit triage. Not for synthesis of hazardous or harmful compounds.
license: CC-BY-4.0
---

# Cheminformatics and Drug Discovery

## Workflow

1. Define the objective (target activity, property prediction, library triage, SAR analysis) and the assay type and units. Bioactivity values from different assays are not interchangeable.
2. Standardize structures: parse and sanitize SMILES, handle salts and mixtures, neutralize charges where appropriate, treat tautomers and stereochemistry consistently, and remove duplicates. Log structures that fail parsing instead of silently dropping them.
3. Curate bioactivity data: restrict to comparable assay types, convert units, record measurement relation (such as ">" values), resolve conflicting replicates, and flag assay artifacts and promiscuous or reactive chemotypes (for example PAINS-type alerts) as warnings, not proof.
4. Compute descriptors and fingerprints appropriate to the model, and report the version of the toolkit.
5. Split data so evaluation reflects the intended use: random splits overestimate performance for new chemotypes, so use scaffold or time-aware splits, and keep near-duplicates out of the test set.
6. Train baseline models first, quantify uncertainty and applicability domain, use proper metrics for imbalanced data, and compare to simple baselines. Report variance across seeds or folds.
7. Treat docking scores as rough ranking signals that depend on the protein preparation and scoring function. They do not measure affinity, and require validation with experimental data or controls such as known actives and decoys.
8. Property and ADMET predictions are screening aids. State training-domain limits, and recommend experimental confirmation.
9. Safety boundary: do not provide routes, optimization, or design guidance aimed at toxic agents, chemical weapons, or controlled substances. Decline and offer safe, defensive or regulatory-oriented help instead.

## Deliverable

Cleaned dataset with provenance, curation rules, split strategy, model metrics with uncertainty, applicability domain, and limitations. Do not claim efficacy, safety, or clinical relevance from computed scores.
