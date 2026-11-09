---
name: rna-seq-analysis
description: Plan or review bulk RNA-seq analysis, gene expression counts, differential expression, sample quality control, batch effects, and functional interpretation. Use for transcriptomics questions and count-matrix analysis.
license: CC-BY-4.0
---

# Bulk RNA-seq Analysis

## Workflow

1. Identify organism, reference assembly and annotation release, library preparation, count-generation method, sample metadata, biological replicates, and the precise contrast. Check that sample identifiers and group labels align between counts and metadata.
2. Inspect library sizes, low-count features, sample relationships, outliers, and potential batch effects. Preserve raw counts; use normalized or transformed values for appropriate visualizations, not as a substitute for raw counts in count-based models.
3. Specify a statistical design that reflects biological replication, pairing, covariates, and the experimental structure. Check whether group and batch are confounded. Do not claim that a model can separate effects when the design does not support it.
4. Choose an appropriate method such as DESeq2 or edgeR based on the input and design. State the contrast direction, filtering rule, multiple-testing correction, effect-size measure, and thresholds. Assess model assumptions and sensitivity where practical.
5. For functional interpretation, define the tested gene background, identifier mapping, database version, and enrichment method. Report effect sizes and adjusted p-values alongside uncertainty; enrichment does not establish a mechanism or causal relationship.

## Deliverable

Give the design and QC decisions, code or results only if actually generated, a reproducible environment, and limitations. Distinguish biological replicates from technical replicates. Never fabricate counts, differentially expressed genes, figures, or statistics.
