---
name: biomedical-databases
description: Find and reconcile research data from biomedical databases such as PubMed, NCBI Gene, Ensembl, UniProt, GEO, and ClinVar. Use for gene or protein identifiers, dataset discovery, accession lookup, database provenance, and cross-resource comparisons.
license: CC-BY-4.0
---

# Biomedical Database Retrieval

## Workflow

1. Define the entity, organism, research question, desired fields, and source constraints. Disambiguate common gene symbols and distinguish genes, transcripts, proteins, variants, samples, and publications.
2. Select an appropriate authoritative source and access it only through tools actually available. For example, PubMed indexes publications; GEO catalogs functional-genomics datasets; NCBI Gene and Ensembl provide gene records; UniProt provides protein records; ClinVar aggregates submitted interpretations.
3. Record the source, stable accession, species, release or retrieval date, and direct record URL when available. For identifiers that change between resources, document the mapping and report ambiguity or failed matches rather than guessing.
4. For public datasets, review study design, sample metadata, access conditions, licensing, and whether raw or processed data match the question. For ClinVar, distinguish submitted assertions, review status, conditions, and conflicts from independently validated clinical conclusions.
5. Check whether source data are current enough for the task and whether an apparent absence may reflect access, query, coverage, or version limitations.

## Deliverable

Provide a compact table of entity, accession, source, relevant observation, and caveat, with verifiable links. Never fabricate records or imply a query succeeded when it did not. Avoid transmitting sensitive or identifying data to external services without authorization.
