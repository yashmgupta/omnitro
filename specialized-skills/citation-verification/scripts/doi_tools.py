#!/usr/bin/env python3
"""Extract, normalize, and de-duplicate DOIs from text or a bibliography (stdlib only).

This checks syntax and duplication only. A well-formed DOI does not prove that the work
exists or supports a claim; resolve each DOI through a bibliographic service.
"""

import argparse
import json
import re
import sys
from collections import Counter

DOI_PATTERN = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.IGNORECASE)
TRAILING = ".,;:)]}'\""


def normalize(doi):
    return doi.strip().rstrip(TRAILING).lower()


def extract(text):
    return [normalize(match) for match in DOI_PATTERN.findall(text)]


def report(text):
    dois = extract(text)
    counts = Counter(dois)
    return {
        "total_mentions": len(dois),
        "unique_dois": sorted(counts),
        "duplicates": {doi: n for doi, n in sorted(counts.items()) if n > 1},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input", help="text/bibliography file, or '-' for stdin")
    args = parser.parse_args(argv)
    if args.input == "-":
        text = sys.stdin.read()
    else:
        with open(args.input, encoding="utf-8") as handle:
            text = handle.read()
    json.dump(report(text), sys.stdout, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
