# Phase 4 acquisition-grouping correction

## Trigger

The v0.2 manuscript audit found that Phase 4A separated known-class data at the 12-second segment level even though NLN-EMP vibration measurements are 60-second acquisitions stored as five consecutive 12-second columns. Phase 4B kept the unseen test speed completely outside development, but its familiar-speed training/calibration partition was also segment-level.

Parent groups were reconstructed as `source_member + floor(trace_column/5)`.

## Corrected Phase 4A

The held-out fault family remains completely excluded from fitting. Known classes are now split by parent acquisition, stratified by fault family. Exact legacy speed-cell stratification is not retained because several representative Phase 2C speed/class cells contain fewer than three reconstructed acquisitions; physical group integrity takes priority.

Predictive entropy:
- mean AUROC: **0.940**
- median AUROC: **0.984**
- worst-family AUROC: **0.735**
- mean known-test false-alarm rate: **0.044**
- mean OOD detection at the locked threshold: **0.605**
- worst OOD detection: **0.000**

Low maximum probability mean AUROC: **0.944**.

The legacy Phase 4A mean AUROC **0.997** is superseded for manuscript claims.

## Corrected Phase 4B familiar-speed calibration audit

The unseen speed remains completely held out from fitting and calibration. Only the familiar-speed training/calibration partition is changed to parent-acquisition grouping.

Predictive entropy:
- mean AUROC across 33 folds: **0.656**
- mean known unseen-speed false-alarm rate: **0.787**
- mean OOD detection: **0.909**
- worst AUROC: **0.144**

Mean known false-alarm rate by held-out speed:
- 50%: **0.742**
- 75%: **0.665**
- 100%: **0.955**

The prior manuscript values 0.660 / 0.892 remain part of the historical record but are superseded for future manuscript claims. The prior statement that mean FAR reaches 1.000 for both 50% and 100% held-out speeds is no longer valid after the acquisition-grouped calibration audit.

## Consequence

OOD evidence remains part of TrustTwin only as conditional evidence. The corrected results support the need to check operating-domain support before novelty interpretation, but they do not justify describing predictive entropy as an almost universally strong held-fault detector even when operating speeds are represented.
