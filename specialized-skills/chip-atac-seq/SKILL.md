---
name: chip-atac-seq
description: >
  Use for ChIP-seq, CUT&RUN, CUT&Tag, and ATAC-seq analysis: read QC, FRiP,
  fragment size, TSS enrichment, peak calling, replicate reproducibility, blacklist
  regions, consensus peaks, differential binding or accessibility, motif
  analysis, and peak-to-gene assignment.
license: CC-BY-4.0
---

# ChIP-seq and ATAC-seq Analysis

## Workflow

1. Record assay, antibody or target with validation, controls (input or IgG), spike-ins, replicates, and genome build. Match reference and annotation versions throughout.
2. Run read QC and alignment (see `sequencing-qc-alignment`), then remove or flag duplicates, low mapping quality, mitochondrial reads (ATAC), and reads in problematic regions such as the ENCODE blacklist for the assembly.
3. Assess library quality using assay-appropriate metrics: library complexity, fraction of reads in peaks (FRiP), strand cross-correlation for ChIP, and TSS enrichment and nucleosome-periodic fragment sizes for ATAC. Compare to guidelines from the relevant consortium for the assay, but interpret against the biology (broad marks behave differently from transcription factors).
4. Call peaks with a method matched to signal shape (narrow versus broad), using control tracks where applicable. For ATAC, account for the transposase cut-site offset when analyzing at base resolution.
5. Assess replicate concordance (for example an irreproducible discovery rate framework or overlap with correlation) and build a consensus peak set explicitly.
6. For differential analysis, count reads in the consensus set per sample and use count-based models with an appropriate normalization. Global shifts in signal need spike-ins or other external calibration, because standard normalization can erase real global change.
7. For motif analysis choose a suitable background (for example GC-matched regions) and report enrichment with caveats. Motif presence does not prove direct binding.
8. Assigning peaks to the nearest gene is a heuristic. Support target-gene claims with chromatin contacts, correlation with expression, or perturbation data.

## Deliverable

Assay and reference details, QC metrics with thresholds used, peak calling parameters, replicate concordance, differential results with adjusted p-values, and limitations. Share peak files with their genome build.
