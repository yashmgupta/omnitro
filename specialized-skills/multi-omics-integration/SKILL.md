---
name: multi-omics-integration
description: >
  Use when combining two or more molecular data layers (transcriptome,
  proteome, methylome, metabolome, genome, imaging, CITE-seq) on the same
  samples or cells: MOFA, mixOmics DIABLO, similarity network fusion, joint
  embeddings, factor analysis, matched versus unmatched samples, and
  cross-layer interpretation.
license: CC-BY-4.0
---

# Multi-omics Integration

## Workflow

1. Define the question: discovery of shared variation, prediction of an outcome, subtyping, or mechanistic linkage. The goal determines the method, and integration is not automatically better than analyzing layers separately.
2. Audit sample matching across layers. List which samples have which assays, how identifiers map, and how missing assays are handled. Confirm there are no sample swaps by checking known relationships (for example sex, genotype concordance, or expected correlations between layers).
3. QC and normalize each layer with methods suitable to its data type before integrating, and record batch structure per layer. Different layers have different scales, sparsity, and noise, so apply layer-specific scaling or weighting deliberately.
4. Choose a method that fits the data: factor models for unsupervised shared and unique variation, supervised multiblock methods for outcome-related features, network fusion for patient similarity, or weighted joint embeddings for paired single-cell modalities. State key hyperparameters and how they were selected.
5. Prevent leakage and overfitting in supervised integration by performing feature selection and tuning inside cross-validation, and by validating on independent samples.
6. Check that learned factors are not driven by batch, library size, or sample quality, and relate factors to metadata.
7. Interpret top-loading features with pathway or annotation analysis, and treat inferred cross-layer links as hypotheses requiring validation, not mechanisms.
8. Report layer-specific missingness and how it influenced the result.

## Deliverable

Sample-by-assay matrix, per-layer preprocessing, method and parameters, stability checks, validation status, interpretation with caveats, and limitations. State explicitly when conclusions rest on a single cohort.
