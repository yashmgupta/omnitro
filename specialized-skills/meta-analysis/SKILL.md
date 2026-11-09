---
name: meta-analysis
description: >
  Use when the user wants to plan, run, critique, or interpret a systematic
  review or meta-analysis: pooling effect sizes, odds ratios, risk ratios, hazard
  ratios, standardized mean differences, heterogeneity, I-squared, forest
  plots, funnel plots, publication bias, subgroup analysis, or PRISMA flow.
license: CC-BY-4.0
---

# Systematic Review and Meta-analysis

## Workflow

1. Define the question (PICO or equivalent) and eligibility criteria before searching. Register or publish a protocol (for example PROSPERO) and note deviations. Use the `search-strategy` skill for searching.
2. Screen and extract in duplicate when possible, with a documented process for disagreements. Record the PRISMA 2020 flow numbers and reasons for exclusion.
3. Extract effect estimates and their uncertainty on a consistent scale. Choose the effect measure to match the outcome: risk ratio or odds ratio (binary), mean difference or standardized mean difference such as Hedges g (continuous), hazard ratio (time-to-event). Use adjusted estimates where available and note the adjustment set.
4. Check for unit-of-analysis problems: overlapping cohorts or duplicate publications, multi-arm trials counted more than once, cluster or crossover designs, and multiple outcomes from the same participants.
5. Assess risk of bias (see `evidence-appraisal`) and use it in sensitivity analyses.
6. Choose the model deliberately. Random-effects is usually appropriate when true effects may vary; with few studies, use an estimator and confidence interval method suited to small numbers (for example REML with a Hartung-Knapp-type adjustment) and report it. Pooling very different studies can be meaningless even when the model runs.
7. Quantify heterogeneity with tau-squared and I-squared and report a prediction interval, not just the pooled mean. Explore causes with prespecified subgroup or meta-regression analyses, noting the low power and ecological bias of such analyses.
8. Assess small-study effects and publication bias only when enough studies exist (commonly at least 10), interpret funnel asymmetry cautiously, and run leave-one-out and fixed-versus-random sensitivity analyses.
9. Handle zero events and rare outcomes with methods designed for them rather than ad hoc continuity corrections.

## Deliverable

Protocol summary, flow numbers, included-study table, pooled estimate with interval and prediction interval, heterogeneity, sensitivity analyses, certainty of evidence, and limitations. Do not compute or quote pooled numbers that were not derived from extracted data.
