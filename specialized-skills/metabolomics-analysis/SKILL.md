---
name: metabolomics-analysis
description: >
  Use for metabolomics and lipidomics data: untargeted or targeted LC-MS, GC-MS,
  or NMR, feature detection, QC samples, drift correction, normalization,
  metabolite identification confidence, missing values, PCA, PLS-DA, and
  pathway interpretation.
license: CC-BY-4.0
---

# Metabolomics Analysis

## Workflow

1. Capture platform, ionization mode, chromatography, extraction, and the run order, including blanks, pooled quality-control (QC) samples, and any internal standards. Randomize or block run order against the biological groups.
2. Process features (detection, alignment, gap filling) with documented software versions and parameters. Remove features present in blanks, and use pooled-QC injections to monitor stability.
3. Correct signal drift and batch effects using QC-based methods, then filter features by QC reproducibility (for example a relative standard deviation threshold justified for the assay) and by missingness.
4. Normalize for sample amount or dilution using internal standards or methods such as probabilistic quotient normalization, then transform (often log) and scale (for example Pareto) as appropriate. Describe what each step changes.
5. Treat missing values by cause (below detection, not extracted, absent) and choose an imputation or filtering approach accordingly.
6. Report identification confidence with a recognized scale (for example Metabolomics Standards Initiative levels). A feature matched only on accurate mass is a putative annotation, not an identification.
7. Use univariate tests with multiplicity control alongside multivariate views (PCA first). Supervised models such as PLS-DA overfit easily, so validate with cross-validation and permutation tests, and never present training-set separation as evidence.
8. Interpret pathway results cautiously: annotation coverage, ambiguous identities, and database bias strongly affect enrichment.

## Deliverable

Acquisition summary, QC outcomes, preprocessing steps and rationale, identification confidence per reported metabolite, statistics with adjusted p-values and validation, and limitations. Do not assign metabolite identities that were not supported by the data.
