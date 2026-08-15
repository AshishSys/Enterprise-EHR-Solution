"""Consumer API Lambda — SLAP/FITE proxy for API Gateway."""

import json
import os
import urllib.request


FITE_URL = os.environ.get("FITE_URL", "http://localhost:8080/fhir")
SLAP_URL = os.environ.get("SLAP_URL", "http://localhost:9000")


def validate_token(token: str) -> dict:
    req = urllib.request.Request(
        f"{SLAP_URL}/auth/introspect",
        data=json.dumps({"token": token}).encode(),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        return json.loads(resp.read())


def proxy_fhir(method: str, path: str, body: str = None, token: str = None) -> dict:
    url = f"{FITE_URL}/{path.lstrip('/')}"
    headers = {"Content-Type": "application/fhir+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, data=body.encode() if body else None, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return {"statusCode": resp.status, "body": resp.read().decode(), "headers": {"Content-Type": "application/fhir+json"}}


def handler(event, context):
    path = event.get("pathParameters", {}).get("proxy", "")
    method = event.get("httpMethod", "GET")
    body = event.get("body", "")
    headers = event.get("headers", {})
    auth = headers.get("Authorization", headers.get("authorization", ""))

    token = auth.replace("Bearer ", "") if auth.startswith("Bearer ") else None

    public_paths = ["metadata", "Practitioner", "Organization", "Location", "PractitionerRole"]
    is_public = any(path.startswith(p) for p in public_paths)

    if not is_public:
        if not token:
            return {"statusCode": 401, "body": json.dumps({"error": "Unauthorized"})}
        introspect = validate_token(token)
        if not introspect.get("active"):
            return {"statusCode": 403, "body": json.dumps({"error": "Token inactive"})}

    try:
        result = proxy_fhir(method, path, body, token)
        return result
    except Exception as e:
        return {"statusCode": 502, "body": json.dumps({"error": str(e)})}
