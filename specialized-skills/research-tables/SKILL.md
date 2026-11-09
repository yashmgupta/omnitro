---
name: research-tables
description: Create, check, or format scientific evidence tables, study-characteristics tables, data dictionaries, and statistical results tables. Use for spreadsheets, manuscript tables, cohort summaries, and research comparisons.
license: CC-BY-4.0
---

# Research Tables

## Workflow

1. Define the purpose, audience, input data, unit of observation, desired format, and column definitions. Preserve source identifiers so every reported value can be traced back.
2. Validate data types, units, denominators, missing-value codes, duplicated rows, and consistency of group labels before summarizing. State whether percentages use all participants, available cases, or another denominator.
3. Choose summaries appropriate to the data and design. Label sample sizes and distinguish standard deviation, standard error, confidence intervals, and ranges; do not infer one from another without sufficient information.
4. Preserve numeric values internally, apply consistent rounding only for display, and report exact tests and multiple-testing adjustments when supplied. Never fabricate data or p-values to fill a table.
5. Make the table accessible with descriptive headers, units, defined abbreviations, and explanatory footnotes. Sanitize untrusted cell values before exporting to spreadsheet formats if a spreadsheet application might interpret them as formulas.

## Helper script

Neutralize spreadsheet formula injection (cells starting with `=`, `+`, `-`, `@`) in a CSV before sharing or opening it in a spreadsheet:

`python3 specialized-skills/research-tables/scripts/safe_csv.py input.csv output.csv`

## Deliverable

Return the requested table with a caption or data dictionary and caveats. Mark missing values explicitly, avoid exposing identifiable records, and state whether summaries were actually calculated or are illustrative templates.
