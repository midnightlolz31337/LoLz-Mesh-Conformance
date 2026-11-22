import unittest
from pathlib import Path

from mesh_conformance.manifest import load_json, validate_manifest

ROOT = Path(__file__).resolve().parents[1]
VALID = ROOT / "fixtures" / "valid" / "manifest-minimal.json"
INVALID = ROOT / "fixtures" / "invalid" / "manifest-missing-id.json"


class ManifestConformanceTests(unittest.TestCase):
    def test_valid_fixture_passes(self):
        self.assertEqual(validate_manifest(load_json(VALID)), [])

    def test_missing_required_id_fails(self):
        errors = validate_manifest(load_json(INVALID))
        self.assertTrue(any("id" in error and "required" in error for error in errors))

    def test_unknown_fields_fail_closed(self):
        document = load_json(VALID)
        document["operator_override"] = True
        errors = validate_manifest(document)
        self.assertTrue(any("Additional properties are not allowed" in error for error in errors))

    def test_invalid_repository_uri_fails_format_check(self):
        document = load_json(VALID)
        document["repository"] = "not a URI"
        self.assertTrue(validate_manifest(document))

    def test_invalid_calendar_date_fails_format_check(self):
        document = load_json(VALID)
        document["updated"] = "2026-02-30"
        self.assertTrue(validate_manifest(document))

    def test_unknown_status_fails(self):
        document = load_json(VALID)
        document["status"] = "trusted"
        self.assertTrue(validate_manifest(document))


if __name__ == "__main__":
    unittest.main()
