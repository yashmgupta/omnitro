---
name: sequencing-qc-alignment
description: >
  Use for raw sequencing data handling: FASTQ quality control, adapter and
  quality trimming, contamination screening, read alignment or pseudoalignment,
  BAM or CRAM processing, duplicate marking, coverage and mapping metrics,
  reference genome and annotation selection, and MultiQC-style reporting.
license: CC-BY-4.0
---

# Sequencing QC and Alignment

## Workflow

1. Confirm what was sequenced: assay, library type, strandedness, read length, single or paired end, UMIs or barcodes, and platform. Verify FASTQ pairing and file integrity (checksums, read counts per mate).
2. Run read-level QC (base quality, per-base content, adapter content, duplication, overrepresented sequences) and aggregate across samples so outliers are visible. Judge warnings against the assay: some flags are expected for RNA-seq, amplicons, or bisulfite data.
3. Trim adapters and low-quality ends only when QC indicates it, and keep the parameters. Aggressive trimming can harm some assays.
4. Screen for contamination and sample identity problems (other species, adapters, rRNA, PhiX, or unexpected genotypes), especially for low-input or pooled data.
5. Select the reference deliberately: assembly version, patch level, whether alt contigs and decoys are included, and an annotation release matching the assembly. Use the same reference everywhere and record it.
6. Pick an aligner or quantifier suited to the data (splice-aware for RNA, bisulfite-aware for methylation, long-read-aware for long reads). Retain the command line and software versions.
7. Post-alignment, sort and index, mark or remove duplicates as appropriate to the assay (not blindly for RNA-seq), and compute mapping rate, insert size, coverage uniformity, and on-target rates.
8. Define pass and fail criteria before looking at downstream results, and document excluded samples with reasons.
9. Keep raw data immutable, and store large files outside version control.

## Deliverable

A per-sample QC table, reference and tool versions, exact commands, flagged samples and decisions, and aggregated QC report. See `reproducible-workflows` for pipeline capture and `genomic-coordinates` for build and coordinate pitfalls.
