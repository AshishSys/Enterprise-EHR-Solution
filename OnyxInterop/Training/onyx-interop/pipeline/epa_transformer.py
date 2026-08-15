"""ePA workflow transformer — Da Vinci CRD/DTR/PAS."""

import uuid
from datetime import datetime, timezone
from .base_transformer import BaseTransformer


class EPATransformer(BaseTransformer):
    workflow_family = "epa"

    def preprocess(self, raw_data: dict) -> dict:
        requests = raw_data.get("pa_requests", [])
        return {"pa_requests": requests}

    def transform_fm(self, raw_data: dict) -> dict:
        return {"epa_fm": raw_data["pa_requests"]}

    def transform_sam(self, fm_data: dict) -> dict:
        return {"epa_sam": fm_data["epa_fm"]}

    def to_fhir(self, sam_data: dict) -> list[dict]:
        resources = []
        for req in sam_data["epa_sam"]:
            auth_id = req.get("auth_id", str(uuid.uuid4()))
            resources.append({
                "resourceType": "Claim",
                "id": auth_id,
                "meta": {"profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claim"]},
                "status": "active",
                "type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type", "code": "professional"}]},
                "use": "preauthorization",
                "patient": {"reference": f"Patient/{req.get('member_id', 'unknown')}"},
                "created": req.get("request_date", datetime.now(timezone.utc).isoformat()),
                "insurer": {"display": "Onyx Health Plan"},
                "priority": {"coding": [{"code": req.get("priority", "normal")}]},
            })
            if req.get("status") in ("approved", "denied", "pending"):
                resources.append({
                    "resourceType": "ClaimResponse",
                    "id": f"response-{auth_id}",
                    "meta": {"profile": ["http://hl7.org/fhir/us/davinci-pas/StructureDefinition/profile-claimresponse"]},
                    "status": "active",
                    "type": {"coding": [{"system": "http://terminology.hl7.org/CodeSystem/claim-type", "code": "professional"}]},
                    "use": "preauthorization",
                    "patient": {"reference": f"Patient/{req.get('member_id', 'unknown')}"},
                    "created": req.get("decision_date", datetime.now(timezone.utc).isoformat()),
                    "outcome": "complete",
                    "disposition": req.get("decision_reason", f"Prior authorization {req.get('status', 'pending')}"),
                    "preAuthRef": auth_id,
                })
        return resources
