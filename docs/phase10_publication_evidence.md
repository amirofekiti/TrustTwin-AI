# Phase 10 — Publication-Grade Evidence Freeze

## Purpose

Phase 10 consolidates the **verified, frozen evidence** from TrustTwin Phases 3–8 into a manuscript-facing structure. It does not introduce a new model, alter thresholds, or create a new performance claim.

The publication figures were regenerated directly from the CSV outputs stored inside the original result bundles.

## Core scientific story

TrustTwin's experimental record does not support a single numeric "trust score." Different failure modes break different indicators:

1. operating-speed shift can make predictive OOD evidence falsely flag known faults;
2. severe sensor corruption can create confidently wrong diagnoses;
3. ordinary temperature scaling can fail under shift or become degenerate on an almost-error-free calibration set;
4. paired explanation instability can be informative offline, while explanation prototypes fail as runtime gates;
5. conformal prediction provides a useful in-domain abstention mechanism, but its validity remains conditional on its assumptions.

The resulting contribution is therefore a **hierarchical trust architecture**:

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

Phases 3F–3G then rejected explanation prototypes as runtime gates. Explanation stability is therefore retained as **offline robustness evidence**, not a deployment trust score.

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

### Calibration and conformal abstention

Phase 7A temperature scaling became degenerate in an almost error-free calibration regime. Intended 50–90% selective thresholds all collapsed to **1.0**, with approximately **99.1%** test coverage at every requested target.

Phase 7B global LAC at 95% nominal coverage achieved:

- empirical coverage **0.956**;
- review rate **0.0436**;
- singleton accuracy **1.000** in the observed splits;
- both observed base-classifier errors routed to review.

Only two base errors occurred, so this is not a zero-error guarantee.

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

The weak valve task is important evidence: the conformal layer does not repair the classifier; it becomes highly conservative and routes almost all cases to review.

## Recommended contribution statement

> TrustTwin introduces and empirically motivates a hierarchical trust layer for industrial digital-twin fault diagnosis that separates operating-domain support, sensor-health evidence, predictive novelty and conformal uncertainty before allowing a diagnosis to proceed. Across controlled sensor-degradation, operating-shift, unknown-fault, condition-holdout and independent hydraulic replication experiments, the constituent trust signals are shown to fail under different regimes, supporting explicit reason-coded abstention and human review rather than a single opaque trust score.

## Claims excluded from the manuscript

Do not claim:

- safety certification;
- universal 95% conformal coverage;
- zero-error operation;
- universal OOD detection;
- direct cross-machine transfer of the Motor-2 classifier;
- causal explanations;
- autonomous maintenance decision-making;
- that the dashboard itself is a complete industrial digital twin.
