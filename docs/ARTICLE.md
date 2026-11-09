# Turn Any AI Into a Careful Research Assistant with Omnitro

Most AI assistants are fluent but not careful. They invent citations, skip power calculations, and treat 5,000 cells from one donor as 5,000 replicates. **Omnitro** is an open, tool-agnostic set of 45 "skills" (plain Markdown files) that tell an AI how a careful biomedical researcher works.

It covers literature search, study design, statistics, RNA-seq, single-cell, GWAS, proteomics, CRISPR screens, scientific writing, peer review, ethics and more. Seven tiny Python helpers (power calculation, multiple-testing correction, VCF checks, DOI checks) run with no installs.

Repo: https://github.com/yashmgupta/omnitro (CC-BY-4.0). It is independent of Biomni and Stanford. It is research support, not clinical advice.

## How it works

Each skill is a `SKILL.md` file with a trigger-rich description, a workflow, pitfalls and a deliverable. `AGENTS.md` holds the global rules (never fabricate results or citations, state limits). `INDEX.md`, `skills-index.json` and `llms.txt` list everything so an AI can pick the right skill.

## Three ways to use it

### 1. An AI that can open links or read files (Claude Code, Copilot, Codex, or a chat with browsing)

Clone it, or just share the link:

> Read https://github.com/yashmgupta/omnitro, starting with AGENTS.md and INDEX.md. Follow those rules for this conversation and load the matching SKILL.md before each task.

If it can't open links, give it the raw file URL (https://raw.githubusercontent.com/yashmgupta/omnitro/main/AGENTS.md) or paste the file.

### 2. A chat app without file access (ChatGPT, Claude, Gemini)

Paste `AGENTS.md` into Custom Instructions, a Project or a custom GPT. Then paste or upload only the 2-3 `SKILL.md` files you need, because context is limited.

### 3. Agent tools with skill folders

Copy the skill folders you want into your tool's skills directory (check its docs for the location). Keep each folder intact so the scripts stay with their skill.

## Prompt examples

**Sample size**
> Using the statistical-power skill: I want to compare tumor volume between two mouse groups. I expect a 30% difference, SD about 25%. State your assumptions, give n per group with 15% dropout, and show a sensitivity range.

**Literature without made-up papers**
> Use search-strategy then literature-review. Build a PubMed search for CAR-T resistance in solid tumors. If you can't search, say so and give me the strings to run myself. Don't cite anything you haven't verified.

**Check a reference list**
> Use citation-verification on this bibliography. Label each entry Verified, Partial, Unverifiable or Not found, and don't invent DOIs. [paste list]

**RNA-seq**
> Use rna-seq-analysis. Here are my metadata columns and design: [paste]. Is batch confounded with condition? Propose the model formula, filtering rule and QC plots before any testing.

**Single-cell replication**
> Use single-cell-analysis. I have 5,000 cells per group but one donor per group. What can I and can't I conclude?

**Writing and figures**
> Use scientific-writing and scientific-visualization. Draft a Results paragraph using only the numbers below, with placeholders for anything missing, and suggest a colorblind-safe figure. [paste results]

**Reviewing and revising**
> Use manuscript-revision. Turn these reviewer comments into a numbered point-by-point response plan. Mark which need new analyses. [paste comments]

**Ethics check**
> Use research-ethics-biosafety. I plan to use patient RNA-seq from a controlled-access cohort. List the approvals, data-use constraints and re-identification risks to check.

**Chain skills**
> Plan a study on gut microbiome and immunotherapy response using study-design, statistical-power, metagenomics-microbiome, then reporting-guidelines. Give one checklist.

## Tips

- Name the skill in your prompt. It is the most reliable way to trigger it.
- Ask the AI to list its assumptions and what it could not verify.
- Keep patient-identifiable and unpublished data out of third-party chat tools unless your policy allows it.
- Use the helper scripts only where the AI can execute code, and check the numbers yourself.
- Skills guide behavior. They don't make a model more accurate, so review important outputs.

## Contribute

Add a skill folder, list it in `docs/categories.json`, run `python3 scripts/build_index.py`, and open a pull request.
