# Architecture

TrustTwin is a **hierarchical evidence gate**, not a scalar trust score.

1. **Operating-condition support** — unsupported or unknown state triggers domain-shift abstention.
2. **Sensor health** — degradation evidence is assessed independently of classifier confidence.
3. **Known-domain OOD / novelty evidence** — predictive novelty is interpreted only inside supported operation.
4. **Diagnostic classifier** — produces a base fault prediction and raw class probabilities.
5. **95% global split-conformal set** — singleton may proceed; empty is RED; multi-class is AMBER/review.
6. **Human authority** — maintenance action remains a human decision.

Paired explanation stability is retained for offline robustness/audit analysis. Explanation prototypes are not runtime gates.
