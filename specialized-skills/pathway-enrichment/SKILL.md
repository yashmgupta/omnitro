---
name: pathway-enrichment
description: Analyze or interpret gene-set and pathway enrichment, over-representation analysis, ranked gene-set analysis, functional annotation, and biological pathway results. Use for GO, Reactome, and gene-list interpretation questions.
license: CC-BY-4.0
---

# Pathway and Gene-Set Interpretation

## Workflow

1. Define the biological question, organism, input gene identifiers, gene-list selection or ranking method, contrast direction, and source analysis. Verify identifier mapping and report unmapped or duplicated entries.
2. Choose a method appropriate to the input: over-representation analysis for a defined gene list, or ranked enrichment for a suitable ranked list. For over-representation, use a background representing genes eligible for selection, not an arbitrary whole genome.
3. Record the gene-set source and version, database access conditions, algorithm, parameters, background, and multiple-testing correction. Account for small gene sets and highly overlapping pathways when interpreting results.
4. Report adjusted p-values, effect or enrichment measures where applicable, gene-set size, and supporting or leading-edge genes. Distinguish pathway names from observed measurements and check the direction of the underlying gene-level effects.
5. Discuss dependency on thresholds, annotation coverage, gene length or detection biases where relevant, and enrichment stability. A significant pathway does not demonstrate activation, causality, or a validated mechanism by itself.

## Deliverable

Provide methods, a traceable results table if computed, interpretation, and limitations. If no input data or tools are available, give a plan and do not invent enriched pathways or statistics.
