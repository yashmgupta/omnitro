---
name: crispr-screen-analysis
description: >
  Use for analysis and interpretation of pooled CRISPR knockout, CRISPRi, or
  CRISPRa screens and Perturb-seq: guide count QC, library coverage, replicate
  correlation, gene essentiality, MAGeCK, BAGEL, drugZ, copy-number bias,
  hit calling, and validation planning. Analysis only, not laboratory protocols.
license: CC-BY-4.0
---

# CRISPR Screen Analysis

## Workflow

1. Capture the design: library and guides per gene, non-targeting and positive or negative control guides, cell model, perturbation type, selection or phenotype readout, timepoints, replicates, and the genome build used for guide mapping.
2. Count guides from sequencing reads with exact library matching and report the fraction of reads mapped. Examine guide representation at baseline: coverage per guide, zero-count guides, and distribution skew (for example the Gini index).
3. Check replicate correlation and whether control separation matches expectations: depletion of core essential genes and non-depletion of non-targeting guides in survival screens. A screen that fails these controls should not be interpreted gene by gene.
4. Normalize to library size or controls, and account for bottlenecking or low coverage, which add noise that no statistic can remove.
5. Choose a method for the question: robust rank aggregation or maximum-likelihood models (for example MAGeCK) for gene-level scores, Bayesian essentiality frameworks, or methods designed for drug-gene interaction screens. State the contrast and the test direction.
6. Correct for copy-number effects, since cutting in amplified regions causes guide depletion unrelated to gene function, and for guide efficiency or off-target risks where possible.
7. Call hits using FDR control and effect sizes, require concordance across independent guides, and compare with orthogonal resources (for example public dependency data) as context, not proof.
8. Plan validation with independent guides and orthogonal perturbation, and distinguish genes with phenotypes from direct mechanistic targets.
9. For single-cell perturbation screens, handle guide assignment, multiplicity of infection, and per-cell perturbation efficiency explicitly.

## Deliverable

QC summary with control performance, method and parameters, ranked hits with FDR and effect sizes, bias corrections applied, validation plan, and limitations. Do not call hits from a screen that failed its controls.
