---
name: survival-analysis
description: >
  Use for time-to-event analysis: Kaplan-Meier curves, log-rank tests, Cox
  proportional hazards models, hazard ratios, censoring, competing risks,
  overall or progression-free survival, time-varying covariates, immortal-time
  bias, or restricted mean survival time in clinical or biological cohorts.
license: CC-BY-4.0
---

# Survival and Time-to-Event Analysis

## Workflow

1. Define the event, the time origin (diagnosis, randomization, treatment start), the time scale, and the follow-up end. Define who is at risk and when. Ambiguous origins produce biased results.
2. Characterize censoring: right-censored subjects, administrative censoring, loss to follow-up, and whether censoring may relate to prognosis. Standard methods assume non-informative censoring.
3. Describe with Kaplan-Meier estimates and show numbers at risk. Report median follow-up using an appropriate method (for example reverse Kaplan-Meier) rather than a simple average.
4. For multivariable analysis, use a Cox model or a parametric alternative, and check the proportional hazards assumption with Schoenfeld residuals and plots. If violated, consider stratification, time-varying effects, or restricted mean survival time.
5. Handle competing risks (for example death before the event of interest) with cumulative incidence and cause-specific or subdistribution hazard models. One minus Kaplan-Meier overestimates incidence under competing risks.
6. Avoid immortal-time bias: do not classify exposure using information only available after follow-up begins. Use time-varying exposure definitions or landmark analysis.
7. Keep model complexity proportionate to the number of events, not the number of subjects, and pre-specify covariates. Report hazard ratios with confidence intervals and the event count.
8. For prognostic models, validate on independent data and report discrimination and calibration (see `biomedical-machine-learning`).

## Deliverable

Definitions, cohort and event counts, curves with risk tables, model specification, assumption checks, effect estimates with intervals, sensitivity analyses, and limitations. State that associations in observational cohorts are not necessarily causal.
