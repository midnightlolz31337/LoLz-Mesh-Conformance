"""Validate a project manifest against the pinned Mesh Atlas schema."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from jsonschema.exceptions import SchemaError

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "project-manifest.schema.json"


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def validate_manifest(document: Any, schema: dict[str, Any] | None = None) -> list[str]:
    """Return sorted, human-readable validation errors; empty means schema-valid."""
    selected_schema = schema if schema is not None else load_json(DEFAULT_SCHEMA)
    Draft202012Validator.check_schema(selected_schema)
    validator = Draft202012Validator(selected_schema, format_checker=FormatChecker())
    errors = []
    for error in validator.iter_errors(document):
        location = ".".join(str(part) for part in error.absolute_path) or "$"
        errors.append(f"{location}: {error.message}")
    return sorted(errors)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate a LoLz Mesh project manifest.")
    parser.add_argument("manifest", type=Path, help="Path to a JSON manifest")
    parser.add_argument(
        "--schema",
        type=Path,
        default=DEFAULT_SCHEMA,
        help="Schema JSON path (defaults to the pinned project-manifest schema)",
    )
    args = parser.parse_args(argv)

    try:
        schema = load_json(args.schema)
        document = load_json(args.manifest)
        errors = validate_manifest(document, schema)
    except (OSError, json.JSONDecodeError, SchemaError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        return 1

    print("PASS: manifest conforms to the pinned project-manifest schema")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
