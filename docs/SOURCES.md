# Research sources and further reading

This is a curated snapshot, not an exhaustive catalog or ranking. It was checked on 2026-11-09. GitHub stars are approximate, change over time, and measure attention rather than scientific quality or safety. Descriptions are based on project documentation, not an audit or endorsement of every skill.

The skills in this pack are independently written, not copies of the repositories below. Each external project has its own license and terms. Check the specific file, model, dataset, and version before using or redistributing it; GitHub license detection can be incomplete.

## Biomedical and scientific skill catalogs

| Project | Snapshot stars | Why it is useful | License note |
| --- | ---: | --- | --- |
| [LabClaw](https://github.com/wu-yc/LabClaw) | 1,056 | Biology, literature, and visualization skill categories, including genomics and single-cell tools. | README identifies MIT; check the files you use. |
| [ScienceClaw](https://github.com/beita6969/ScienceClaw) | 1,027 | Broad science skills including bioinformatics, databases, statistics, and scientific writing. | MIT according to repository metadata. |
| [BioMate Bioconductor KB](https://github.com/bioMate-AI/biomate-bioconductor-kb) | 792 | Bioconductor package-oriented skills for transcriptomics, genomics, single-cell work, and other fields. | Project has different terms for skill content and scripts; consult its license. |
| [Paper Workbench](https://github.com/Yrzsh/paper-workbench) | 120 | Academic writing and evidence-verification workflows. | MIT according to repository metadata. |
| [Biomni](https://github.com/snap-stanford/Biomni) | Not ranked here | Biomedical agent software with broad biomedical tool categories; it is not just a skills catalog. | Biomni is Apache-2.0; integrated tools and databases may have other terms. |

## Additional skill collections surveyed (2026-11-09)

Surveyed to find coverage gaps; the new skills here are independently written, not copied. Counts and stars are snapshots from repository metadata and READMEs; they were not audited. Check each project's license file before reuse.

| Project | Snapshot | Notable scope | License note |
| --- | --- | --- | --- |
| [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | ~56.5k stars, 177 skills | Broad scientific skills with bundled scripts and references. | MIT per metadata. |
| [GPTomics bioSkills](https://github.com/GPTomics/bioSkills) | 562 skills | Very large bioinformatics catalog. Only skimmed by name here. | MIT per metadata. |
| [SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) | ~386 stars | Scientific agent skills. | Check repository. |
| [MannLabs proteomics-agent-skills](https://github.com/MannLabs/proteomics-agent-skills) | 11 skills | Proteomics workflows. | Apache-2.0 per metadata. |
| [medsci-skills](https://github.com/Aperivue/medsci-skills) | 63 skills | Medical research and reporting. | MIT per metadata. |
| [K-Dense drug-discovery-agent-skills](https://github.com/K-Dense-AI/drug-discovery-agent-skills) | 37 skills | Cheminformatics and drug discovery. | MIT per metadata. |
| [ssinder bioinformatics-agent-skills](https://github.com/ssinder/bioinformatics-agent-skills) | n/a | Bioinformatics skills. | MIT per metadata. |
| [aipoch medical-research-skills](https://github.com/aipoch/medical-research-skills) | n/a | Medical research skills. | MIT per metadata. |
| [AlterLab Academic Skills](https://github.com/AlterLab-IEU/AlterLab-Academic-Skills) | 241 skills (85 stars) | Academic research and writing. | MIT per metadata. |
| [awesome-genomic-skills](https://github.com/GoekeLab/awesome-genomic-skills) | n/a | Curated genomic skills list. | CC0 per metadata. |
| [awesome-bio-agent-skills](https://github.com/BioTender-max/awesome-bio-agent-skills) | n/a | Curated bio skills list. | Check repository. |
| [ClawBio](https://github.com/ClawBio/ClawBio), [KalarisLabs research-agent-skills](https://github.com/KalarisLabs/research-agent-skills), [ai4s-skills](https://github.com/ai4s-research/ai4s-skills), [scipilot-figure-skill](https://github.com/Haojae/scipilot-figure-skill), [claude-scientific-writer](https://github.com/K-Dense-AI/claude-scientific-writer), [paper-search-pro](https://github.com/O0000-code/paper-search-pro) | n/a | Bioinformatics, research workflow, figures, writing and paper search. | Check each repository. |

Design patterns adopted from these collections: skills that bundle small runnable scripts and references, trigger-rich descriptions, explicit verification statuses for citations, and machine-readable indexes. Design choices specific to this pack: stdlib-only helpers, a validator, a generated index with a category check, and safety boundaries for dual-use topics.

## Hugging Face and major AI company resources

| Project | Snapshot stars | What to explore |
| --- | ---: | --- |
| [Hugging Face Skills](https://github.com/huggingface/skills) | 11,306 | Skills for Hub access, datasets, model evaluation, and AI research papers. |
| [Hugging Face Semantic Scholar CLI](https://github.com/huggingface/s2-cli) | 31 | Read-only paper search and citation-graph CLI and skill; the project states an API key is required. |
| [Anthropic Skills](https://github.com/anthropics/skills) | 189,959 | Agent Skills examples and document-related skills. Licensing can vary by skill. |
| [OpenAI Plugins](https://github.com/openai/plugins) | 7,830 | Codex plugin and skill examples. The older `openai/skills` README directs users to this repository. |
| [Google Skills](https://github.com/google/skills) | 23,732 | Agent Skills for Google products and technologies. |
| [Microsoft Skills](https://github.com/microsoft/skills) | 3,187 | Skills, custom agents, and evaluation examples focused on Microsoft technologies. |

Hugging Face's GitHub-hosted documentation and skills were accessible during this research. Direct searches of the Hugging Face Hub were unavailable in this environment, so no current Hub model or dataset recommendations or license claims have been verified here. The ScienceClaw README links to its [Hugging Face evaluation dataset](https://huggingface.co/datasets/beita6969/scienceclaw-eval), but its contents and terms were not inspected.

## Rechecking this catalog

Revisit primary READMEs and license files, check current project activity and maintenance, inspect individual skills for accuracy and security, and evaluate them on representative tasks before adoption. External URLs and popularity change; this document does not update automatically. Never install or run third-party scripts or send sensitive datasets to external services without reviewing them and obtaining appropriate authorization.
