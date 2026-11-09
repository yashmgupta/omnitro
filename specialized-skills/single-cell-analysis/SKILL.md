---
name: single-cell-analysis
description: Plan or review single-cell RNA sequencing analysis, cell quality control, clustering, annotation, integration, and differential expression. Use for scRNA-seq, AnnData, Scanpy, Seurat, cell-type markers, and pseudobulk questions.
license: CC-BY-4.0
---

# Single-Cell RNA-seq

## Workflow

1. Establish organism, assay, count matrix format, sample and donor metadata, biological replicates, and research question. Confirm cell barcodes are unique and metadata rows match the matrix.
2. Review per-cell and per-sample QC metrics, including detected genes, counts, mitochondrial fraction when appropriate, and potential doublets or ambient RNA. Choose and justify dataset-specific criteria; visualize their effects and report removed cells.
3. Document normalization, feature selection, batch handling, dimensionality reduction, and clustering. Check whether differences in protocol or donor are confounded with condition; integration is not a substitute for an informative design.
4. Annotate clusters with multiple relevant markers and context. Identify ambiguous or low-quality clusters and distinguish marker-based labels from validated cell identity.
5. For condition comparisons, respect the biological unit of replication. Cells from the same donor are not independent biological replicates. Consider donor-level pseudobulk or suitable hierarchical models; if there is only one donor per condition, report that population-level inference is not supported.
6. Record software, reference annotation, parameters, random seeds where relevant, and the number of cells and donors retained per group. Avoid interpreting clusters, marker expression, or trajectories as proof of mechanism.

## Deliverable

Provide QC summaries, clear sample-level counts, defensible analysis choices, results only when actually computed, and limitations. Do not invent cell labels, marker genes, statistics, or tool execution.
