# Phase 9C demonstrator

## Objective

Translate the empirically frozen TrustTwin hierarchy into a human-facing digital-twin trust console without inventing new model performance.

## Architecture

```text
Browser UI
   |
   | POST /api/decision
   v
Python demo server
   |
   v
src/trusttwin/decision_engine.py
   |
   +--> GREEN / AMBER / RED
   +--> issued diagnosis or withheld
   +--> reason codes
   +--> human-review requirement
```

## Why simulated scenarios are used first

The Phase 9C objective is **software integration and decision transparency**, not a new benchmark.

The built-in scenarios reproduce research-observed regimes while keeping the distinction clear:

- scenario evidence values and probability vectors are illustrative;
- reported phase metrics in the research-note panel come from verified experiments;
- no new accuracy claim is created by the dashboard.

## Scenario-to-evidence links

- supported BPFI / in-domain conformal: Phase 7B;
- severe sensor degradation: Phase 3C / 3D;
- unsupported operating condition: Phase 4B;
- known-domain novelty: Phase 4A;
- weak external valve classifier with broad conformal sets: Phase 8A.

## Human factors

The demonstrator intentionally avoids one percentage labelled "trust." Operators see separate evidence channels and explicit reason codes.

GREEN means "passes the current evidence gates," not "guaranteed correct."

AMBER and RED both retain human authority, with RED representing a hard abstention state.

## Future extension

A later Phase 9C.2 can replay archived experimental traces or a streaming simulator through the same API contract. That extension should not alter the frozen decision hierarchy unless new predeclared experiments justify a policy revision.
