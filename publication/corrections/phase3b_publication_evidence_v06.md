# Phase 3B publication evidence summary

## Scope

Phase 3B evaluated whether a generic scalar combination of four segment-level trust signals improved error ranking under held-speed shift. The signals were low predictive confidence, predictive entropy, Random-Forest/Extra-Trees Jensen-Shannon disagreement, and predicted-class nearest-neighbour distance after train-fitted standardisation and PCA. The nested meta-model was trained only on familiar-speed inner data and evaluated on the untouched outer held-out speed.

This analysis originated as an exploratory pre-publication branch and was not included in the initial public result-bundle SHA ledger. This file records the exact summary metrics used in manuscript v0.6; it does not claim to replace unavailable row-level archival outputs.

## Reported metrics

| Metric | 50% held out | 75% held out | 100% held out | Mean |
| --- | ---: | ---: | ---: | ---: |
| Low-confidence error AUROC | 0.476 | 0.861 | 0.911 | 0.749 |
| Predictive-entropy error AUROC | - | - | - | 0.719 |
| Four-signal meta-trust error AUROC | 0.486 | 0.717 | 0.903 | 0.702 |
| RF/ET disagreement error AUROC | 0.637 | 0.443 | 0.392 | - |

## Interpretation boundary

No tested generic scalar combination consistently improved the low-confidence baseline across the three held-speed regimes. The exact full uncertainty-OOD-explanation combination proposed in H5 was not established as one deployable model.
