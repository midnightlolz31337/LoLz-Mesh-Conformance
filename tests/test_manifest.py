import unittest
from pathlib import Path

from mesh_conformance.manifest import load_json, validate_manifest

ROOT = Path(__file__).resolve().parents[1]
VALID = ROOT / "fixtures" / "valid" / "manifest-minimal.json"
INVALID = ROOT / "fixtures" / "invalid" / "manifest-missing-id.json"


class ManifestConformanceTests(unittest.TestCase):
    def setUp(self):
        self.document = load_json(VALID)

    def test_valid_fixture_passes(self):
        self.assertEqual(validate_manifest(self.document), [])

    def test_missing_required_id_fails(self):
        errors = validate_manifest(load_json(INVALID))
        self.assertTrue(any("id" in error and "required" in error for error in errors))

    def test_unknown_fields_fail_closed(self):
        self.document["operator_override"] = True
        errors = validate_manifest(self.document)
        self.assertTrue(any("Additional properties are not allowed" in error for error in errors))

    def test_invalid_calendar_date_fails_format_check(self):
        self.document["updated"] = "2026-02-30"
        self.assertTrue(validate_manifest(self.document))

    def test_unknown_status_fails(self):
        self.document["status"] = "trusted"
        self.assertTrue(validate_manifest(self.document))

    def test_non_https_repository_url_fails(self):
        self.document["repository"] = "http://example.com/project"
        self.assertTrue(validate_manifest(self.document))

    def test_repository_url_with_credentials_fails(self):
        self.document["repository"] = "https://user:secret@example.com/project"
        self.assertTrue(validate_manifest(self.document))

    def test_repository_url_with_invalid_port_fails(self):
        self.document["repository"] = "https://example.com:99999/project"
        self.assertTrue(validate_manifest(self.document))

    def test_repository_url_with_non_numeric_port_fails(self):
        self.document["repository"] = "https://example.com:abc/project"
        self.assertTrue(validate_manifest(self.document))

    def test_repository_url_with_empty_port_fails(self):
        self.document["repository"] = "https://example.com:/project"
        self.assertTrue(validate_manifest(self.document))

    def test_non_object_document_fails(self):
        self.assertTrue(validate_manifest(["not", "an", "object"]))


if __name__ == "__main__":
    unittest.main()
