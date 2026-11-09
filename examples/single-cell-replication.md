# Worked example: single-cell replication

This is a fictional example illustrating how to apply the single-cell skill. No analysis, scientific claim, or model evaluation is implied.

## Input prompt

> I have 5,000 cells from one disease donor and 5,000 cells from one control donor. Can I treat all 10,000 cells as independent samples to prove a disease effect?

## Example response

No. Cells from the same donor share donor-specific characteristics, so treating them as independent biological replicates would underestimate uncertainty. There is only one biological donor per condition, and donor and condition are confounded. The data can support exploratory descriptions of these two samples, but not a reliable population-level disease comparison.

If feasible, obtain multiple independent donors per condition and record relevant sample metadata. Then consider a donor-level pseudobulk analysis or a suitable hierarchical model, with the analysis and assumptions reviewed by a qualified statistician. A larger number of cells from the same two donors does not replace independent donors.
