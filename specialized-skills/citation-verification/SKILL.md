---
name: citation-verification
description: >
  Use before finalizing any manuscript, report, or literature summary that cites
  papers: verify that each reference exists and supports the claim attributed to
  it, check DOIs, detect duplicates, find retractions or corrections, and catch
  fabricated or misattributed citations. Includes an offline DOI extraction and
  de-duplication script.
license: CC-BY-4.0
---

# Citation Verification

AI-generated and hastily compiled references are often wrong in subtle ways. Verify every citation that carries a claim.

## Workflow

1. Extract identifiers. Run the offline helper to list normalized DOIs and flag duplicates in a bibliography or draft:
   `python3 specialized-skills/citation-verification/scripts/doi_tools.py references.txt`
   It does not contact the network and does not verify that a DOI exists.
2. For each reference, confirm in a primary index (publisher page, PubMed, Crossref, or the preprint server) that the paper exists, and that authors, title, year, and venue match. If you cannot access a source, say so instead of guessing.
3. Check the claim, not just the existence. Read the abstract or relevant section and confirm the paper actually reports what the text says (population, effect direction, magnitude, design).
4. Check status: look for retractions, expressions of concern, corrections, and whether a preprint has a published version that should be cited instead.
5. Assign a status to each citation:
   - **Verified**: found and supports the claim.
   - **Partial**: found, but support is weaker, narrower, or differs in detail.
   - **Unverifiable**: could not be accessed or checked.
   - **Not found**: no matching record. Treat as potentially fabricated and remove or replace it.
6. Prefer primary studies over reviews for specific numerical claims, and cite the source you actually read.
7. Fix inconsistent formatting only after verification, using the target venue's reference style.

## Deliverable

A table with reference, DOI, status, and a one-line note for each problem, and a list of changes made to the text. Never invent a DOI, page range, or author list to complete a reference.
