import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trusttwin import (
    DecisionLevel,
    DomainStatus,
    OODStatus,
    SensorStatus,
    TrustTwinInput,
    decide,
)


class TrustTwinDecisionTests(unittest.TestCase):
    def test_green_singleton_supported(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.KNOWN,
            ("bearing_bpfi",), "bearing_bpfi"
        ))
        self.assertEqual(result.level, DecisionLevel.GREEN)
        self.assertEqual(result.issued_diagnosis, "bearing_bpfi")
        self.assertFalse(result.human_review_required)
        self.assertFalse(result.autonomous_maintenance_allowed)

    def test_red_domain_outside(self):
        result = decide(TrustTwinInput(
            DomainStatus.OUTSIDE, SensorStatus.HEALTHY, OODStatus.KNOWN,
            ("bearing_bpfi",)
        ))
        self.assertEqual(result.level, DecisionLevel.RED)
        self.assertIn("DOMAIN_OUTSIDE_SUPPORT", result.reason_codes)

    def test_red_sensor_degraded(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.DEGRADED, OODStatus.KNOWN,
            ("bearing_bpfi",)
        ))
        self.assertEqual(result.level, DecisionLevel.RED)

    def test_red_ood_novel(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.NOVEL,
            ("bearing_bpfi",)
        ))
        self.assertEqual(result.level, DecisionLevel.RED)

    def test_red_empty_conformal(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.KNOWN, ()
        ))
        self.assertEqual(result.reason_codes, ("CONFORMAL_EMPTY",))

    def test_amber_multiclass(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.KNOWN,
            ("healthy", "impeller")
        ))
        self.assertEqual(result.level, DecisionLevel.AMBER)

    def test_red_base_singleton_disagreement(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.KNOWN,
            ("soft_foot",), "healthy"
        ))
        self.assertEqual(result.level, DecisionLevel.RED)
        self.assertIn("BASE_DIAGNOSIS_DISAGREES_WITH_SINGLETON", result.reason_codes)

    def test_amber_auxiliary_warning(self):
        result = decide(TrustTwinInput(
            DomainStatus.SUPPORTED, SensorStatus.HEALTHY, OODStatus.KNOWN,
            ("bearing_bpfo",), "bearing_bpfo", ("CONTEXT_REVIEW",)
        ))
        self.assertEqual(result.level, DecisionLevel.AMBER)

    def test_unknown_statuses_are_red(self):
        result = decide(TrustTwinInput(
            DomainStatus.UNKNOWN, SensorStatus.UNKNOWN, OODStatus.UNKNOWN,
            ("healthy",)
        ))
        self.assertEqual(result.level, DecisionLevel.RED)
        self.assertEqual(set(result.reason_codes), {
            "DOMAIN_STATUS_UNKNOWN",
            "SENSOR_STATUS_UNKNOWN",
            "OOD_STATUS_UNKNOWN",
        })


if __name__ == "__main__":
    unittest.main()
