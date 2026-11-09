#!/usr/bin/env python3
"""Summarize a VCF/VCF.gz for quick sanity checks (stdlib only).

Reports record counts, SNV/indel/other mix, transition/transversion ratio for SNVs,
FILTER values, contig naming style and header/record contig mismatches, and the
fraction of fully missing genotypes per sample. It does not validate the file format.
"""

import argparse
import gzip
import json
import sys
from collections import Counter

TRANSITIONS = {("A", "G"), ("G", "A"), ("C", "T"), ("T", "C")}
BASES = set("ACGT")


def summarize(lines):
    header_contigs = set()
    reference = None
    samples = []
    format_cache = {}
    kinds = Counter()
    filters = Counter()
    records = multiallelic = transitions = transversions = 0
    contigs = Counter()
    called = Counter()
    missing = Counter()
    for line in lines:
        line = line.rstrip("\n")
        if line.startswith("##contig=<"):
            for part in line[len("##contig=<"):-1].split(","):
                if part.startswith("ID="):
                    header_contigs.add(part[3:])
        elif line.startswith("##reference="):
            reference = line.split("=", 1)[1]
        elif line.startswith("#CHROM"):
            samples = line.split("\t")[9:]
        elif line and not line.startswith("#"):
            fields = line.split("\t")
            if len(fields) < 8:
                raise ValueError(f"malformed VCF record: {line[:60]!r}")
            records += 1
            contigs[fields[0]] += 1
            filters[fields[6]] += 1
            ref, alts = fields[3], fields[4].split(",")
            if len(alts) > 1:
                multiallelic += 1
            for alt in alts:
                if alt.startswith("<") or alt in ("*", "."):
                    kinds["symbolic_or_other"] += 1
                elif len(ref) == 1 and len(alt) == 1:
                    kinds["snv"] += 1
                    if ref.upper() in BASES and alt.upper() in BASES:
                        if (ref.upper(), alt.upper()) in TRANSITIONS:
                            transitions += 1
                        else:
                            transversions += 1
                else:
                    kinds["indel_or_mnv"] += 1
            if len(fields) > 9 and samples:
                fmt = fields[8]
                if fmt not in format_cache:
                    keys = fmt.split(":")
                    format_cache[fmt] = keys.index("GT") if "GT" in keys else None
                gt_index = format_cache[fmt]
                if gt_index is not None:
                    for sample, value in zip(samples, fields[9:]):
                        parts = value.split(":")
                        genotype = parts[gt_index] if gt_index < len(parts) else "."
                        alleles = genotype.replace("|", "/").split("/")
                        called[sample] += 1
                        if all(allele == "." for allele in alleles):
                            missing[sample] += 1
    return {
        "records": records,
        "multiallelic_records": multiallelic,
        "alt_allele_types": dict(kinds),
        "titv_ratio": round(transitions / transversions, 3) if transversions else None,
        "filters": dict(filters),
        "reference_header": reference,
        "contig_style": "chr-prefixed" if any(c.startswith("chr") for c in contigs) else "unprefixed",
        "contigs_missing_from_header": sorted(set(contigs) - header_contigs) if header_contigs else None,
        "missing_genotype_fraction": {
            sample: round(missing[sample] / called[sample], 4) for sample in samples if called[sample]
        },
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("vcf", help="VCF or VCF.gz path")
    args = parser.parse_args(argv)
    opener = gzip.open if args.vcf.endswith(".gz") else open
    with opener(args.vcf, "rt", encoding="utf-8") as handle:
        json.dump(summarize(handle), sys.stdout, indent=2)
        print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
