"""CMS-0057 Payer-to-Payer workflow transformer."""

import uuid
from .base_transformer import BaseTransformer


class CMS0057Transformer(BaseTransformer):
    workflow_family = "cms0057"

    def preprocess(self, raw_data: dict) -> dict:
        members = raw_data.get("members", [])
        return {"members": [m for m in members if m.get("consent_status") == "opt_in"]}

    def transform_fm(self, raw_data: dict) -> dict:
        return {"cms0057_fm": raw_data["members"]}

    def transform_sam(self, fm_data: dict) -> dict:
        return {"cms0057_sam": fm_data["cms0057_fm"]}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        for member in sam_data["cms0057_sam"]:
            mid = member.get("member_id", str(uuid.uuid4()))
            resources.append({
                "resourceType": "Patient",
                "id": mid,
                "meta": {"profile": ["http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/pdex-patient"]},
                "identifier": [{"value": mid}],
                "name": [{"family": member.get("last_name", ""), "given": [member.get("first_name", "")]}],
                "birthDate": member.get("birth_date", ""),
                "gender": member.get("gender", "unknown"),
            })
            resources.append({
                "resourceType": "Coverage",
                "id": f"coverage-{mid}",
                "meta": {"profile": ["http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/pdex-coverage"]},
                "status": "active",
                "beneficiary": {"reference": f"Patient/{mid}"},
                "payor": [{"display": "Onyx Health Plan"}],
            })
        return resources
