---
name: gwas-statistical-genetics
description: >
  Use for genome-wide association studies and statistical genetics: sample and
  variant QC, population stratification, mixed models, REGENIE, SAIGE, PLINK,
  summary statistics, LD, clumping, fine-mapping, colocalization, heritability,
  polygenic scores, and harmonizing alleles across datasets.
license: CC-BY-4.0
---

# GWAS and Statistical Genetics

## Workflow

1. Define phenotype, ascertainment, ancestry composition, genotyping or sequencing platform, imputation reference, and genome build for every dataset. Mismatched builds or allele coding silently corrupt results.
2. Apply sample QC (call rate, sex concordance, heterozygosity, relatedness, duplicates) and variant QC (call rate, Hardy-Weinberg deviation in controls, minor allele frequency, imputation quality). State thresholds and why they suit the data.
3. Control population structure with ancestry principal components and, where appropriate, mixed models that account for relatedness. Do not pool ancestries without handling stratification.
4. Choose software for the trait: linear or logistic models, mixed models, or methods built for severe case-control imbalance and rare variants.
5. Use the conventional genome-wide significance threshold for common-variant studies, and report genomic inflation or an equivalent diagnostic. Inflation can reflect polygenicity as well as confounding.
6. For summary statistics, harmonize alleles and strand (palindromic variants need care), confirm effect-allele direction, and match LD reference ancestry to the study.
7. Prioritize loci with LD clumping or statistical fine-mapping (credible sets), and test colocalization with expression or other traits while stating its assumption of a single shared causal variant. Association does not identify the causal gene.
8. For polygenic scores, build on a discovery set and evaluate on a fully independent target set, report incremental variance explained, and describe reduced portability across ancestries. Scores are research tools, not individual risk predictions.
9. Handle controlled-access and identifiable data under the approved data use terms. Genotype data are inherently identifying.

## Deliverable

Cohort and QC summary, model and covariates, diagnostics, significant loci with effect sizes and build, fine-mapping or colocalization results if run, replication status, and limitations. Do not make clinical or ancestry-based claims about individuals.
