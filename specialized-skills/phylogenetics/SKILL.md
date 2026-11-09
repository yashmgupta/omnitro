---
name: phylogenetics
description: >
  Use for evolutionary and sequence-comparison analysis: multiple sequence
  alignment, alignment trimming, substitution model selection, maximum
  likelihood or Bayesian tree inference, bootstrap and posterior support,
  rooting, molecular clock dating, orthology, and tree interpretation.
license: CC-BY-4.0
---

# Phylogenetics

## Workflow

1. State the question: species relationships, gene family evolution, outbreak or lineage tracking, or dating. Choose sequences and taxa to suit it, including appropriate outgroups.
2. Distinguish orthologs from paralogs before inferring species relationships. Gene trees need reconciliation with species trees when duplications or transfers are present.
3. Align sequences with a method suited to the data (nucleotide, protein, or codon-aware), inspect the alignment, and consider trimming only when it is justified. Poor alignment is the most common source of misleading trees.
4. Select a substitution model with a documented criterion, and account for rate heterogeneity. For coding sequences consider codon structure and saturation of third positions.
5. Infer the tree with maximum likelihood or Bayesian methods. Run multiple starts or chains, check convergence for Bayesian runs (effective sample sizes, agreement across chains), and keep the software versions and seeds.
6. Report branch support with the proper interpretation: bootstrap and posterior probabilities are not directly comparable measures, and high support does not imply a correct tree under model misspecification.
7. Root the tree with outgroups or a stated method, and avoid reading ancestry from the layout of tips. Only the branching pattern carries information.
8. For dating, test for temporal signal, pick clock and tree priors with justification, calibrate with sound evidence, and show prior sensitivity.
9. For pathogen data, record collection dates and metadata ethically and report sampling bias.

## Deliverable

Sequence sources and accessions, alignment and trimming decisions, model, method and software versions, support values, convergence diagnostics, tree files (Newick or Nexus) and limitations. Do not overstate relationships supported only by weak branches.
