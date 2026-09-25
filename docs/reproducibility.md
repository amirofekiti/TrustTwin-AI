# Reproducibility

The public repository includes the deterministic decision engine, test suite, experiment registry, claim/evidence ledger, result-bundle SHA-256 provenance and the frozen runtime policy.

Raw datasets and large result bundles are excluded.

## Original experiment artifacts

The research archive contains the executed experiment packs and compact result summaries. Their SHA-256 identities are recorded in the provenance ledgers committed here.

This allows future archival releases to verify that a supplied phase bundle is the same artifact used to support a reported result.

## Verify result bundles

Use `provenance/result_bundles.sha256` with your preferred SHA-256 utility.

## Historical development caveat

Several experiment launchers used Windows paths from the original research environment. Those historical scripts should be archived unchanged; configurable wrappers should be treated as later reproduction tooling rather than silently replacing provenance.
