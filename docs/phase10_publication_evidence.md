# Phase 10 — Publication-Grade Evidence Freeze

## Correction notice — 27 September 2026

The original Phase 10 synthesis used legacy Phase 7 results whose split unit was the 12-second CSV column. A subsequent acquisition audit established that NLN-EMP vibration measurements are 60-second acquisitions stored as five consecutive 12-second columns. Phase 7A/7B was therefore rerun with reconstructed parent acquisitions kept wholly inside train, calibration, or test.

**The corrected Phase 7 values below supersede the legacy Phase 7 manuscript-facing values.** The legacy result bundle remains preserved as provenance rather than being overwritten.

## Purpose

Phase 10 consolidates the verified evidence from TrustTwin Phases 3–8 into a manuscript-facing structure. It does not introduce a new feature representation or a new diagnostic model.

## Core scientific story

TrustTwin's experimental record does not support a single numeric "trust score." Different failure modes break different indicators:

1. operating-speed shift can make predictive OOD evidence falsely flag known faults;
2. severe sensor corruption can create confidently wrong diagnoses;
3. temperature scaling/absolute confidence thresholds can fail under operating shift and can produce saturated confidence scales in-domain;
4. paired explanation instability can be informative offline, while explanation prototypes fail as runtime gates;
5. conformal prediction can provide an in-domain abstention mechanism, but it does not guarantee that every observed classifier error is routed to review.

The resulting contribution is therefore a hierarchical trust architecture:

> operating-domain support → sensor health → predictive novelty/OOD → diagnostic model → split-conformal prediction set → GREEN / AMBER / RED → human authority.

## Publication-level findings

### Representation robustness

Phase 5A: across ten Random-Forest seeds, the order-envelope representation achieved mean seed-level balanced accuracy **0.680**, compared with **0.309** for the fixed-Hz baseline.

Phase 5B: under multi-condition source-trace resampling, mean balanced accuracy was **0.650** versus **0.514**. The order-envelope advantage was strongest at 50% and 75%, while the 100% held-speed mean remained weak at approximately **0.496**.

Phase 5C: complete condition holdout produced mean recall **0.763** for order-envelope versus **0.530** for fixed-Hz. Bearing families transferred strongly; healthy and impeller remained condition-dependent.

### Sensor degradation

Phase 3C clean balanced accuracy was **0.818**. Gaussian 10 dB corruption reduced it to **0.345**, while mean classifier confidence increased from **0.472** to **0.520**.

This is direct evidence that predictive confidence cannot substitute for a sensor-health gate.

### Explanation stability

Phase 3E explanation-instability error AUROC reached **1.000** under Gaussian 10 dB and approximately **0.952** under random dropout.

Phases 3F–3G then rejected explanation prototypes as runtime gates. Explanation stability is therefore retained as offline robustness evidence, not a deployment trust score.

### OOD and operating-condition shift

Phase 4A, with operating speeds represented, produced predictive-entropy mean AUROC **0.997** with mean known false-alarm rate about **3.5%**.

Phase 4B added unseen operating speed. Predictive-entropy mean AUROC fell to **0.660**, while the known unseen-speed false-alarm rate rose to about **89.2%**.

This contrast is the empirical reason the domain-support check precedes predictive novelty/OOD evidence.

### Multimodal fusion

Phase 6A mean balanced accuracy:

- vibration only: **0.648**;
- current only: **0.222**;
- equal late fusion: **0.469**.

The original multimodal-improvement hypothesis is not supported in this design.

### Calibration and conformal abstention — corrected parent-acquisition split

The correction reconstructs **224 complete 60-second parent acquisitions** from five-column groups, retains **1,120 complete 12-second chunks**, and excludes **9 trailing incomplete chunks**.

Corrected Phase 7A:
- raw RF mean test BAcc **0.996**;
- raw mean NLL **0.112**;
- raw mean ECE **0.094**;
- temperature-scaled mean NLL **0.00835**;
- temperature-scaled mean ECE **0.00337**.

Temperature scaling therefore improves average in-domain calibration metrics after the correction. However, three of five fitted temperatures remain at the lower search boundary near 0.05, the calibrated confidence scale remains highly saturated, and calibration-derived target coverages do not reproduce the requested test coverage. The manuscript must therefore describe **unstable/saturated selective confidence**, not blanket in-domain temperature-scaling failure.

Corrected Phase 7B global LAC at 95% nominal coverage:
- mean empirical coverage **0.955**;
- minimum replicate coverage **0.931**;
- mean review rate **0.0458**;
- mean set size **0.959**;
- mean singleton accuracy **0.999**;
- five observed base-classifier errors, of which **3/5** were routed to review.

The previous claim that all observed errors were caught by review is withdrawn.

Global LAC at the pre-specified 99% point achieved mean empirical coverage **0.988**, mean review rate **0.0240**, and routed all five observed base errors to review. It is reported for completeness rather than silently replacing the previously selected 95% candidate.

### Phase 3A acquisition-group audit

The Phase 3A held-out test speed was already independent from training, so the audit concerns the internal train/calibration split among familiar speeds. After grouping sibling columns by reconstructed parent acquisition:

- held-out 50%: raw BAcc **0.667**, raw NLL **1.379**, temperature-scaled NLL **5.835**;
- held-out 75%: raw BAcc **0.842**, raw NLL **0.972**, temperature-scaled NLL **1.272**;
- held-out 100%: raw BAcc **0.564**, raw NLL **1.482**, temperature-scaled NLL **5.388**.

Thus the original conclusion that ordinary temperature scaling and absolute confidence thresholds fail to transfer safely under unseen-speed shift survives the grouping correction and is strengthened with respect to NLL.

### Independent hydraulic replication

Phase 8A mean balanced accuracy:
- cooler condition: **1.000**;
- pump leakage: **0.978**;
- accumulator pressure: **0.847**;
- valve condition: **0.441**.

Mean review rates:
- cooler: **4.55%**;
- pump leakage: **5.10%**;
- accumulator: **55.79%**;
- valve: **99.52%**.

The weak valve task remains important evidence: the conformal layer does not repair the classifier; it becomes highly conservative and routes almost all cases to review.

## Recommended contribution statement

> TrustTwin introduces and empirically motivates a hierarchical trust layer for industrial diagnostic decision support that separates operating-domain support, sensor-health evidence, predictive novelty and conformal uncertainty before allowing a diagnosis to proceed. Across controlled sensor degradation, operating shift, unknown-fault, condition-holdout and independent hydraulic replication experiments, the constituent trust signals fail under different regimes, supporting explicit reason-coded abstention and human review rather than a single opaque trust score.

## Claims excluded from the manuscript

Do not claim:
- safety certification;
- universal 95% conformal coverage;
- zero-error operation;
- universal OOD detection;
- that 95% LAC catches every error;
- direct cross-machine transfer of the Motor-2 classifier;
- causal explanations;
- autonomous maintenance decision-making;
- that the dashboard itself is a complete industrial digital twin.
