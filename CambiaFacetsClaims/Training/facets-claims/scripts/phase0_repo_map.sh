#!/usr/bin/env bash
# Phase 0: Map repos and catalog paths for Facets Claims
set -euo pipefail

echo "=== Cambia Facets Claims — Repo & Catalog Map ==="
echo ""
printf "%-30s %s\n" "REPO/SERVICE" "ROLE"
printf "%-30s %s\n" "facets-core" "Bespoke CDC: SQL Server → JSON + manifest"
printf "%-30s %s\n" "facets-infrastructure" "AWS CDC infra (Step Functions, Batch, S3)"
printf "%-30s %s\n" "ng-abacus-inbound-infra" "SFTP / connector landing zone"
printf "%-30s %s\n" "ng-orchestration-service" "Manifest-triggered workflow orchestration"
printf "%-30s %s\n" "ng-pipelines-cambia" "Bronze/silver/gold Databricks pipelines"
printf "%-30s %s\n" "ng-abacus-insights-runtime" "AIR library (encryption, SCD2, manifest)"
printf "%-30s %s\n" "ng-pipelines-onyx" "DM 2.0 → FHIR downstream"
echo ""
echo "Catalog paths:"
echo "  config/repo-rules/transporters/sftp.yaml"
echo "  config/repo-rules/transporters/orchestration.yaml"
echo "  config/repo-rules/xform/pipelines.yaml"
echo ""
echo "Tenant: cambia02"
echo "GitLab: abacusinsights/facets-integration/"
echo ""
echo "PASS: Repo map complete"
