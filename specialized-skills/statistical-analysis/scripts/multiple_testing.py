#!/usr/bin/env python3
"""Multiple-testing adjustments (Benjamini-Hochberg, Holm, Bonferroni); stdlib only."""

import argparse
import csv
import math
import sys


def _validate(pvalues):
    for p in pvalues:
        if not isinstance(p, (int, float)) or math.isnan(p) or not 0 <= p <= 1:
            raise ValueError(f"invalid p-value: {p!r}")


def bonferroni(pvalues):
    _validate(pvalues)
    m = len(pvalues)
    return [min(1.0, p * m) for p in pvalues]


def holm(pvalues):
    _validate(pvalues)
    m = len(pvalues)
    order = sorted(range(m), key=pvalues.__getitem__)
    adjusted = [0.0] * m
    running = 0.0
    for rank, index in enumerate(order):
        running = max(running, (m - rank) * pvalues[index])
        adjusted[index] = min(1.0, running)
    return adjusted


def benjamini_hochberg(pvalues):
    _validate(pvalues)
    m = len(pvalues)
    order = sorted(range(m), key=pvalues.__getitem__)
    adjusted = [0.0] * m
    running = 1.0
    for rank in range(m, 0, -1):
        index = order[rank - 1]
        running = min(running, pvalues[index] * m / rank)
        adjusted[index] = running
    return adjusted


def _read(path, column):
    handle = sys.stdin if path == "-" else open(path, newline="", encoding="utf-8")
    with handle:
        if column is None:
            return [float(line) for line in handle if line.strip()]
        return [float(row[column]) for row in csv.DictReader(handle, delimiter="\t")]


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", help="file of p-values, one per line, or '-' for stdin")
    parser.add_argument("--column", help="read this column from a tab-separated file with a header")
    args = parser.parse_args(argv)
    pvalues = _read(args.input, args.column)
    print("p\tbh\tholm\tbonferroni")
    for row in zip(pvalues, benjamini_hochberg(pvalues), holm(pvalues), bonferroni(pvalues)):
        print("\t".join(f"{value:.6g}" for value in row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
