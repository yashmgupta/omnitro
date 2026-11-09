#!/usr/bin/env python3
"""Neutralize spreadsheet formula injection in CSV cells (stdlib only).

Cells that begin with =, +, -, @, tab, or carriage return and are not plain numbers
get a leading apostrophe so spreadsheet programs treat them as text.
"""

import argparse
import csv
import sys

TRIGGERS = ("=", "+", "-", "@", "\t", "\r")


def _is_number(text):
    try:
        float(text)
    except ValueError:
        return False
    return True


def sanitize_cell(value):
    text = "" if value is None else str(value)
    if text.startswith(TRIGGERS) and not _is_number(text):
        return "'" + text
    return text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("input")
    parser.add_argument("output")
    args = parser.parse_args(argv)
    with open(args.input, newline="", encoding="utf-8") as src, open(
        args.output, "w", newline="", encoding="utf-8"
    ) as dst:
        writer = csv.writer(dst)
        for row in csv.reader(src):
            writer.writerow([sanitize_cell(cell) for cell in row])
    return 0


if __name__ == "__main__":
    sys.exit(main())
