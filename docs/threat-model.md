# Threat model (initial)

## Assets
Node identity keys, trust configuration, private case data, approval tokens, manifests, provenance records, and exported bundles.

## Adversaries
Malicious or compromised peers; malicious catalogue entries; stale publishers; compromised dependencies; operator misconfiguration.

## Test questions
- Can a peer exceed declared scope?
- Can approval be replayed or rebound to another target/input?
- Can revoked keys authenticate fresh data?
- Can private data or secrets leak through public projections/logs?
- Are malformed or oversized records bounded?
- Does partial failure leave ambiguous state?

This is an initial checklist, not a complete threat analysis. Use synthetic fixtures or explicitly authorized systems only.