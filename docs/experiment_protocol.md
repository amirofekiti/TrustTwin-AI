# Experiment protocol

## Leakage control

- Never split windows from the same source trace across train and test.
- Prefer machine > run/instance > source recording > windows.
- Do not pair electrical and vibration trace indices without proven synchrony.

## Evaluation

Diagnostics: balanced accuracy, macro-F1, class recall and confusion structure.

Trust evidence: calibration metrics, selective risk/coverage, OOD AUROC/AUPRC, sensor-health detection, conformal coverage/set size/review rate, and offline explanation stability.

## Research integrity

- Preserve negative results.
- Do not promote test-set oracle analyses to deployment methods.
- Do not make causal claims from feature attribution.
- Do not call a dashboard itself a digital twin.
- Do not claim autonomous maintenance authority.
