"""MDM golden-record tests."""

from pipeline.mdm_engine import MasterDataManager


def test_deterministic_member_match():
    mdm = MasterDataManager()
    first = {"tokenized_member_id": "tok_a", "source_system": "ehr_fhir", "updated_at": "2026-01-01"}
    second = {"tokenized_member_id": "tok_a", "source_system": "claims", "updated_at": "2026-06-01"}
    result = mdm.resolve_batch("member", [first, second])
    assert len(result["golden"]) == 1
    assert result["match_audit"][1]["method"] == "deterministic"
    assert result["match_audit"][1]["confidence"] == 1.0


def test_survivorship_prefers_ehr_then_recency():
    mdm = MasterDataManager()
    records = [
        {"tokenized_member_id": "tok_b", "source_system": "claims", "coverage_status": "old", "updated_at": "2025-01-01"},
        {"tokenized_member_id": "tok_b", "source_system": "ehr_fhir", "coverage_status": "active", "updated_at": "2026-08-01"},
    ]
    result = mdm.resolve_batch("member", records)
    gold = result["golden"][0]
    assert gold["source_system"] == "ehr_fhir"
    assert gold["coverage_status"] == "active"


def test_quality_report_has_no_phi_fields():
    mdm = MasterDataManager()
    mdm.resolve_batch("member", [{"tokenized_member_id": "tok_c", "source_system": "pvd"}])
    report = mdm.quality_report()
    assert "crosswalk_rows" in report
    assert "name" not in report
    assert "ssn" not in report
