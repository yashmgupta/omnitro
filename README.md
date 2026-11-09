# Biomedical Research Superagent Pack

A portable set of instructions and modular skills for configuring an AI assistant to help with biomedical research. This is an independently written starter pack, not an official Biomni project or a replacement for Biomni's software, tools, or data.

## What is included

- `AGENTS.md` — top-level, tool-agnostic behavior and output instructions.
- `skills/literature-review/SKILL.md` — evidence-focused literature reviews.
- `skills/study-design/SKILL.md` — conceptual study planning.
- `skills/data-analysis/SKILL.md` — reproducible analysis planning and interpretation.
- `specialized-skills/` — specialist research, bioinformatics, and communication workflows listed below.
- `docs/EVALUATION.md` — practical scenarios for evaluating agent behavior.
- `docs/SOURCES.md` — research references and attribution.
- `examples/single-cell-replication.md` — a worked example using fictional inputs.
- `LICENSE` — CC-BY-4.0 terms for this instructional content.

## Specialist skills

| Skill | Use for |
| --- | --- |
| [Genomics variants](specialized-skills/genomics-variants/SKILL.md) | Variant calls, reference builds, and research prioritization |
| [Bulk RNA-seq](specialized-skills/rna-seq-analysis/SKILL.md) | Count data, experimental designs, and differential expression |
| [Single-cell analysis](specialized-skills/single-cell-analysis/SKILL.md) | Cell QC, annotation, and donor-aware comparisons |
| [Biomedical databases](specialized-skills/biomedical-databases/SKILL.md) | Database records, identifiers, and provenance |
| [Pathway enrichment](specialized-skills/pathway-enrichment/SKILL.md) | Gene sets, enrichment methods, and interpretation |
| [Scientific writing](specialized-skills/scientific-writing/SKILL.md) | Manuscripts, abstracts, reporting, and editing |
| [Research tables](specialized-skills/research-tables/SKILL.md) | Evidence tables, cohort summaries, and data dictionaries |
| [Scientific visualization](specialized-skills/scientific-visualization/SKILL.md) | Accessible, reproducible figures and legends |
| [Python research](specialized-skills/python-research/SKILL.md) | Reproducible scripts, data checks, and analysis |
| [Research ideation](specialized-skills/research-ideation/SKILL.md) | Hypotheses, research directions, and prioritization |
| [Research model selection](specialized-skills/research-model-selection/SKILL.md) | Assessing biomedical models, datasets, licenses, and benchmarks |

## Use it

1. Unzip the pack (or clone this repo).
2. Give your AI assistant `AGENTS.md` as its project instructions, or paste its contents into the assistant's system/project-instructions field.
3. Give it the relevant `SKILL.md` from `skills/` or `specialized-skills/`. If your assistant supports Agent Skills discovery, install or copy each desired skill **folder** to the skill directory specified by that assistant's documentation. Discovery locations and automatic loading differ between products; this repository's folders are not guaranteed to be discovered automatically.
4. Ask a specific task, such as: “Review the evidence for this research question and identify disagreements, limitations, and source links.”

For a GitHub project, add these files to the repository and point your assistant to `AGENTS.md`. Keep each skill folder intact. For an assistant without file access, paste the relevant instructions into its project settings or conversation, subject to its instruction hierarchy and context limits.

To check the pack's supported frontmatter format and folder names locally, run `python3 scripts/check_skills.py`. To test that checker, run `python3 -m unittest discover -s tests`. See `docs/EVALUATION.md` for behavioral checks; structural validation does not prove that an AI follows the instructions.

## Important limitations

These are instructions, not a model, executable agent, biomedical database, or set of analysis tools. Results depend on the AI model and tools available in the environment. Web search, code execution, access to papers, and data analysis require a compatible assistant or separately configured tools. Do not put API keys, private patient data, or other sensitive information in this pack or a public repository.

The pack is for research support and education, not diagnosis, treatment, or clinical decision-making. Validate scientific claims and consult qualified experts and institutional safety and ethics processes before acting on research suggestions.
