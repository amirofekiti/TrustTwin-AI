# Phase 9C — TrustTwin Digital Twin Trust Console

This demonstrator is a **local research application** for the frozen TrustTwin architecture.

It is not a live industrial control system and it is not a claim of production deployment.

## Run

From the repository root:

```bash
python demo/server.py
```

Open:

```text
http://127.0.0.1:8000
```

No web-framework dependency is required. The server uses Python's standard library and imports the repository's actual `trusttwin.decision_engine`.

## What the interface shows

- digital-twin / machine context;
- operating-domain status;
- sensor-health status;
- known-domain OOD / novelty status;
- base diagnosis;
- conformal prediction set;
- GREEN / AMBER / RED decision;
- reason codes;
- human-review requirement;
- illustrative class probabilities;
- research provenance note;
- local audit trail.

## Important boundary

The included scenarios are **simulated demonstrator inputs**. Their probability vectors are illustrative and must not be presented as raw experimental traces.

The research notes shown beside each scenario are based on the verified experimental findings recorded in the repository.

## Policy mapping

The browser posts evidence to `POST /api/decision`. The Python server constructs `TrustTwinInput` and calls the same `decide()` function used by the Phase 9A decision engine.

Therefore, the web demonstrator does not maintain a separate hidden trust-score algorithm.

## Example states

- GREEN: supported domain + healthy sensor + known/OOD-pass + singleton conformal set.
- AMBER: upstream gates pass but the conformal set contains multiple classes.
- RED: unsupported domain, degraded/unknown sensor status, novel/unknown OOD state, empty conformal set, or a pipeline inconsistency.

Autonomous maintenance remains disabled in every state.
