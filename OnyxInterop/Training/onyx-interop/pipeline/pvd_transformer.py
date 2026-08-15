"""Provider Directory transformer — Da Vinci Plan-Net."""

import uuid
from .base_transformer import BaseTransformer

PLANNET_PROFILES = {
    "Practitioner": "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Practitioner",
    "Organization": "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Organization",
    "Location": "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-Location",
    "PractitionerRole": "http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/plannet-PractitionerRole",
}


class PVDTransformer(BaseTransformer):
    workflow_family = "pvd"

    def preprocess(self, raw_data: dict) -> dict:
        providers = raw_data.get("providers", [])
        return {"providers": [p for p in providers if p.get("NPI")]}

    def transform_fm(self, raw_data: dict) -> dict:
        return {"pvd_fm": raw_data["providers"]}

    def transform_sam(self, fm_data: dict) -> dict:
        return {"pvd_sam": fm_data["pvd_fm"]}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        for p in sam_data["pvd_sam"]:
            npi = p.get("NPI", str(uuid.uuid4()))
            resources.append({
                "resourceType": "Practitioner",
                "id": npi,
                "meta": {"profile": [PLANNET_PROFILES["Practitioner"]]},
                "identifier": [{"system": "http://hl7.org/fhir/sid/us-npi", "value": npi}],
                "name": [{"text": p.get("PROVIDER_NAME", p.get("name", "Unknown"))}],
                "qualification": [{"code": {"text": p.get("SPECIALTY", p.get("specialty", ""))}}],
            })
            if p.get("ORG_NAME") or p.get("organization"):
                org_id = f"org-{npi}"
                resources.append({
                    "resourceType": "Organization",
                    "id": org_id,
                    "meta": {"profile": [PLANNET_PROFILES["Organization"]]},
                    "name": p.get("ORG_NAME", p.get("organization", "Unknown Org")),
                    "active": True,
                })
        return resources
