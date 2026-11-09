---
name: statistical-analysis
description: >
  Use when the user needs to choose, run, check, or interpret statistical tests
  for biomedical data: t-tests, nonparametric tests, regression, mixed models,
  confidence intervals, effect sizes, p-values, multiple-testing correction,
  FDR, missing data, outliers, or pseudoreplication. Includes a tested
  multiple-testing calculator.
license: CC-BY-4.0
---

# Statistical Analysis

## Workflow

1. State the estimand: what quantity answers the question, in which population, with what comparison. Fix the primary analysis before looking at outcomes; label everything else exploratory.
2. Identify the unit of independence. Repeated measures, litter or cage effects, cells from one donor, and technical replicates require paired tests, mixed models, or aggregation to the biological unit.
3. Choose a method that matches the outcome type (continuous, binary, count, ordinal, time-to-event), design, and covariates. Check assumptions with residual or diagnostic plots rather than relying only on significance tests of assumptions. Nonparametric tests test different hypotheses and are not an automatic fix.
4. Report effect size with a confidence interval, the exact test, sample sizes per group, and the exact p-value. Statistical significance is not scientific importance, and a non-significant result is not evidence of no effect.
5. Control multiplicity across the family of tests actually performed: family-wise error (Holm, Bonferroni) when any false positive matters, false discovery rate (Benjamini-Hochberg) for large discovery screens. Compute with `scripts/multiple_testing.py`:
   - `python3 specialized-skills/statistical-analysis/scripts/multiple_testing.py pvalues.txt`
   - `python3 specialized-skills/statistical-analysis/scripts/multiple_testing.py results.tsv --column pvalue`
6. Handle missing data deliberately: describe the amount and likely mechanism (MCAR, MAR, MNAR), run complete-case and a principled method such as multiple imputation as sensitivity analyses, and avoid mean imputation for inference.
7. Do not remove outliers without a pre-specified, justified rule; report analyses with and without influential points when relevant.
8. Distinguish description, association, prediction, and causal claims, and keep conclusions at the strength the design supports.

## Pitfalls

- Selective reporting, optional stopping, and trying many analyses until one is significant inflate false positives.
- Dichotomizing continuous variables discards information.
- Adjusting p-values within one subgroup while testing across many subgroups understates multiplicity.

## Deliverable

Give the analysis plan or results, assumptions checked, effect sizes with intervals, adjustment method, sensitivity analyses, and limitations. Report only results that were actually computed.
