# Draft figure captions

**Figure 1. Representation robustness across held operating speeds (Phase 5B).** Mean balanced accuracy across ten source-trace resamples for the frozen order-envelope representation and fixed-Hz baseline. The order-envelope representation retains a clear advantage at 50% and 75%, while both representations remain weak at 100%.

**Figure 2. Leave-one-condition-out generalisation by fault family (Phase 5C).** Mean recall across completely held-out source conditions. Bearing families transfer strongly under the order-envelope representation, whereas healthy/impeller separation remains condition-dependent.

**Figure 3. Diagnostic performance and model confidence under synthetic sensor corruption (Phase 3C).** Severe random dropout and Gaussian 10 dB noise substantially reduce balanced accuracy. Under Gaussian 10 dB, mean confidence increases despite diagnostic collapse, showing that confidence cannot substitute for sensor-health evidence.

**Figure 4. Explanation-instability and low-confidence error detection under degradation (Phase 3E).** Paired explanation instability becomes highly informative under severe random dropout and Gaussian 10 dB noise. This supports explanation stability as an offline robustness diagnostic rather than a runtime trust gate.

**Figure 5. Predictive OOD evidence inside represented operating conditions versus joint operating-condition shift (Phases 4A–4B).** Unknown-fault detection is strong when operating conditions are represented but degrades sharply when operating speed is also unseen.

**Figure 6. Unsynchronised multimodal late fusion (Phase 6A).** Equal late fusion of vibration and one phase-current channel underperforms vibration alone; the multimodal-improvement hypothesis is therefore not supported in this design.

**Figure 7. Global split-conformal coverage and review rate in-domain (Phase 7B).** Empirical coverage follows the requested operating points reasonably closely. The 95% setting is retained as the candidate in-domain abstention rule, while the low error count prevents a zero-error safety claim.

**Figure 8a. Independent UCI hydraulic diagnostic replication (Phase 8A).** Diagnostic competence varies substantially across targets, from perfect cooler classification to a weak valve classifier.

**Figure 8b. Independent UCI hydraulic conformal review burden (Phase 8A).** Review burden rises sharply as the underlying diagnostic task becomes less reliable, with the weak valve task routed almost entirely to review.
