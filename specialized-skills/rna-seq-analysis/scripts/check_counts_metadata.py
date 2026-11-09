#!/usr/bin/env python3
"""Check that an RNA-seq count matrix and sample metadata agree (stdlib only).

Counts: delimited text with feature IDs in the first column and samples as the other
columns (header required). Metadata: delimited text with a sample ID column.
Files ending in .csv are comma-separated; everything else is tab-separated.
"""

import argparse
import csv
import json
import sys
from collections import Counter


def _delimiter(path):
    return "," if path.lower().endswith(".csv") else "\t"


def check(counts_rows, metadata_rows, sample_col="sample"):
    header = counts_rows[0]
    samples = header[1:]
    problems = []
    duplicates = sorted(s for s, n in Counter(samples).items() if n > 1)
    if duplicates:
        problems.append(f"duplicate count-matrix sample IDs: {duplicates}")
    if metadata_rows and sample_col not in metadata_rows[0]:
        raise ValueError(f"metadata has no column {sample_col!r}")
    meta_ids = [row[sample_col] for row in metadata_rows]
    meta_duplicates = sorted(s for s, n in Counter(meta_ids).items() if n > 1)
    if meta_duplicates:
        problems.append(f"duplicate metadata sample IDs: {meta_duplicates}")
    only_counts = sorted(set(samples) - set(meta_ids))
    only_meta = sorted(set(meta_ids) - set(samples))
    if only_counts:
        problems.append(f"samples only in counts: {only_counts}")
    if only_meta:
        problems.append(f"samples only in metadata: {only_meta}")
    library_sizes = [0.0] * len(samples)
    non_integer = negative = zero_features = 0
    for row in counts_rows[1:]:
        if len(row) != len(header):
            raise ValueError(f"row {row[0]!r} has {len(row) - 1} values; expected {len(samples)}")
        values = [float(value) for value in row[1:]]
        zero_features += all(value == 0 for value in values)
        for i, value in enumerate(values):
            negative += value < 0
            non_integer += value != int(value)
            library_sizes[i] += value
    if negative:
        problems.append(f"{negative} negative values")
    if non_integer:
        problems.append(f"{non_integer} non-integer values; count-based models expect raw counts")
    return {
        "n_samples": len(samples),
        "n_features": len(counts_rows) - 1,
        "zero_count_features": zero_features,
        "library_sizes": dict(zip(samples, library_sizes)),
        "problems": problems,
        "ok": not problems,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("counts")
    parser.add_argument("metadata")
    parser.add_argument("--sample-col", default="sample")
    args = parser.parse_args(argv)
    with open(args.counts, newline="", encoding="utf-8") as handle:
        counts_rows = list(csv.reader(handle, delimiter=_delimiter(args.counts)))
    with open(args.metadata, newline="", encoding="utf-8") as handle:
        metadata_rows = list(csv.DictReader(handle, delimiter=_delimiter(args.metadata)))
    result = check(counts_rows, metadata_rows, args.sample_col)
    json.dump(result, sys.stdout, indent=2)
    print()
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
