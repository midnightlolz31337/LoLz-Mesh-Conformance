# LoLz Mesh Conformance

A public, implementation-neutral test suite for checking whether independent mesh nodes and protocols interoperate as specified.

## Mission

Turn federation claims into reproducible tests. A result applies only to the named implementation, version, suite revision, and configuration. Passing is not a general security certification.

## Current executable profile: project-manifest-v1

The first executable slice validates project manifests against a pinned snapshot of the LoLz Mesh Atlas project-manifest schema.

```bash
python -m pip install -r requirements.txt
python -m mesh_conformance.manifest fixtures/valid/manifest-minimal.json
python -m mesh_conformance.manifest fixtures/invalid/manifest-missing-id.json
python -m unittest discover -s tests -v
```

The validator checks JSON Schema Draft 2020-12 structure and URI/date formats. The schema snapshot and its upstream commit are recorded in `schemas/SCHEMA-PROVENANCE.md`. Updating the authoritative schema requires a reviewed snapshot update; test runs do not fetch a moving branch.

## Planned test domains

- Manifest parsing and schema compatibility.
- Identity and trust-root selection.
- Signature verification, key rotation, and revocation.
- Least-privilege scope enforcement.
- Approval binding to target, operation, and input digest.
- Private-to-public projection and secret-leak rejection.
- Stale, malformed, poisoned, and adversarial metadata.
- Replay, partial network failure, retry, and recovery.
- Export, import, fork, and operation without LoLz services.

These are planned domains, not implemented capabilities. The current profile does not test federation, signatures, approvals, trust-root rotation, or node independence.

## Layout

- `spec/` — normative contracts and version notes.
- `schemas/` — pinned schema snapshots and provenance.
- `fixtures/valid/` and `fixtures/invalid/` — portable test vectors.
- `mesh_conformance/` — executable validation code.
- `tests/` — automated conformance tests.
- `docs/threat-model.md` — assumptions and attacker capabilities.

## Status

EARLY IMPLEMENTATION. Manifest validation is executable and CI-tested on the declared Python matrix when the workflow passes. No mesh implementation is certified; passing this profile is not a security certification.
