---
name: metagenomics-microbiome
description: >
  Use for microbiome and metagenomic data: 16S or ITS amplicon sequencing,
  shotgun metagenomics, ASVs, taxonomy assignment, contamination, diversity
  metrics, PERMANOVA, compositional differential abundance, functional
  profiling, and longitudinal or low-biomass studies.
license: CC-BY-4.0
---

# Metagenomics and Microbiome Analysis

## Workflow

1. Record sample type, collection, storage, DNA extraction, target region or shotgun library prep, sequencing platform, and batches. Technical choices strongly shape microbial profiles, and they may be confounded with biology.
2. Process amplicon reads into amplicon sequence variants with a denoising method, remove chimeras, and assign taxonomy with a named reference database and version. Pipeline and database versions change results.
3. Use negative controls (extraction and PCR blanks) and mock communities where available to detect contamination and bias. Apply contaminant-identification methods, particularly for low-biomass samples, and report what was removed.
4. Recognize that sequencing data are compositional: relative abundances are not absolute abundances. Use compositionally aware methods (log-ratio transforms or models designed for compositions) and avoid claiming that a taxon "increased" when only proportions changed.
5. Compute alpha diversity (richness, Shannon, phylogenetic diversity) and beta diversity (Bray-Curtis, UniFrac, Aitchison distance) with a justified depth-handling approach. For group comparisons by PERMANOVA, also test dispersion, because differing spread can mimic location differences.
6. Model repeated measures and subject identity (mixed models or other appropriate methods) in longitudinal designs. Adjust for known covariates such as diet, medication, age, and batch.
7. Test differential abundance with methods designed for sparse compositional data, control FDR, and compare more than one approach when conclusions are important.
8. Treat predicted functional profiles from marker genes as inference, not measurement. Shotgun profiling supports function more directly but depends on reference coverage.
9. Deposit data with metadata that follows a community standard for environmental or host-associated samples.

## Deliverable

Pipeline and database versions, control performance, filtering steps, diversity and differential results with adjusted p-values, covariates, and limitations. Never present an association between taxa and disease as causal without supporting design.
