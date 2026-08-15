"""Claims workflow transformer — EOB and Coverage (CARIN BB)."""

import uuid
from .base_transformer import BaseTransformer


class ClaimsTransformer(BaseTransformer):
    workflow_family = "claims"

    def preprocess(self, raw_data: dict) -> dict:
        claims = raw_data.get("claims", [])
        return {"claims": [c for c in claims if c.get("TOTAL_CLAIM_COST", 0) >= 0]}

    def transform_fm(self, raw_data: dict) -> dict:
        fm_records = []
        for claim in raw_data["claims"]:
            fm_records.append({
                "claim_id": claim.get("Id", str(uuid.uuid4())),
                "member_id": claim.get("PATIENT", ""),
                "service_date": claim.get("START", ""),
                "paid_amount": claim.get("TOTAL_CLAIM_COST", 0),
                "status": "active",
            })
        return {"claims_fm": fm_records}

    def transform_sam(self, fm_data: dict) -> dict:
        sam_records = []
        for fm in fm_data["claims_fm"]:
            sam_records.append({
                **fm,
                "profile": "http://hl7.org/fhir/us/carin-bb/StructureDefinition/C4BB-ExplanationOfBenefit",
            })
        return {"claims_sam": sam_records}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        for record in sam_data["claims_sam"]:
            resources.append({
                "resourceType": "ExplanationOfBenefit",
                "id": record["claim_id"],
                "meta": {"profile": [record["profile"]]},
                "status": "active",
                "type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type", "code": "professional"}]},
                "use": "claim",
                "patient": {"reference": f"Patient/{record['member_id']}"},
                "billablePeriod": {"start": record["service_date"]},
                "created": record["service_date"],
                "insurer": {"display": "Onyx Health Plan"},
                "provider": {"display": "Provider Network"},
                "outcome": "complete",
                "total": [{"category": {"coding": [{"code": "benefit"}]}, "amount": {"value": record["paid_amount"], "currency": "USD"}}],
            })
        return resources
