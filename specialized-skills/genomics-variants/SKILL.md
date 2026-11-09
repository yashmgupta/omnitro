---
name: genomics-variants
description: Analyze or interpret genomic variants, VCF files, variant annotations, genome builds, allele frequencies, and variant prioritization for research. Use for questions about SNPs, indels, variant filtering, or variant-quality assessment.
license: CC-BY-4.0
---

# Genomics and Variant Analysis

Use for research analysis of DNA sequence variants, not patient-specific diagnosis or clinical variant classification.

## Workflow

1. Establish the research question, organism, reference assembly and accession, sample type, sequencing method, and whether the input is raw reads, variant calls, or an annotation table. Ask for missing information that changes interpretation.
2. Record software and database versions and, where available, reference FASTA checksums and sample provenance. Verify genome build, contig naming, coordinate conventions, allele orientation, and transcript versions before joining sources. Do not silently convert builds.
3. For VCF data, assess sample and site quality using appropriate caller documentation: examine genotype quality, read depth, allele balance, missingness, and batch effects. Distinguish a missing call from a reference genotype. Choose thresholds from the assay and validated workflow, not generic defaults.
4. Normalize representations when appropriate and preserve the original records and transformations. Annotate using appropriate transcript consequences and population frequencies; consider ancestry, coverage, and database version. A frequency is not proof of pathogenicity.
5. Prioritize candidates against the stated research hypothesis and uncertainty. Separate observed genotypes, database annotations, computational predictions, and hypotheses. Note technical validation needs and alternative explanations.

## Deliverable

Provide a reproducible plan or actual computed results, with input and reference versions, selection criteria, limitations, and a candidate table when justified. If data, tools, or reference resources are unavailable, explicitly say so; never invent variants or annotations. Clinical use requires a qualified professional and validated clinical workflow.
