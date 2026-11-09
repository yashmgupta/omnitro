---
name: research-model-selection
description: Find, compare, or assess AI models and datasets for biomedical research, including Hugging Face model cards, datasets, model evaluation, and responsible research use. Use for selecting biological language models or open research resources.
license: CC-BY-4.0
---

# Biomedical Research Model and Dataset Selection

## Workflow

1. Define the research task, organism and data modality, expected inputs and outputs, intended deployment, compute budget, and evaluation criteria. Specify whether the goal is discovery, prediction, or a clinically validated application.
2. Search available model and dataset catalogs only with tools actually available. Hugging Face model and dataset cards can describe intended use, training data, evaluation, limitations, and licensing; a catalog listing or popularity does not prove suitability or open licensing.
3. Verify identifiers, revisions, authorship, access controls, model and dataset licenses, and restrictions separately. Check whether weights, training code, data, and commercial use are available; distinguish these from an open-source repository.
4. Compare evaluation datasets and metrics, independent validation, data leakage risks, demographic or biological coverage, uncertainty, and out-of-distribution performance. Do not compare benchmark numbers as equivalent unless tasks and evaluation conditions match.
5. Before loading or sending data to an external provider, check authorization, privacy, terms, and applicable institutional controls. Assess untrusted model artifacts and dependencies according to the host's security policies.

## Deliverable

Provide a comparison table with verified sources, task fit, resource and access requirements, license information, and limitations. Mark unknowns and the date of verification. Do not fabricate benchmark scores, access status, or model capabilities; if catalog access is unavailable, provide a selection checklist instead.
