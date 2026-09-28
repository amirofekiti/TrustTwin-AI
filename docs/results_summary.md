# Verified results summary

Original result-bundle SHA-256 values are recorded in `provenance/result_bundles.sha256`.

> **Methodological corrections, 27 September 2026:** the legacy Phase 7 train/calibration/test split treated 12-second CSV columns as independent source traces. Phase 7A/7B was rerun with reconstructed 60-second parent acquisitions kept intact. A subsequent audit found the same physical-independence issue in the known-class Phase 4A train/calibration/test partition and segment-level familiar-speed calibration in Phase 4B. Phase 4A was rerun with parent-acquisition-grouped known splits; Phase 4B was re-audited with parent-acquisition-grouped familiar-speed calibration. Corrected values below supersede the legacy manuscript-facing Phase 4/7 values while legacy bundles remain archived as provenance.

## Diagnostic representation

- **Phase 2C:** frozen 11-class order-envelope RF mean BAcc ≈ **0.699**.
- **Phase 5A:** across 10 RF seeds, order-envelope mean BAcc ≈ **0.680** vs fixed-Hz ≈ **0.309**; all 30 paired comparisons favoured order-envelope.
- **Phase 5B:** multi-condition resampling mean BAcc ≈ **0.650** vs fixed-Hz ≈ **0.514**; 29/30 matched folds favoured order-envelope, with one tie.
- **Phase 5C:** complete condition-holdout mean recall ≈ **0.763** vs fixed-Hz ≈ **0.530**.

## Sensor degradation

Phase 3C clean BAcc ≈ **0.818**; Gaussian 10 dB BAcc ≈ **0.345** while mean confidence increased. Confidence alone is therefore not a sensor-health mechanism.

## Explainability

Phase 3E explanation-instability error AUROC reached ≈ **0.952** for random dropout and **1.000** for Gaussian 10 dB. Phases 3F–3G rejected explanation prototypes as runtime gates.

## OOD — acquisition-grouped correction

- **Phase 4A corrected:** predictive-entropy mean AUROC ≈ **0.940**, median ≈ **0.984**, worst-family ≈ **0.735**. Mean known-test false-alarm rate ≈ **4.4%**. Calibration-locked mean OOD detection ≈ **60.5%**, with some held-out families at 0% detection. Low maximum probability mean AUROC ≈ **0.944**.
- **Phase 4B corrected familiar-speed calibration audit:** under unknown fault + unseen speed, predictive-entropy mean AUROC ≈ **0.656** with ≈ **78.7%** mean false alarms on known unseen-speed traces. Mean false-alarm rate by held-out speed: 50% ≈ **74.2%**, 75% ≈ **66.5%**, 100% ≈ **95.5%**.

The corrected evidence still supports an explicit operating-domain check before novelty/OOD interpretation, but no longer supports the legacy claim that predictive entropy is nearly universally strong for represented-speed held-fault detection.

## Multimodal late fusion

Phase 6A: vibration-only BAcc ≈ **0.648**, current-only ≈ **0.222**, equal late fusion ≈ **0.469**.

## Calibration and conformal abstention — acquisition-grouped correction

The corrected Phase 7 rerun reconstructs one 60-second parent acquisition as five consecutive 12-second CSV columns from the same source file. It retains **224 complete parent acquisitions / 1,120 complete 12-second chunks** and excludes **9 trailing incomplete chunks**.

- **Phase 7A corrected:** raw RF mean test BAcc ≈ **0.996**. Temperature scaling improves aggregate in-domain NLL/ECE, but three of five fitted temperatures remain at the lower search boundary near 0.05 and calibration-derived selective-coverage targets do not transfer exactly to test coverage. The corrected conclusion is therefore **unstable/saturated confidence scaling and poor selective-coverage control**, not blanket in-domain calibration failure.
- **Phase 7B corrected:** global 95% LAC mean empirical coverage ≈ **0.955**, mean review rate ≈ **0.0458**, mean singleton accuracy ≈ **0.999**, and minimum replicate coverage ≈ **0.931**. Five erroneous segment predictions were observed; they arose from only two parent acquisitions. **3/5** erroneous segments were routed to review and **2/5** were issued as incorrect singletons.
- **Acquisition-level sensitivity:** in a fresh five-seed sensitivity run using parent acquisitions as the conformal calibration/evaluation unit, 95% global LAC mean empirical coverage ≈ **0.975** and mean review rate ≈ **0.025** over 55 test acquisitions per split. No acquisition-level base errors occurred in those sensitivity splits, so error-interception performance cannot be inferred from that analysis.
- **Finite-sample quantile correction (28 September 2026):** conformal rank is `ceil((n+1)(1-alpha))`; when that rank exceeds the calibration-set size, the threshold is infinite and the full label set is returned rather than capping the rank. The headline global 95% segment result and 95% acquisition-level sensitivity are unchanged. Acquisition-level 99% and 99% Mondrian are full-set/100%-review cases under the canonical rule.

The Phase 3A held-speed calibration analysis was also audited with parent-acquisition grouping inside the familiar-speed train/calibration pool. Its central conclusion survives: calibration/absolute confidence thresholds learned under familiar speeds do not transfer reliably to unseen-speed data, and temperature scaling worsened NLL on all three corrected held-speed folds.

## Independent replication

Phase 8A UCI hydraulic mean BAcc:

- cooler condition **1.000**;
- pump leakage **0.978**;
- accumulator pressure **0.847**;
- valve condition **0.441**.

Original cycle-level conformal review rates were approximately 4.55%, 5.10%, 55.79% and 99.52%, respectively. A separate block-level sensitivity analysis using fresh deterministic block splits retained the qualitative pattern: cooler and pump tasks remained compact, accumulator remained less stable, and the valve task was routed entirely to review at block level.

