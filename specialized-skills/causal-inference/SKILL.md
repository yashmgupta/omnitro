---
name: causal-inference
description: >
  Use when the user asks whether an exposure or treatment causes an outcome using
  observational data: confounding, DAGs, propensity scores, inverse probability
  weighting, target trial emulation, instrumental variables, Mendelian
  randomization, E-values, negative controls, or mediation.
license: CC-BY-4.0
---

# Causal Inference from Observational Data

## Workflow

1. State the causal question as a contrast (what intervention versus what comparator, in which population, over what time horizon). Consider specifying a target trial: eligibility, treatment strategies, time zero, outcomes, and follow-up.
2. Draw a directed acyclic graph from subject knowledge. Adjust for common causes of exposure and outcome; do not adjust for colliders or post-exposure mediators when estimating a total effect. Document assumptions as untestable.
3. Align time zero with eligibility and treatment assignment to avoid immortal-time and selection biases.
4. Choose an estimation approach: regression adjustment, propensity score matching or weighting, g-methods, or doubly robust estimators. Check positivity and overlap, covariate balance (for example standardized mean differences), and influence of extreme weights.
5. Quantify sensitivity to unmeasured confounding (for example the E-value) and use negative control outcomes or exposures where available. These assess plausibility; they do not prove absence of bias.
6. For Mendelian randomization, state the three instrument assumptions (relevance, independence from confounders, exclusion restriction). Check instrument strength, pleiotropy (sensitivity estimators such as weighted median and MR-Egger), sample overlap, ancestry matching, and whether harmonization of alleles was correct. Results depend on the validity of the instruments.
7. Report estimates with uncertainty and describe the strength of causal language the design supports. Association, prediction, and causal effect are distinct claims.

## Deliverable

The causal question, DAG or assumption list, estimator and diagnostics, effect estimates with intervals, sensitivity analyses, and a plain statement of what remains unidentified. Never describe an observational association as proof of causation.
