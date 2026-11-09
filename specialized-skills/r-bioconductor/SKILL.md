---
name: r-bioconductor
description: >
  Use for R and Bioconductor work in genomics: SummarizedExperiment,
  SingleCellExperiment, GenomicRanges, DESeq2, edgeR, limma, tidyverse data
  handling, ggplot2 figures, package installation and renv lockfiles,
  Bioconductor release matching, and common R debugging in bioinformatics.
license: CC-BY-4.0
---

# R and Bioconductor

## Workflow

1. Check the R version and the matching Bioconductor release before installing anything. Bioconductor packages are versioned in lockstep with R and with each other. Install with `BiocManager::install()` and avoid mixing releases.
2. Capture the environment with `renv` (or equivalent) and record `sessionInfo()` in the output so analyses can be rerun (see `reproducible-workflows`).
3. Use standard containers for data: `SummarizedExperiment` for matrices plus row and column annotations, `SingleCellExperiment` for single-cell data, and `GRanges` for genomic intervals. Keep sample metadata aligned with matrix columns and assert that alignment explicitly.
4. Mind coordinate conventions: `GRanges` is 1-based and closed, and seqlevel naming styles must match across objects (see `genomic-coordinates`).
5. For count-based testing, give the full design formula, set factor reference levels deliberately, filter low-count features by a stated rule, and inspect dispersion and diagnostic plots before reading results (see `rna-seq-analysis`).
6. Prefer vectorized and tidy approaches. Avoid growing objects in loops, and use `stopifnot()` or explicit checks for dimension and name agreement.
7. Debug by reading the exact error, checking object classes with `class()` and `str()`, then reducing to a minimal reproducible example. Common causes are factor level mismatches, duplicated names, and version conflicts.
8. For figures, export with explicit dimensions and resolution, and with text sizes legible at final print size (see `scientific-visualization`).

## Deliverable

Scripts that run top to bottom, a lockfile or session info, saved intermediate objects with clear names, and a note of Bioconductor and package versions. Do not silently coerce or drop samples to make code run.
