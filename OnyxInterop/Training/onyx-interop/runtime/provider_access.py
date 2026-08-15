#!/usr/bin/env python3
"""
Provider Access API — CMS-0057
Attribution-based bulk export with patient opt-out enforcement.
"""

import json
import uuid
import csv
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs


class AttributionStore:
    """Member-provider attribution with opt-out tracking."""

    def __init__(self, data_dir: str = None):
        self.attributions = {}  # {provider_tin: [member_ids]}
        self.opt_outs = set()
        self.groups = {}
        if data_dir:
            self._load_from_csv(data_dir)

    def _load_from_csv(self, data_dir: str):
        paa_dir = Path(data_dir)
        members_file = paa_dir / "CPCDS_Members.csv"
        practitioners_file = paa_dir / "Practitioners.csv"

        if members_file.exists():
            with open(members_file) as f:
                for row in csv.DictReader(f):
                    member_id = row.get("MemberId", row.get("member_id", ""))
                    provider_npi = row.get("AttributionNPI", row.get("attribution_npi", ""))
                    opt_out = row.get("OptOut", "false").lower() == "true"
                    if opt_out:
                        self.opt_outs.add(member_id)
                    if provider_npi:
                        self.attributions.setdefault(provider_npi, []).append(member_id)

        if practitioners_file.exists():
            with open(practitioners_file) as f:
                for row in csv.DictReader(f):
                    npi = row.get("NPI", "")
                    if npi in self.attributions:
                        group_id = f"group-{npi}"
                        members = [m for m in self.attributions[npi] if m not in self.opt_outs]
                        self.groups[group_id] = {
                            "resourceType": "Group",
                            "id": group_id,
                            "type": "person",
                            "actual": True,
                            "name": f"Attributed members for NPI {npi}",
                            "member": [{"entity": {"reference": f"Patient/{m}"}} for m in members],
                            "characteristic": [{
                                "code": {"coding": [{"system": "http://hl7.org/fhir/us/davinci-pdex/StructureDefinition/group-attribution", "code": "attributed"}]},
                                "valueReference": {"reference": f"Practitioner/{npi}"}
                            }]
                        }

    def get_group(self, group_id: str) -> dict:
        return self.groups.get(group_id)

    def get_attributed_members(self, provider_npi: str) -> list[str]:
        members = self.attributions.get(provider_npi, [])
        return [m for m in members if m not in self.opt_outs]

    def is_opted_out(self, member_id: str) -> bool:
        return member_id in self.opt_outs


class ProviderAccessHandler(BaseHTTPRequestHandler):
    store = None
    fhir_store = None

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip('/')

        if path == '/fhir/Group' or path == '/Group':
            groups = list(self.store.groups.values())
            self._respond_json(200, self._bundle(groups))

        elif '/Group/' in path and '/$export' in path:
            group_id = path.split('/Group/')[1].split('/')[0]
            self._handle_group_export(group_id)

        elif '/Group/' in path:
            group_id = path.split('/Group/')[1].split('/')[0]
            group = self.store.get_group(group_id)
            if group:
                self._respond_json(200, group)
            else:
                self._respond_json(404, {"error": "Group not found"})

        elif path == '/health':
            self._respond_json(200, {"status": "healthy", "groups": len(self.store.groups)})

        else:
            self._respond_json(404, {"error": f"Unknown endpoint: {path}"})

    def _handle_group_export(self, group_id: str):
        group = self.store.get_group(group_id)
        if not group:
            self._respond_json(404, {"error": "Group not found"})
            return

        output = []
        if self.fhir_store:
            for member in group.get("member", []):
                ref = member.get("entity", {}).get("reference", "")
                if ref.startswith("Patient/"):
                    pid = ref.split("/")[1]
                    for rtype, resources in self.fhir_store.resources.items():
                        for rid, resource in resources.items():
                            subject = resource.get("subject", resource.get("patient", {}))
                            if isinstance(subject, dict) and subject.get("reference") == ref:
                                output.append({"type": rtype, "url": f"Patient/{pid}/{rtype}/{rid}.ndjson"})

        response = {
            "transactionTime": datetime.now(timezone.utc).isoformat(),
            "request": f"/fhir/Group/{group_id}/$export",
            "requiresAccessToken": True,
            "output": output,
            "error": []
        }
        self._respond_json(202, response)

    def _bundle(self, resources: list) -> dict:
        return {
            "resourceType": "Bundle",
            "type": "searchset",
            "total": len(resources),
            "entry": [{"resource": r} for r in resources]
        }

    def _respond_json(self, code: int, body: dict):
        self.send_response(code)
        self.send_header('Content-Type', 'application/fhir+json')
        self.end_headers()
        self.wfile.write(json.dumps(body, indent=2).encode())


def start_server(data_dir: str = None, port: int = 9003):
    store = AttributionStore(data_dir)
    ProviderAccessHandler.store = store
    print(f"Provider Access API on port {port} — {len(store.groups)} attribution groups")
    server = HTTPServer(('0.0.0.0', port), ProviderAccessHandler)
    server.serve_forever()


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=9003)
    parser.add_argument("--data", default="../PAA+")
    args = parser.parse_args()
    start_server(args.data, args.port)
