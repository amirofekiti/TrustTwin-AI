# Claim-to-evidence matrix

| Claim / hypothesis | Disposition | Evidence | Boundary |
| --- | --- | --- | --- |
| H1: vibration + electrical improves over best single modality | **Not supported** | Phase 6A | Unsynchronised condition-level late fusion |
| H2: ordinary calibration/UQ robustly improves reliability under corruption/shift | **Not supported in original simple form** | Phase 3A acquisition-group audit; corrected Phase 7A | Temperature scaling is unreliable under unseen-speed shift; in-domain scaling improves aggregate calibration metrics but produces saturated/unstable confidence scales and poor selective-coverage control |
| H3: uncertainty/OOD abstention can reduce unsafe accepted predictions | **Conditionally supported** | Phases 4A, 4B, corrected 7B, 8A | Separate domain support from fault novelty; 95% LAC does not catch every observed error |
| H4: explanation stability can signal failures under degradation | **Supported offline** | Phase 3E | Runtime prototypes failed in 3F–3G |
| H5: one combined trust score outperforms predictive probability | **Not supported** | Phase 3B exploratory, Phase 3F | Final architecture keeps trust signals explicit |
| Order-envelope improves held-speed robustness | **Supported for tested scope** | 2C, 5A, 5B, 5C | Not universal across every implementation |
| Predictive entropy detects unknown faults | **Only inside represented operation** | 4A positive, 4B negative | Not a global OOD rule |
| Global 95% LAC is useful as in-domain review gate | **Candidate, with corrected limitation** | Corrected 7B, 8A | Approximately nominal marginal coverage in tested in-domain splits; two corrected Phase 7 errors were issued as incorrect singletons |
| Workflow replicates on a second hydraulic dataset | **Supported as workflow replication** | 8A | Not direct classifier transfer |
