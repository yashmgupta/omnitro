---
name: scientific-visualization
description: Design, generate, or review scientific plots and publication figures, including distributions, scatterplots, heatmaps, volcano plots, and multi-panel figures. Use for Python or R plotting, visual accessibility, and figure interpretation.
license: CC-BY-4.0
---

# Scientific Visualization

## Workflow

1. Identify the question, input data, biological unit, intended audience, and target output format. Select a plot that exposes the relevant comparisons, distributions, and uncertainty.
2. Validate the plotted data and transformations. Label axes, units, sample sizes, legends, and group names; specify log scales and pseudocounts where used. Do not silently omit outliers or truncate axes in misleading ways.
3. Prefer perceptually distinguishable, color-blind-accessible colors and legible text. Avoid using color alone to encode critical categories. Explain error bars and the level of replication in the figure legend.
4. For heatmaps and embeddings, report scaling, distance or reduction methods, clustering choices, and batch or sample context. For volcano plots, specify contrast direction, effect-size and adjusted-p-value definitions, and any thresholds.
5. Write reproducible plotting code with input and software versions, explicit random seeds when needed, and appropriate output dimensions. Use vector formats for suitable plots or high-resolution raster output when required by the venue.

## Deliverable

Provide a figure or code only when the environment supports it; otherwise offer a concrete design. Include a draft legend and disclose whether the plot was generated from real, supplied, or illustrative data. Never claim to have visually inspected a plot that was not rendered.
