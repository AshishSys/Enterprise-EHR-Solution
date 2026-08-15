#!/usr/bin/env python3
"""Validate FHIR output against US Core and CARIN BB profile requirements."""

import json
import sys
from pathlib import Path

REQUIRED_PROFILES = {
    "Patient": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"],
    "Encounter": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter"],
    "Condition": [
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition",
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition-encounter-diagnosis",
    ],
    "Observation": [
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab",
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-vital-signs",
        "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-clinical-result",
    ],
    "MedicationRequest": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest"],
    "Procedure": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure"],
    "AllergyIntolerance": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance"],
    "ExplanationOfBenefit": [
        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit",
        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Inpatient-Institutional",
        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Professional-NonClinician",
        "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit-Outpatient-Institutional",
    ],
}

REQUIRED_FIELDS = {
    "Patient": ["identifier", "name", "gender", "birthDate"],
    "Encounter": ["status", "class", "subject"],
    "Condition": ["clinicalStatus", "code", "subject"],
    "ExplanationOfBenefit": ["status", "type", "patient", "billablePeriod"],
}


def validate_resource(resource: dict) -> list[str]:
    errors = []
    rtype = resource.get("resourceType")
    if not rtype:
        return ["Missing resourceType"]

    for field in REQUIRED_FIELDS.get(rtype, []):
        if field not in resource:
            errors.append(f"{rtype}/{resource.get('id', '?')}: missing required field '{field}'")

    meta = resource.get("meta", {})
    profiles = meta.get("profile", [])
    expected_list = REQUIRED_PROFILES.get(rtype, [])
    if expected_list and profiles and not any(p in profiles for p in expected_list):
        errors.append(
            f"{rtype}/{resource.get('id', '?')}: profile mismatch "
            f"(expected one of {expected_list}, got {profiles})"
        )

    return errors


def validate_ndjson_dir(ndjson_dir: Path) -> dict:
    results = {"total": 0, "errors": [], "by_type": {}}

    for ndjson_file in sorted(ndjson_dir.glob("*.ndjson")):
        rtype = ndjson_file.stem
        count = 0
        type_errors = []

        with open(ndjson_file) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                resource = json.loads(line)
                count += 1
                type_errors.extend(validate_resource(resource))

        results["by_type"][rtype] = {"count": count, "errors": len(type_errors)}
        results["total"] += count
        results["errors"].extend(type_errors)

    return results


def main():
    ndjson_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "../../fhir_output/ndjson")
    if not ndjson_dir.exists():
        ndjson_dir = Path(__file__).resolve().parents[2] / ".." / "fhir_output" / "ndjson"
    ndjson_dir = ndjson_dir.resolve()

    if not ndjson_dir.exists():
        print(f"ERROR: NDJSON directory not found: {ndjson_dir}")
        sys.exit(1)

    print(f"Validating FHIR output in: {ndjson_dir}")
    results = validate_ndjson_dir(ndjson_dir)

    print(f"\nTotal resources: {results['total']}")
    for rtype, info in sorted(results["by_type"].items()):
        status = "OK" if info["errors"] == 0 else f"{info['errors']} errors"
        print(f"  {rtype}: {info['count']} resources — {status}")

    if results["errors"]:
        print(f"\nValidation FAILED with {len(results['errors'])} errors:")
        for err in results["errors"][:20]:
            print(f"  - {err}")
        if len(results["errors"]) > 20:
            print(f"  ... and {len(results['errors']) - 20} more")
        sys.exit(1)

    print("\nValidation PASSED — all resources meet US Core / CARIN BB requirements")
    sys.exit(0)


if __name__ == "__main__":
    main()
