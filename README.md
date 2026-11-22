# LoLz Mesh Conformance

A public, implementation-neutral test suite for checking whether independent mesh nodes and protocols interoperate as specified.

## Mission
Turn federation claims into reproducible tests. A result applies only to the named implementation, version, suite revision, and configuration. Passing is not a general security certification.

## Test domains
- Manifest parsing and schema compatibility.
- Identity and trust-root selection.
- Signature verification, key rotation, and revocation.
- Least-privilege scope enforcement.
- Approval binding to target, operation, and input digest.
- Private-to-public projection and secret-leak rejection.
- Stale, malformed, poisoned, and adversarial metadata.
- Replay, partial network failure, retry, and recovery.
- Export, import, fork, and operation without LoLz services.

## Layout
- spec/ — normative contracts and version notes.
- fixtures/valid/ and fixtures/invalid/ — portable test vectors.
- tests/ — executable tests (not yet implemented).
- reports/ — results with implementation/version context.
- docs/threat-model.md — assumptions and attacker capabilities.

## Status
BOOTSTRAP. This repository currently defines test scope and starter fixtures only; no implementation is certified.