---
name: protein-structure
description: >
  Use for interpreting protein structure data and predictions: PDB and mmCIF
  files, AlphaFold or other predicted models, pLDDT, PAE, ipTM, experimental
  resolution and validation, domain and interface analysis, mapping variants to
  structure, and structure-based hypotheses about function.
license: CC-BY-4.0
---

# Protein Structure Interpretation

## Workflow

1. Identify the source: experimental (X-ray, cryo-EM, NMR) or predicted. Record entry IDs, release or version, chain, species, construct boundaries, ligands, and any modifications.
2. For experimental structures, check resolution, validation reports, R-free or map-model fit, local quality at the region of interest, and whether the biologically relevant assembly differs from the asymmetric unit. Crystal contacts and engineered constructs can mislead.
3. For predicted models, use confidence metrics: per-residue pLDDT for local confidence and predicted aligned error (PAE) for relative domain placement. Low-confidence regions are often disordered, and a high-confidence local fold can still have an unreliable domain arrangement.
4. For complexes, use interface confidence measures (for example ipTM and interface PAE) and treat predicted complexes as hypotheses. Where possible compare with experimental evidence, such as cross-linking or mutagenesis.
5. A predicted model is a single static conformation. It does not by itself tell you stability, binding affinity, ligand binding, or effects of mutation. Say so when asked about these.
6. When mapping variants, state the transcript and numbering scheme (UniProt versus construct numbering), then assess location (core, interface, active site, disordered) as supporting evidence only. Structure alone does not classify pathogenicity.
7. Use structural alignment or domain annotation to compare homologs, and cite the database sources.
8. Use dedicated tools for stability, docking, or dynamics, and describe their limitations rather than reading numbers from a model.

## Deliverable

Structure sources and versions, quality metrics with the regions used, interpretation tied to confidence, and explicit statements of what cannot be concluded. Do not present low-confidence regions as defined structure.
