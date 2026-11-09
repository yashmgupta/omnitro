# Biomedical Research Superagent Pack

A portable set of instructions and modular skills for configuring an AI assistant to help with biomedical research. This is an independently written starter pack, not an official Biomni project or a replacement for Biomni's software, tools, or data.

## What is included

- `AGENTS.md` — top-level, tool-agnostic behavior and output instructions.
- `skills/literature-review/SKILL.md` — evidence-focused literature reviews.
- `skills/study-design/SKILL.md` — conceptual study planning.
- `skills/data-analysis/SKILL.md` — reproducible analysis planning and interpretation.
- `LICENSE` — CC-BY-4.0 terms for this instructional content.

## Use it

1. Unzip the pack (or clone this repo).
2. Give your AI assistant `AGENTS.md` as its project instructions, or paste its contents into the assistant's system/project-instructions field.
3. If the assistant supports the Agent Skills format, make the `skills/` directory available to it. Otherwise, provide the relevant `SKILL.md` when asking for that kind of work.
4. Ask a specific task, such as: “Review the evidence for this research question and identify disagreements, limitations, and source links.”

For a GitHub project, add these files to the repository and point your assistant to `AGENTS.md`. Keep the `skills/` folders intact so tools that discover Agent Skills can find each `SKILL.md`.

## Important limitations

These are instructions, not a model, executable agent, biomedical database, or set of analysis tools. Results depend on the AI model and tools available in the environment. Web search, code execution, access to papers, and data analysis require a compatible assistant or separately configured tools. Do not put API keys, private patient data, or other sensitive information in this pack or a public repository.

The pack is for research support and education, not diagnosis, treatment, or clinical decision-making. Validate scientific claims and consult qualified experts and institutional safety and ethics processes before acting on research suggestions.
