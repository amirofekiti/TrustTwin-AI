# RESS submission positioning

Target journal: **Reliability Engineering & System Safety**

## Positioning

The manuscript is framed as a reliability and diagnostic decision-support contribution rather than as a new fault-classification backbone.

Recent RESS studies provide two close comparison points:

- Azari et al. (2025), *Self-adaptive fault diagnosis for unseen working conditions based on digital twins and domain generalization* (RESS 254, 110560), focuses on adaptation and generalisation to unseen operating conditions.
- Lin et al. (2026), *An uncertainty-guided contrastive learning method for OOD detection in trustworthy fault diagnosis* (RESS 267, 111967), focuses on improving uncertainty-aware ID/OOD separability.

TrustTwin is complementary: it tests when distinct reliability evidence channels themselves become unreliable under sensor degradation, operating-condition shift and fault novelty, then uses those observed failure modes to define an ordered abstention and human-review policy.

## Submission-facing scientific boundaries

- Operating-domain support is supplied from known operating metadata/support bounds in the present experiments; a separately learned domain-support classifier is not validated.
- H5 is reported as **not supported by the tested combinations**, not universally disproved.
- The 95% conformal headline remains valid after correcting the finite-sample rank rule.
- 99% acquisition-level and 99% Mondrian conformal settings are vacuous full-set cases under the canonical finite-sample rule and are not treated as informative operating points.
- Phase 7 in-domain estimates apply to 45/48 speed-by-condition cells; three sparse cells comprising five complete acquisitions are training-only.
