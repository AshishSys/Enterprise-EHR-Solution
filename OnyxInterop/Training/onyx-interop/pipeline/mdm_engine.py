"""Healthcare MDM golden-record resolution (AHIMA / ISO 8000 / HL7 PA).

Operates on de-identified or tokenized keys. Never stores raw PHI in the
crosswalk. Match confidence is logged as a score only.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "mdm" / "mdm_rules.yaml"


class MdmConfigError(RuntimeError):
    """Raised when MDM rules cannot be loaded."""


class MasterDataManager:
    """Deterministic + probabilistic match with survivorship."""

    def __init__(self, config_path: Path | None = None):
        self.config_path = config_path or CONFIG_PATH
        self.config = self._load()
        self.crosswalk: list[dict] = []

    def _load(self) -> dict:
        if not self.config_path.exists():
            raise MdmConfigError(f"MDM rules missing: {self.config_path}")
        with open(self.config_path) as f:
            return yaml.safe_load(f)

    def entity_types(self) -> list[str]:
        return list(self.config.get("entities", {}).keys())

    def _deterministic_key(self, record: dict, fields: list[str]) -> str | None:
        parts = []
        for field in fields:
            value = record.get(field)
            if value in (None, ""):
                return None
            parts.append(str(value).strip().lower())
        return "|".join(parts)

    def match_member(self, record: dict, existing: list[dict]) -> dict:
        rules = self.config["entities"]["member"]
        for field_set in rules["match"]["deterministic"]:
            incoming = self._deterministic_key(record, field_set)
            if not incoming:
                continue
            for gold in existing:
                if self._deterministic_key(gold, field_set) == incoming:
                    return {
                        "status": "matched",
                        "method": "deterministic",
                        "confidence": 1.0,
                        "golden_id": gold.get("member_golden_id"),
                        "rule_id": "+".join(field_set),
                    }
        return {
            "status": "new",
            "method": "insert",
            "confidence": 1.0,
            "golden_id": record.get("member_golden_id") or record.get("tokenized_member_id"),
            "rule_id": "new_golden",
        }

    def apply_survivorship(self, entity: str, candidates: list[dict]) -> dict:
        """Pick winning attributes per source_priority and recency rules."""
        rules = self.config["entities"][entity]
        priority = rules.get("survivorship", {}).get("source_priority", [])
        ranked = sorted(
            candidates,
            key=lambda r: (
                priority.index(r.get("source_system", ""))
                if r.get("source_system") in priority
                else len(priority),
                str(r.get("updated_at", "")),
            ),
        )
        winner = dict(ranked[0]) if ranked else {}
        recency_fields = rules.get("survivorship", {}).get("recency_wins", [])
        by_recency = sorted(candidates, key=lambda r: str(r.get("updated_at", "")), reverse=True)
        if by_recency:
            newest = by_recency[0]
            for field in recency_fields:
                if newest.get(field) not in (None, ""):
                    winner[field] = newest[field]
        winner["_mdm_survivorship"] = True
        return winner

    def resolve_batch(self, entity: str, records: list[dict]) -> dict:
        golden: list[dict] = []
        matches: list[dict] = []
        for record in records:
            if entity == "member":
                result = self.match_member(record, golden)
            else:
                result = {
                    "status": "new",
                    "method": "insert",
                    "confidence": 1.0,
                    "golden_id": record.get(f"{entity}_golden_id"),
                    "rule_id": "passthrough",
                }
            enriched = dict(record)
            enriched[f"{entity}_golden_id"] = result["golden_id"]
            if result["status"] == "new" and result["golden_id"]:
                golden.append(enriched)
            elif result["status"] == "matched":
                peers = [g for g in golden if g.get(f"{entity}_golden_id") == result["golden_id"]]
                peers.append(enriched)
                merged = self.apply_survivorship(entity, peers) if entity in self.config["entities"] else enriched
                golden[:] = [g for g in golden if g.get(f"{entity}_golden_id") != result["golden_id"]]
                golden.append(merged)
            matches.append({
                "entity_type": entity,
                "golden_id": result["golden_id"],
                "method": result["method"],
                "confidence": result["confidence"],
                "rule_id": result["rule_id"],
            })
            self.crosswalk.append({
                "entity_type": entity,
                "source_system": record.get("source_system", "unknown"),
                "source_key_token": record.get("tokenized_member_id") or record.get("Id"),
                "golden_id": result["golden_id"],
                "confidence": result["confidence"],
                "rule_id": result["rule_id"],
            })
        if golden:
            golden = [self.apply_survivorship(entity, [g]) if entity in self.config["entities"] else g for g in golden]
        return {"golden": golden, "match_audit": matches}

    def quality_report(self) -> dict[str, Any]:
        goldens = [c["golden_id"] for c in self.crosswalk if c.get("golden_id")]
        return {
            "crosswalk_rows": len(self.crosswalk),
            "unique_goldens": len(set(goldens)),
            "duplicate_golden_keys": len(goldens) - len(set(goldens)),
            "gates": self.config.get("quality_gates", []),
        }
