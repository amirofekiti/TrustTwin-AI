# Claim-to-evidence matrix

| Claim / hypothesis | Disposition | Evidence | Boundary |
| --- | --- | --- | --- |
| H1: vibration + electrical improves over best single modality | **Not supported** | Phase 6A | Unsynchronised condition-level late fusion |
| H2: ordinary calibration/UQ robustly improves reliability under corruption/shift | **Not supported in original simple form** | Phase 3A acquisition-group audit; corrected Phase 7A | Temperature scaling is unreliable under unseen-speed shift; in-domain scaling improves aggregate calibration metrics but produces saturated/unstable confidence scales and poor selective-coverage control |
| H3: uncertainty/OOD abstention can reduce unreliable accepted predictions | **Conditionally supported, weaker after acquisition correction** | Corrected Phase 4A, Phase 4B audit, corrected 7B, Phase 7 acquisition-level sensitivity, 8A | OOD ranking is useful but heterogeneous even inside represented operation; operating support must precede novelty interpretation; conformal review does not catch every segment-level error |
| H4: explanation stability can signal failures under degradation | **Supported offline** | Phase 3E | Runtime prototypes failed in 3F–3G |
| H5: one combined trust score outperforms predictive probability | **Not supported by the tested combinations** | Phase 3B exploratory; Phase 3F | No tested scalar combination consistently improved the probability baseline; the exact full uncertainty–OOD–explanation combination was not established as one deployable model |
| Order-envelope improves held-speed robustness | **Supported for tested scope** | 2C, 5A, 5B, 5C | Not universal across every implementation |
| Predictive entropy detects unknown faults | **Useful but heterogeneous within represented operation** | Corrected 4A; 4B negative under joint shift | Corrected 4A mean AUROC ≈0.940, worst ≈0.735; thresholded detection can fail for some held-out families; not a global OOD rule |
| Global 95% LAC is useful as in-domain review gate | **Candidate, with corrected limitation** | Corrected 7B + acquisition-level sensitivity + 8A | Approximately nominal empirical coverage in tested in-domain analyses; segment-level errors are clustered by acquisition and two corrected segment errors were incorrect singletons |
| Workflow replicates on a second hydraulic dataset | **Supported as workflow replication** | 8A + block-level sensitivity | Not direct classifier transfer; block-level sensitivity uses fresh splits and is not a replacement headline benchmark |
