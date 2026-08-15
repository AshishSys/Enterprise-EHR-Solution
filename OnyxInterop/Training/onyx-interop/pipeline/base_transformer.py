"""Base transformer for FM → SAM → FHIR pipeline steps."""

from abc import ABC, abstractmethod
from typing import Any


class BaseTransformer(ABC):
    """Base class for workflow family transformers."""

    workflow_family: str = "base"

    @abstractmethod
    def preprocess(self, raw_data: dict) -> dict:
        """Validate and normalize raw input."""

    @abstractmethod
    def transform_fm(self, raw_data: dict) -> dict:
        """Transform raw → Foundational Marts (non-FHIR)."""

    @abstractmethod
    def transform_sam(self, fm_data: dict) -> dict:
        """Transform FM → Subject Area Marts (IG-aligned)."""

    @abstractmethod
    def to_fhir(self, sam_data: dict) -> list[dict]:
        """Transform SAM → FHIR R4 resources."""

    def run(self, raw_data: dict, path: str = "identified") -> list[dict]:
        """CMS path uses identified records; analytics path must pass de-id first."""
        staged = raw_data
        if path == "deidentified":
            from .deid_engine import DeIdentificationEngine
            from .mdm_engine import MasterDataManager
            import os

            pepper = os.environ.get("DEID_TOKEN_PEPPER")
            if not pepper:
                raise RuntimeError("DEID_TOKEN_PEPPER required for de-identified path")
            engine = DeIdentificationEngine(token_pepper=pepper)
            split = engine.split_paths(raw_data)
            staged = split["deidentified"]
            mdm = MasterDataManager()
            if "patients" in staged:
                resolved = mdm.resolve_batch("member", staged["patients"])
                staged = {**staged, "patients": resolved["golden"]}
        preprocessed = self.preprocess(staged)
        fm = self.transform_fm(preprocessed)
        sam = self.transform_sam(fm)
        return self.to_fhir(sam)
