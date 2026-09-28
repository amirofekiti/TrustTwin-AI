# Phase 7 conformal finite-sample quantile correction

## Date

28 September 2026

## Issue

The earlier implementation capped the split-conformal order-statistic rank to the calibration-set size. The canonical finite-sample rule is:

`k = ceil((n + 1) * (1 - alpha))`.

When `k > n`, the conformal threshold is treated as infinite and the prediction set is the full label space. The rank is not capped to `n`.

## Consequence for the headline results

The primary segment-level global LAC analysis has 275 calibration segments. Its 90%, 95% and 99% ranks are all supported by the available calibration size.

Therefore the headline global 95% result remains unchanged:
- mean empirical coverage: 0.955;
- minimum replicate coverage: 0.931;
- mean review rate: 0.0458.

The acquisition-level sensitivity uses 55 calibration acquisitions:
- 90%: rank 51, valid finite threshold;
- 95%: rank 54, valid finite threshold;
- 99%: rank 56 > 55, therefore full six-class set and 100% review.

The headline acquisition-level 95% sensitivity also remains unchanged:
- mean empirical coverage: 0.975;
- mean review rate: 0.0255.

## Mondrian 99%

Every class-specific calibration sample in the six-family Phase 7 analysis is smaller than the count needed for a finite 99% class-conditional threshold. Under the canonical rule, 99% Mondrian therefore returns the full six-class set and 100% review.

The 90% and 95% Mondrian settings are not affected by this finite-sample issue.

## Sparse-cell disclosure

The six-family acquisition-grouped benchmark contains 48 speed-by-source-condition cells. Forty-five can contribute independent train/calibration/test acquisitions. Three are training-only:

- 50% / impeller 1 — 2 complete acquisitions;
- 50% / soft foot 1 — 2 complete acquisitions;
- 100% / impeller 2 — 1 complete acquisition.

## Scientific interpretation

No headline 95% conformal claim changes. The correction affects only requested coverage levels for which the available calibration sample cannot support a finite canonical order statistic. Those cases are now reported as degenerate full-set cases rather than ordinary finite-threshold results.
