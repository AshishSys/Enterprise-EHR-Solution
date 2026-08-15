"""HIPAA Safe Harbor + Expert Determination de-identification gate.

Identified PHI stays on the CMS API path (SLAP-scoped). Analytics, Fabric,
AI observability, and logs receive only de-identified records.
Never logs raw field values.
"""

from __future__ import annotations

import hashlib
import hmac
import re
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "deid" / "safe_harbor.yaml"

# HMAC pepper must come from a secret store in production (dbutils.secrets / SM).
# Empty pepper fails closed so tokens are never derived from a default key.
_TOKEN_PEPPER_ENV = "DEID_TOKEN_PEPPER"


class DeidConfigError(RuntimeError):
    """Raised when de-id configuration or secrets are missing."""


class DeIdentificationEngine:
    """Applies 45 CFR 164.514 Safe Harbor rules to record dicts."""

    def __init__(self, config_path: Path | None = None, token_pepper: str | None = None):
        self.config_path = config_path or CONFIG_PATH
        self.config = self._load_config()
        self.token_pepper = token_pepper
        self._field_actions = self._index_field_actions()

    def _load_config(self) -> dict:
        if not self.config_path.exists():
            raise DeidConfigError(f"De-id config missing: {self.config_path}")
        with open(self.config_path) as f:
            return yaml.safe_load(f)

    def _index_field_actions(self) -> dict[str, dict]:
        index: dict[str, dict] = {}
        for ident in self.config.get("identifiers", []):
            for field in ident.get("fields", []):
                index[field.lower()] = ident
        return index

    def _require_pepper(self) -> str:
        if self.token_pepper:
            return self.token_pepper
        raise DeidConfigError(
            "DEID_TOKEN_PEPPER is required — refuse to tokenize with an empty key"
        )

    def tokenize(self, value: str, field: str) -> str:
        pepper = self._require_pepper()
        digest = hmac.new(
            pepper.encode("utf-8"),
            f"{field}|{value}".encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()[:24]
        return f"tok_{field}_{digest}"

    def _year_only(self, value: Any) -> Any:
        if value is None or value == "":
            return value
        text = str(value)
        match = re.match(r"^(\d{4})", text)
        if not match:
            return None
        year = int(match.group(1))
        now_year = datetime.now().year
        if now_year - year >= 90:
            return "90+"
        return str(year)

    def _generalize_geo(self, field: str, value: Any) -> Any:
        if value is None:
            return None
        if field.lower() in {"zip", "postal_code"}:
            digits = re.sub(r"\D", "", str(value))
            return digits[:3] if len(digits) >= 3 else None
        if field.lower() == "state":
            return value
        return None

    def deidentify_record(self, record: dict, path: str = "deidentified") -> dict:
        """Return a copy with Safe Harbor actions applied. Does not mutate input."""
        if path == "identified":
            return dict(record)
        out: dict[str, Any] = {}
        for key, value in record.items():
            rule = self._field_actions.get(key.lower())
            if not rule:
                out[key] = value
                continue
            action = rule.get("action")
            if action == "suppress":
                continue
            if action == "year_only":
                out[key] = self._year_only(value)
            elif action == "generalize_geo":
                out[key] = self._generalize_geo(key, value)
            elif action == "tokenize" and value not in (None, ""):
                out[key] = self.tokenize(str(value), key.lower())
            else:
                out[key] = None
        out["_deid_method"] = self.config.get("method", "safe_harbor")
        out["_deid_version"] = self.config.get("version", "1.0.0")
        return out

    def deidentify_batch(self, records: list[dict], path: str = "deidentified") -> list[dict]:
        return [self.deidentify_record(r, path=path) for r in records]

    def split_paths(self, raw_data: dict, token_pepper: str | None = None) -> dict:
        """Split ingest into identified (CMS) and de-identified (analytics) copies."""
        if token_pepper:
            self.token_pepper = token_pepper
        identified: dict[str, list] = {}
        deidentified: dict[str, list] = {}
        for entity, rows in raw_data.items():
            if not isinstance(rows, list):
                continue
            identified[entity] = [dict(r) for r in rows]
            deidentified[entity] = self.deidentify_batch(rows, path="deidentified")
        return {
            "identified": identified,
            "deidentified": deidentified,
            "outputs": self.config.get("outputs", {}),
        }


def load_engine(token_pepper: str) -> DeIdentificationEngine:
    return DeIdentificationEngine(token_pepper=token_pepper)
