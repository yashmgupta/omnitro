---
name: genomic-coordinates
description: >
  Use when working with positions on genomes: BED versus VCF or GFF coordinate
  conventions, 0-based and 1-based indexing, half-open intervals, chromosome
  naming (chr1 vs 1), genome build mismatches (GRCh37 vs GRCh38), liftOver,
  strand, intersecting intervals, and off-by-one bugs.
license: CC-BY-4.0
---

# Genomic Coordinates

## Workflow

1. Always record genome assembly, version, and chromosome naming style with every coordinate file. Never merge or intersect files without confirming these match.
2. Know the conventions of each format. BED uses 0-based, half-open intervals (start inclusive, end exclusive). VCF, GFF/GTF, SAM and most genome browser displays use 1-based, closed intervals. BAM stores 0-based positions internally while SAM text is 1-based. Convert explicitly when crossing formats.
3. Normalize chromosome names (for example `chr1` versus `1`, `MT` versus `chrM`) with a mapping that is checked against the reference's contig list. Silent mismatches produce empty intersections instead of errors.
4. Convert between assemblies with a dedicated tool (liftOver or similar), count and inspect unmapped and split intervals, and do not liftOver blindly when reprocessing from raw data against the target build is feasible. Report conversion loss.
5. For variants, normalize representation (left-align and trim) before comparing, and handle multiallelic records and different indel representations. Compare using the same reference FASTA.
6. Use interval libraries instead of hand-rolled loops for overlaps, and test boundaries with tiny cases that include adjacent, nested, and single-base intervals.
7. Keep strand with features, and flip coordinates and sequences together for minus-strand features.
8. Sanity-check: confirm that reference alleles in VCF match the FASTA at the stated positions, and that coordinates do not exceed contig lengths.

## Deliverable

A statement of assembly, indexing and naming conventions for every input and output, conversion steps with loss counts, and the tests used to check boundaries. Flag any file whose build could not be confirmed.
