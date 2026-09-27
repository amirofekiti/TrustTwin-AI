# Verified results summary

Original result-bundle SHA-256 values are recorded in `provenance/result_bundles.sha256`.

> **Methodological correction, 27 September 2026:** the legacy Phase 7 train/calibration/test split treated 12-second CSV columns as independent source traces. The NLN-EMP data documentation states that each 60-second vibration acquisition is stored as five consecutive 12-second columns. Phase 7A/7B was therefore rerun with reconstructed 60-second parent acquisitions kept intact. The corrected Phase 7 values below supersede the legacy Phase 7 manuscript claims; the legacy bundle remains archived as provenance.

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

## Calibration and conformal abstention — acquisition-grouped correction

The corrected Phase 7 rerun reconstructs one 60-second parent acquisition as five consecutive 12-second CSV columns from the same source file. It retains **224 complete parent acquisitions / 1,120 complete 12-second chunks** and excludes **9 trailing incomplete chunks**.

- **Phase 7A corrected:** raw RF mean test BAcc ≈ **0.996**. Temperature scaling improves aggregate in-domain NLL/ECE, but three of five fitted temperatures remain at the lower search boundary near 0.05 and calibration-derived selective-coverage targets do not transfer exactly to test coverage. The corrected conclusion is therefore **unstable/saturated confidence scaling and poor selective-coverage control**, not blanket in-domain calibration failure.
- **Phase 7B corrected:** global 95% LAC mean empirical coverage ≈ **0.955**, mean review rate ≈ **0.0458**, mean singleton accuracy ≈ **0.999**, and minimum replicate coverage ≈ **0.931**. Five base-classifier errors were observed; **3/5** were routed to review and **2/5** were issued as incorrect singletons. The previous claim that all observed errors were caught by review is withdrawn.
- For completeness, the pre-specified global 99% LAC operating point achieved mean empirical coverage ≈ **0.988**, mean review rate ≈ **0.0240**, and routed all five observed base errors to review. This is reported as an evaluated operating point, not retroactively substituted for the previously selected 95% candidate.

The Phase 3A held-speed calibration analysis was also audited with parent-acquisition grouping inside the familiar-speed train/calibration pool. Its central conclusion survives: calibration/absolute confidence thresholds learned under familiar speeds do not transfer reliably to unseen-speed data, and temperature scaling worsened NLL on all three corrected held-speed folds.

## Independent replication

Phase 8A UCI hydraulic mean BAcc:

- cooler condition **1.000**;
- pump leakage **0.978**;
- accumulator pressure **0.847**;
- valve condition **0.441**.

Conformal review rates were approximately 4.55%, 5.10%, 55.79% and 99.52%, respectively.
