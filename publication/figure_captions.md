# Draft figure captions

**Figure 1. Representation robustness across held operating speeds (Phase 5B).** Mean balanced accuracy across ten source-trace resamples for the frozen order-envelope representation and fixed-Hz baseline. The order-envelope representation retains a clear advantage at 50% and 75%, while both representations remain weak at 100%.

**Figure 2. Leave-one-condition-out generalisation by fault family (Phase 5C).** Mean recall across completely held-out source conditions. Bearing families transfer strongly under the order-envelope representation, whereas healthy/impeller separation remains condition-dependent.

**Figure 3. Diagnostic performance and model confidence under synthetic sensor corruption (Phase 3C).** Severe random dropout and Gaussian 10 dB noise substantially reduce balanced accuracy. Under Gaussian 10 dB, mean confidence increases despite diagnostic collapse, showing that confidence cannot substitute for sensor-health evidence.

**Figure 4. Explanation-instability and low-confidence error detection under degradation (Phase 3E).** Paired explanation instability becomes highly informative under severe random dropout and Gaussian 10 dB noise. This supports explanation stability as an offline robustness diagnostic rather than a runtime trust gate.

**Figure 5. Acquisition-grouped predictive OOD evidence inside represented operating conditions versus joint operating-condition shift (corrected Phases 4A–4B).** Under represented speeds, predictive entropy remains useful on average but is heterogeneous across held-out fault families (mean AUROC 0.940; worst-family 0.735). Under simultaneous fault-family and operating-speed shift, mean entropy AUROC is 0.656 and the mean known unseen-speed false-alarm rate is 0.787, rising to 0.955 at held-out 100% speed.

**Figure 6. Unsynchronised multimodal late fusion (Phase 6A).** Equal late fusion of vibration and one phase-current channel underperforms vibration alone; the multimodal-improvement hypothesis is therefore not supported in this design.

**Figure 7. Acquisition-grouped global split-conformal coverage and review rate (corrected Phase 7B).** Parent 60-second acquisitions are kept intact across train, calibration and test. Global 95% LAC achieves mean empirical coverage 0.955 and mean review rate 0.0458 across five splits; mean singleton accuracy is 0.999, but two of five erroneous segment predictions remain incorrect singleton decisions. Those five erroneous segments arise from only two parent acquisitions. A separate acquisition-level sensitivity analysis produces mean 95% coverage 0.975 and review 0.025 but contains no acquisition-level base errors.

**Figure 8a. Independent UCI hydraulic diagnostic replication (Phase 8A).** Diagnostic competence varies substantially across targets, from perfect cooler classification to a weak valve classifier.

**Figure 8b. Independent UCI hydraulic conformal review burden (Phase 8A).** Review burden rises sharply as the underlying diagnostic task becomes less reliable, with the weak valve task routed almost entirely to review. A separate block-level sensitivity analysis retains the same qualitative ordering.
