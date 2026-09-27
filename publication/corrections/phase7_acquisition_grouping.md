# Phase 7 parent-acquisition grouping correction

## Why the correction was required

The legacy Phase 7 split unit was the 12-second CSV column. The NLN-EMP source documentation states that one vibration measurement lasts 60 seconds and is stored as five consecutive 12-second columns. The CSV header audit showed sequential integer column labels rather than explicit parent-acquisition identifiers.

The corrected analysis reconstructs the physical parent group as:

`acquisition_index = floor(trace_column / 5)`

within each source CSV.

Trailing groups containing fewer than five 12-second chunks are excluded rather than treated as complete acquisitions.

## Corrected dataset accounting

- 224 complete reconstructed 60-second acquisitions;
- 1,120 complete 12-second chunks retained;
- 9 trailing incomplete chunks excluded;
- source-condition cells with fewer than three complete acquisitions are training-only;
- each split replicate contains 55 calibration acquisitions and 55 test acquisitions, equivalent to 275 12-second chunks in each partition.

All sibling chunks from one reconstructed acquisition remain in exactly one partition.

## Corrected Phase 7A

Across five acquisition-grouped splits:

| State | Mean BAcc | Mean NLL | Mean ECE | Mean confidence |
| --- | ---: | ---: | ---: | ---: |
| Raw RF | 0.996 | 0.112 | 0.094 | 0.904 |
| Temperature scaled | 0.996 | 0.008 | 0.003 | 0.996 |

Temperature scaling improves the aggregate in-domain calibration metrics, so the legacy statement that it simply “degenerates in-domain” is too strong. However, three of five fitted temperatures remain at the lower search boundary near 0.05, confidence remains highly saturated, and requested calibration coverages do not map cleanly to test coverage. Temperature-scaled confidence is therefore not retained as the runtime selective-prediction gate.

## Corrected Phase 7B

Global LAC:

| Nominal | Mean coverage | Minimum coverage | Mean review | Mean set size | Mean singleton accuracy | Base errors |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 0.90 | 0.885 | 0.778 | 0.115 | 0.885 | 1.000 | 5 |
| 0.95 | 0.955 | 0.931 | 0.0458 | 0.959 | 0.999 | 5 |
| 0.99 | 0.988 | 0.967 | 0.0240 | 1.001 | 1.000 | 5 |

At the corrected 95% point, three of five observed base errors are routed to review; two are issued as incorrect singletons. The previous 2/2 perfect error-review statement is withdrawn.

At the pre-specified 99% point, all five observed base errors are routed to review. This is reported for completeness and must not be presented as a post-hoc replacement chosen solely because it catches all errors.

## Phase 3A audit

Phase 3A already held the complete test speed outside model development. The correction therefore concerns only the familiar-speed train/calibration partition.

After parent-acquisition grouping:

| Held speed | Raw BAcc | Raw NLL | Temp-scaled NLL | Fitted T |
| ---: | ---: | ---: | ---: | ---: |
| 50% | 0.667 | 1.379 | 5.835 | 0.050 |
| 75% | 0.842 | 0.972 | 1.272 | 0.050 |
| 100% | 0.564 | 1.482 | 5.388 | 0.050 |

The conclusion that calibration and absolute confidence thresholds learned under familiar speeds do not transfer reliably under unseen-speed shift survives the correction.

## Provenance rule

The legacy Phase 7 result bundle remains part of the project history. It is not deleted or overwritten. Corrected acquisition-grouped results supersede it for future manuscript claims.
