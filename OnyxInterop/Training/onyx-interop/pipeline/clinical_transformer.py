"""Clinical workflow transformer — US Core resources."""

import uuid
from .base_transformer import BaseTransformer

US_CORE_PROFILES = {
    "Patient": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
    "Encounter": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-encounter",
    "Condition": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition",
    "Observation": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-observation-lab",
    "MedicationRequest": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-medicationrequest",
    "Procedure": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-procedure",
    "AllergyIntolerance": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-allergyintolerance",
}


class ClinicalTransformer(BaseTransformer):
    workflow_family = "clinical"

    def preprocess(self, raw_data: dict) -> dict:
        return raw_data

    def transform_fm(self, raw_data: dict) -> dict:
        fm = {}
        for key in ["patients", "encounters", "conditions", "observations", "medications", "procedures", "allergies"]:
            if key in raw_data:
                fm[f"clinical_fm_{key}"] = raw_data[key]
        return fm

    def transform_sam(self, fm_data: dict) -> dict:
        return {k.replace("clinical_fm_", "clinical_sam_"): v for k, v in fm_data.items()}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        patients = sam_data.get("clinical_sam_patients", [])
        for p in patients:
            pid = p.get("Id", str(uuid.uuid4()))
            resources.append({
                "resourceType": "Patient",
                "id": pid,
                "meta": {"profile": [US_CORE_PROFILES["Patient"]]},
                "identifier": [{"system": "urn:oid:2.16.840.1.113883.4.1", "value": p.get("SSN", pid)}],
                "name": [{"use": "official", "family": p.get("LAST", ""), "given": [p.get("FIRST", "")]}],
                "gender": p.get("GENDER", "unknown").lower(),
                "birthDate": p.get("BIRTHDATE", ""),
            })
        return resources
