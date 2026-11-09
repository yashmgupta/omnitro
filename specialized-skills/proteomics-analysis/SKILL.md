---
name: proteomics-analysis
description: >
  Use for mass-spectrometry proteomics or phosphoproteomics data analysis: DDA,
  DIA, TMT, label-free quantification, protein groups, missing values,
  normalization, imputation, batch correction, differential abundance, PTM site
  localization, FDR, or MaxQuant, DIA-NN, Spectronaut, FragPipe, Proteome
  Discoverer outputs.
license: CC-BY-4.0
---

# Proteomics Data Analysis

## Workflow

1. Record the acquisition (DDA, DIA, TMT or other labeling), search engine and version, database and release, FDR thresholds, and sample design including replicates and batches. Reading the right output table (protein groups, peptides, PTM sites) matters for the question.
2. Remove contaminants, decoy or reverse hits, and entries flagged as only identified by site where the software provides that flag. Confirm FDR was controlled at the level you report (PSM, peptide, protein).
3. Run QC at sample level: identified features, missingness, intensity distributions, retention-time or injection-order drift, and sample relationships by PCA or clustering. Investigate outliers against metadata before removing any.
4. Filter by missingness with a documented, design-aware rule (for example valid values within at least one group). Treat missingness as informative: low-abundance proteins are often missing not at random.
5. Normalize with a method justified by the data (median, quantile, variance-stabilizing). For TMT, handle batch structure with an internal reference or equivalent scaling.
6. Impute only when a method requires it, and choose by mechanism: left-censored approaches for missing-not-at-random values and neighbor-based methods only for missing-at-random values. Imputation can create false signal, so compare results with and without it.
7. Correct batch effects with a method that includes the design, and never when batch is confounded with condition.
8. Test differential abundance with models that borrow strength across proteins (for example moderated linear models) and handle peptide-to-protein inference explicitly. Control FDR and report effect sizes.
9. For phosphoproteomics and other PTMs, use localization probabilities, consider normalization to protein abundance, and interpret site-level changes separately from protein changes.
10. Deposit raw data and search results in a proteomics repository such as PRIDE (via ProteomeXchange) where permitted.

## Deliverable

Software and database versions, QC plots, filtering and normalization rationale, imputation choice with sensitivity, statistical model, results with adjusted p-values, and limitations. Never fabricate identifications or quantities.
