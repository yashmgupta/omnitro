#!/usr/bin/env python3
"""Write a JSON provenance snapshot: interpreter, platform, packages, git commit, input checksums."""

import argparse
import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone
from importlib import metadata


def sha256(path, chunk=1 << 20):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(chunk), b""):
            digest.update(block)
    return digest.hexdigest()


def git_commit(cwd="."):
    try:
        out = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=cwd, capture_output=True, text=True, check=True
        )
        return out.stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def snapshot(inputs=(), cwd="."):
    packages = {}
    for dist in metadata.distributions():
        name = dist.metadata["Name"]
        if name:
            packages[name.lower()] = dist.version
    return {
        "created_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "python": sys.version,
        "platform": platform.platform(),
        "git_commit": git_commit(cwd),
        "packages": dict(sorted(packages.items())),
        "inputs": {path: sha256(path) for path in inputs},
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--inputs", nargs="*", default=[], help="input files to checksum")
    parser.add_argument("--output", default="-", help="output JSON path (default: stdout)")
    args = parser.parse_args(argv)
    text = json.dumps(snapshot(args.inputs), indent=2)
    if args.output == "-":
        print(text)
    else:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
