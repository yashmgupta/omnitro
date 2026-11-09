# Biomedical Research Superagent Pack

A portable set of instructions and modular skills for configuring an AI assistant to help with biomedical research. This is an independently written starter pack, not an official Biomni project or a replacement for Biomni's software, tools, or data.

## What is included

- `AGENTS.md` — top-level, tool-agnostic behavior and output instructions.
- `skills/literature-review/SKILL.md` — evidence-focused literature reviews.
- `skills/study-design/SKILL.md` — conceptual study planning.
- `skills/data-analysis/SKILL.md` — reproducible analysis planning and interpretation.
- `specialized-skills/` — specialist research, bioinformatics, and communication workflows listed in the catalog below.
- `INDEX.md`, `skills-index.json`, `llms.txt` — generated catalogs for humans and machines.
- `docs/EVALUATION.md` — practical scenarios for evaluating agent behavior.
- `docs/SOURCES.md` — research references and attribution.
- `examples/single-cell-replication.md` — a worked example using fictional inputs.
- `LICENSE` — CC-BY-4.0 terms for this instructional content.

## Skill catalog

45 skills in 8 categories. The full, generated catalog is in [INDEX.md](INDEX.md); machine-readable versions are [skills-index.json](skills-index.json) and [llms.txt](llms.txt).

| Category | Skills |
| --- | --- |
| Core research workflow | literature-review, study-design, data-analysis, research-ideation, search-strategy |
| Statistics and evidence | statistical-power, statistical-analysis, survival-analysis, causal-inference, meta-analysis, evidence-appraisal, reporting-guidelines, biomedical-machine-learning, research-model-selection |
| Genomics and sequencing | sequencing-qc-alignment, genomic-coordinates, genomics-variants, rna-seq-analysis, chip-atac-seq, gwas-statistical-genetics, crispr-screen-analysis, phylogenetics |
| Single-cell, spatial and multi-omics | single-cell-analysis, spatial-transcriptomics, multi-omics-integration |
| Proteins, metabolites and microbes | proteomics-analysis, metabolomics-analysis, protein-structure, metagenomics-microbiome |
| Databases, pathways and chemistry | biomedical-databases, pathway-enrichment, cheminformatics-drug-discovery |
| Writing, tables and figures | scientific-writing, research-tables, scientific-visualization, scientific-presentations, grant-writing, peer-review, manuscript-revision |
| Integrity, data and tooling | citation-verification, research-ethics-biosafety, research-data-management, reproducible-workflows, python-research, r-bioconductor |

### Helper scripts

Standard-library-only Python helpers (no installs needed), each covered by tests in `tests/test_scripts.py`:

| Script | Purpose |
| --- | --- |
| `specialized-skills/statistical-power/scripts/power.py` | Normal-approximation sample size and power for means and proportions |
| `specialized-skills/statistical-analysis/scripts/multiple_testing.py` | Benjamini-Hochberg, Holm and Bonferroni adjustment |
| `specialized-skills/genomics-variants/scripts/vcf_summary.py` | Offline VCF sanity summary |
| `specialized-skills/rna-seq-analysis/scripts/check_counts_metadata.py` | Count matrix versus metadata consistency |
| `specialized-skills/research-tables/scripts/safe_csv.py` | CSV formula-injection sanitizer |
| `specialized-skills/citation-verification/scripts/doi_tools.py` | Offline DOI extraction and duplicate detection |
| `specialized-skills/reproducible-workflows/scripts/snapshot_env.py` | JSON provenance snapshot with input checksums |

## Use it

1. Unzip the pack (or clone this repo).
2. Give your AI assistant `AGENTS.md` as its project instructions, or paste its contents into the assistant's system/project-instructions field.
3. Give it the relevant `SKILL.md` from `skills/` or `specialized-skills/`. If your assistant supports Agent Skills discovery, install or copy each desired skill **folder** to the skill directory specified by that assistant's documentation. Discovery locations and automatic loading differ between products; this repository's folders are not guaranteed to be discovered automatically.
4. Ask a specific task, such as: “Review the evidence for this research question and identify disagreements, limitations, and source links.”

For a GitHub project, add these files to the repository and point your assistant to `AGENTS.md`. Keep each skill folder intact. For an assistant without file access, paste the relevant instructions into its project settings or conversation, subject to its instruction hierarchy and context limits.

To check the pack's supported frontmatter format and folder names locally, run `python3 scripts/check_skills.py`. After adding or renaming a skill, add it to `docs/categories.json` and run `python3 scripts/build_index.py` (`--check` verifies the generated files are current). To run all tests, use `python3 -m unittest discover -s tests`. See `docs/EVALUATION.md` for behavioral checks; structural validation does not prove that an AI follows the instructions.

## Important limitations

These are instructions, not a model, executable agent, biomedical database, or set of analysis tools. Results depend on the AI model and tools available in the environment. Web search, code execution, access to papers, and data analysis require a compatible assistant or separately configured tools. Do not put API keys, private patient data, or other sensitive information in this pack or a public repository.

The pack is for research support and education, not diagnosis, treatment, or clinical decision-making. Validate scientific claims and consult qualified experts and institutional safety and ethics processes before acting on research suggestions.
