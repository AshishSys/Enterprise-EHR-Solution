"""Formulary workflow transformer — Da Vinci Formulary IG."""

import uuid
from .base_transformer import BaseTransformer


class FormularyTransformer(BaseTransformer):
    workflow_family = "formulary"

    def preprocess(self, raw_data: dict) -> dict:
        drugs = raw_data.get("drugs", [])
        return {"drugs": drugs}

    def transform_fm(self, raw_data: dict) -> dict:
        return {"formulary_fm": raw_data["drugs"]}

    def transform_sam(self, fm_data: dict) -> dict:
        return {"formulary_sam": fm_data["formulary_fm"]}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        for drug in sam_data["formulary_sam"]:
            ndc = drug.get("NDC", str(uuid.uuid4()))
            resources.append({
                "resourceType": "MedicationKnowledge",
                "id": ndc,
                "meta": {"profile": ["http://hl7.org/fhir/us/davinci-drug-formulary/StructureDefinition/usdf-MedicationKnowledgeDefinition"]},
                "code": {"coding": [{"system": "http://hl7.org/fhir/sid/ndc", "code": ndc}]},
                "status": "active",
                "preparationInstruction": [{"text": drug.get("DRUG_NAME", drug.get("name", ""))}],
            })
        return resources
