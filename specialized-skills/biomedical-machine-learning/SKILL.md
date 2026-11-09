---
name: biomedical-machine-learning
description: >
  Use when building, reviewing, or interpreting machine-learning or
  deep-learning models on biomedical data: classifiers, prognostic or diagnostic
  prediction, biomarker panels, omics-based models, imaging models, data
  leakage, cross-validation, calibration, external validation, class
  imbalance, interpretability, or model cards.
license: CC-BY-4.0
---

# Biomedical Machine Learning

## Workflow

1. Define the prediction target, the moment of prediction, the intended use, and who acts on it. A model with no decision context has no defined success criterion.
2. Split data at the level of the independent unit (patient, donor, batch, site), not rows, images, or cells. Keep a final test set untouched until the end.
3. Prevent leakage: fit imputation, scaling, feature selection, and dimensionality reduction inside each training fold only; exclude features that encode the outcome or its downstream consequences; deduplicate near-identical samples; check that batch, site, or scanner does not predict the label.
4. Use nested or otherwise honest cross-validation when tuning, and compare against simple baselines (clinical covariates, logistic regression). In high-dimensional, small-sample settings favor regularized models and report variance across folds.
5. Evaluate with metrics suited to prevalence and use: AUROC with AUPRC when classes are imbalanced, plus calibration, sensitivity and specificity at a stated threshold, and decision-curve analysis when decisions matter. Give confidence intervals (for example bootstrap at the patient level).
6. Validate externally in an independent cohort, site, or time period, and assess subgroup performance for fairness and distribution shift.
7. Treat interpretability outputs such as feature importance or SHAP values as descriptions of the model, not causal biology.
8. Report with TRIPOD (including AI extensions) and document data, code, versions, seeds, intended use, and limitations in a model card.

## Boundaries

Do not present a research model as a validated diagnostic tool. Clinical deployment requires prospective validation, regulatory review, and clinical oversight.

## Deliverable

Task definition, data splits, leakage safeguards, baselines, metrics with intervals, external validation status, failure modes, and an explicit intended-use and limitations statement. Report only results that were actually computed.
