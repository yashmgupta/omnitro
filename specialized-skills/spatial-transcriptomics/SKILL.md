---
name: spatial-transcriptomics
description: >
  Use for spatial transcriptomics and spatial omics: Visium, Visium HD, Xenium,
  MERFISH, CosMx, Slide-seq, spot or cell segmentation, deconvolution, spatially
  variable genes, domain detection, niche or neighborhood analysis, cell-cell
  interaction, and multi-slide integration.
license: CC-BY-4.0
---

# Spatial Transcriptomics

## Workflow

1. Identify the platform, because it determines the analysis: spot-based capture measures mixtures of cells per spot, while imaging-based platforms measure targeted genes at or near single-cell resolution with segmentation uncertainty. Record tissue, sections, slides, and replicate structure.
2. Verify coordinates, image registration, and tissue masks. Check that barcodes, coordinates, and expression matrices line up and that scale factors are applied consistently.
3. QC per spot or cell using counts, detected genes, and platform-specific metrics. Inspect QC metrics on the tissue image, because low counts may be real tissue structure rather than failure. For imaging platforms evaluate segmentation quality and transcript assignment.
4. Normalize with attention to spatial and composition effects, and handle batch effects across slides explicitly, distinguishing technical from regional biology.
5. For spot data, estimate cell-type composition with a reference-based deconvolution method and validate the reference's relevance (species, tissue, state). Spots are not cells.
6. Detect spatial patterns with spatial autocorrelation tests or spatially variable gene methods, and identify domains with methods that use neighborhood information. Report parameters, because clusters depend heavily on spatial smoothing choices.
7. For neighborhood and interaction analyses, define neighborhoods (radius or graph) explicitly and use permutation tests. Ligand-receptor co-expression suggests, but does not demonstrate, signaling.
8. Treat tissue sections or donors as the replicates for inference. Spots or cells in one section are spatially correlated and not independent.

## Deliverable

Platform and design, QC on tissue, normalization and integration choices, domains or patterns with parameters, deconvolution reference and validation, statistics at the correct replication level, and limitations. Do not infer cell-cell communication or cell types without stating assumptions.
