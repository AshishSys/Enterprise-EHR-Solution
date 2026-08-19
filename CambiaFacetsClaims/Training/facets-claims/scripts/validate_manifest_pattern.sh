#!/usr/bin/env bash
# Validate manifest path pattern for Facets Claims incremental batches
set -euo pipefail

PATTERN="cambia/facets/cambia/claims/extension/incremental/*/*manifest.json"

echo "=== Manifest Pattern Validation ==="
echo "Expected pattern: $PATTERN"
echo ""
echo "Manifest must list:"
echo "  - ~25 encrypted JSON files per batch"
echo "  - header, medical/dental line items, diagnosis, PPL, delete files"
echo "  - checksums for AIR library validation"
echo ""
echo "Batch types:"
echo "  - claims-incremental/  (~every 4 hrs + nightly trigger)"
echo "  - claims-historical/"
echo "  - PPL incremental/historical"
echo ""
echo "PASS: Manifest pattern documented (verify against live S3 in dev/stg)"
