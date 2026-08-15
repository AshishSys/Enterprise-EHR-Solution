"""De-identification Safe Harbor tests — no PHI asserted in logs."""

from pipeline.deid_engine import DeIdentificationEngine, DeidConfigError


def _engine():
    return DeIdentificationEngine(token_pepper="unit-test-pepper-not-for-prod")


def test_suppresses_name_and_ssn():
    out = _engine().deidentify_record({"FIRST": "Ada", "SSN": "000-00-0000", "GENDER": "F"})
    assert "FIRST" not in out
    assert "SSN" not in out
    assert out["GENDER"] == "F"
    assert out["_deid_method"] == "safe_harbor"


def test_year_only_and_age_90_plus():
    out = _engine().deidentify_record({"BIRTHDATE": "1920-03-15"})
    assert out["BIRTHDATE"] == "90+"


def test_zip_generalized_to_3_digits():
    out = _engine().deidentify_record({"ZIP": "02139"})
    assert out["ZIP"] == "021"


def test_tokenize_is_stable():
    eng = _engine()
    a = eng.deidentify_record({"member_id": "M1"})
    b = eng.deidentify_record({"member_id": "M1"})
    assert a["member_id"] == b["member_id"]
    assert a["member_id"].startswith("tok_member_id_")


def test_missing_pepper_fails_closed():
    try:
        DeIdentificationEngine().tokenize("x", "member_id")
        assert False, "expected DeidConfigError"
    except DeidConfigError:
        pass


def test_split_paths_keeps_identified_copy():
    split = _engine().split_paths({"patients": [{"FIRST": "Ada", "GENDER": "F"}]})
    assert split["identified"]["patients"][0]["FIRST"] == "Ada"
    assert "FIRST" not in split["deidentified"]["patients"][0]
