#!/usr/bin/env python3
"""FSI converter — Parquet/CSV to NDJSON for Firely bulk $import."""

import json
import sys
from pathlib import Path


def convert_to_ndjson(input_dir: str, output_dir: str):
    """Convert extracted CSV/JSON files to NDJSON format for FSI."""
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    converted = 0
    for f in input_path.rglob("*.json"):
        if f.name.startswith("bundle"):
            with open(f) as fh:
                bundle = json.load(fh)
            rtype = None
            out_file = None
            for entry in bundle.get("entry", []):
                resource = entry.get("resource", {})
                rtype = resource.get("resourceType")
                if not rtype:
                    continue
                out_file = output_path / f"{rtype}.ndjson"
                with open(out_file, "a") as out:
                    out.write(json.dumps(resource) + "\n")
                converted += 1

    print(f"Converted {converted} resources to NDJSON in {output_path}")
    return converted


if __name__ == "__main__":
    input_dir = sys.argv[1] if len(sys.argv) > 1 else "/data/input"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "/data/output"
    convert_to_ndjson(input_dir, output_dir)
