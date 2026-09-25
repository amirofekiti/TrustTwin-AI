# Verified results summary

Original result-bundle SHA-256 values are recorded in `provenance/result_bundles.sha256`.

## Diagnostic representation

- **Phase 2C:** frozen 11-class order-envelope RF mean BAcc ≈ **0.699**.
- **Phase 5A:** across 10 RF seeds, order-envelope mean BAcc ≈ **0.680** vs fixed-Hz ≈ **0.309**; all 30 paired comparisons favoured order-envelope.
- **Phase 5B:** multi-condition resampling mean BAcc ≈ **0.650** vs fixed-Hz ≈ **0.514**; 29/30 matched folds favoured order-envelope, with one tie.
- **Phase 5C:** complete condition-holdout mean recall ≈ **0.763** vs fixed-Hz ≈ **0.530**.

## Sensor degradation

Phase 3C clean BAcc ≈ **0.818**; Gaussian 10 dB BAcc ≈ **0.345** while mean confidence increased. Confidence alone is therefore not a sensor-health mechanism.

## Explainability

Phase 3E explanation-instability error AUROC reached ≈ **0.952** for random dropout and **1.000** for Gaussian 10 dB. Phases 3F–3G rejected explanation prototypes as runtime gates.

## OOD

- **Phase 4A:** predictive-entropy mean AUROC ≈ **0.997** inside represented operating conditions.
- **Phase 4B:** under unknown fault + unseen speed, entropy mean AUROC ≈ **0.660** with ≈ **89.2%** false alarms on known unseen-speed traces.

## Multimodal late fusion

Phase 6A: vibration-only BAcc ≈ **0.648**, current-only ≈ **0.222**, equal late fusion ≈ **0.469**.

## Calibration and conformal abstention

- **Phase 7A:** temperature scaling became degenerate and intended selective thresholds collapsed.
- **Phase 7B:** global 95% LAC empirical coverage ≈ **95.64%**, review rate ≈ **4.36%**, and both observed base errors were routed to review.

## Independent replication

Phase 8A UCI hydraulic mean BAcc:

- cooler condition **1.000**;
- pump leakage **0.978**;
- accumulator pressure **0.847**;
- valve condition **0.441**.

Conformal review rates were approximately 4.55%, 5.10%, 55.79% and 99.52%, respectively.
