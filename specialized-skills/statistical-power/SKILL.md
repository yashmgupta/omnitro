---
name: statistical-power
description: >
  Use when the user asks about sample size, statistical power, minimum detectable
  effect, number of replicates, or whether a study or experiment is
  underpowered. Also use to review power statements in protocols and grants.
  Covers means, proportions, clustering, dropout, and why omics studies need
  design-specific power tools. Includes a tested stdlib calculator.
license: CC-BY-4.0
---

# Statistical Power and Sample Size

## Workflow

1. Fix the design first: primary outcome, comparison, unit of analysis (animal, donor, cluster, cell?), paired or independent, one- or two-sided test, alpha, and target power. Sample size is meaningless until these are stated.
2. Source the effect size from prior data, a pilot with its uncertainty, or the smallest effect that would matter scientifically or clinically. Do not take a "small/medium/large" convention as evidence. Pilot effect estimates are noisy and often optimistic; consider a conservative value.
3. Estimate variability from comparable data, with its uncertainty. For counts, proportions, and time-to-event outcomes use the matching model rather than a normal-means shortcut.
4. Adjust for design features: dropout or missing outcomes, clustering (design effect about `1 + (m - 1) * ICC`), unequal allocation, repeated measures, covariate adjustment, and multiple primary outcomes or multiplicity corrections.
5. For quick planning of two-group means or proportions, use `scripts/power.py` (normal approximation; stdlib only):
   - `python3 specialized-skills/statistical-power/scripts/power.py means --d 0.5 --dropout 0.2`
   - `python3 specialized-skills/statistical-power/scripts/power.py props --p1 0.5 --p2 0.3`
   - `python3 specialized-skills/statistical-power/scripts/power.py power-means --n 40 --d 0.6`
6. For omics (RNA-seq, proteomics, single-cell), power depends on depth, dispersion, effect size distribution, and the number of independent biological units, so use omics-specific tools or simulation and say which assumptions were used.
7. Run a sensitivity analysis across plausible effect sizes and variances, and report the range.

## Pitfalls

- Post-hoc or "observed" power from a completed study is uninformative; report confidence intervals instead.
- Cells, technical replicates, and repeated measures from the same subject are not independent replicates.
- Never claim a study is adequately powered without stating every input assumption.

## Deliverable

State design, assumptions, sources for each input, the calculation and tool used, a sensitivity range, and the inflated recruitment target. Recommend review by a statistician for confirmatory or regulated studies.
