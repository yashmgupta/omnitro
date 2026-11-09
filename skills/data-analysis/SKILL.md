---
name: data-analysis
description: >
  Use when the user asks to analyze, interpret, or write code for biomedical
  or clinical data — e.g. "analyze this dataset", "what statistical test
  should I use", "interpret these results", "help me with this scRNA-seq /
  GWAS / clinical trial data", "check this analysis for errors", or shares a
  data file and asks for findings. Produces reproducible, assumption-aware
  analysis and avoids reporting results that were not actually computed.
license: CC-BY-4.0 (see LICENSE)
---

# Biomedical Data Analysis

Use this skill for analysis planning, code help, interpretation, or review of biomedical datasets.

## Workflow

1. Establish the data source, unit of observation, outcome, comparison, and intended inference. Ask what each column means if unclear.
2. Check whether data are de-identified and whether the user is authorized to share them. Do not request direct identifiers or unnecessary sensitive details.
3. Inspect missingness, data types, duplicates, outliers, measurement units, and possible batch or sampling effects before choosing methods.
4. Match the method to the design and assumptions. Distinguish descriptive, exploratory, predictive, and causal analyses.
5. If code execution is available, make the analysis reproducible and report what was actually run. Otherwise provide code or a plan without claiming results.
6. Explain uncertainty, multiple-comparison concerns, confounding, validation requirements, and limits to generalization.
7. Keep conclusions proportional to the data. A predictive association is not proof of causation or clinical utility.

## Output

Describe the question, data checks, method and assumptions, results (only if computed), limitations, and reproducibility details. Include code when requested and when the environment supports a reliable implementation. Never fabricate statistics or imply an analysis was run when it was not.
