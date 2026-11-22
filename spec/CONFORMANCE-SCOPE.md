# Conformance scope v0.1-draft

Every report MUST identify implementation name and immutable version/commit, suite commit and profile, operating system/runtime, tests executed/skipped/failed, fixture-set version, and timestamp.

## Result vocabulary
- PASS: assertions in the named test passed.
- FAIL: at least one assertion failed.
- SKIP: not run, with reason.
- BLOCKED: environmental prerequisite unavailable.
- NOT-IMPLEMENTED: feature outside declared support.

Never convert skipped or blocked tests into passes. A suite result is bounded evidence, not a security certification.