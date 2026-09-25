import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from demo.server import evaluate_payload


class DemoDecisionIntegrationTests(unittest.TestCase):
    def test_green_demo_uses_frozen_engine(self):
        result = evaluate_payload({
            "domain_status": "SUPPORTED",
            "sensor_status": "HEALTHY",
            "ood_status": "KNOWN",
            "base_diagnosis": "bearing_bpfi",
            "conformal_set": ["bearing_bpfi"],
            "auxiliary_warnings": [],
        })
        self.assertEqual(result["level"], "GREEN")
        self.assertEqual(result["issued_diagnosis"], "bearing_bpfi")
        self.assertFalse(result["human_review_required"])
        self.assertFalse(result["autonomous_maintenance_allowed"])

    def test_amber_multiclass_routes_to_review(self):
        result = evaluate_payload({
            "domain_status": "SUPPORTED",
            "sensor_status": "HEALTHY",
            "ood_status": "KNOWN",
            "base_diagnosis": "impeller",
            "conformal_set": ["healthy", "impeller"],
            "auxiliary_warnings": [],
        })
        self.assertEqual(result["level"], "AMBER")
        self.assertTrue(result["human_review_required"])
        self.assertIsNone(result["issued_diagnosis"])

    def test_red_sensor_degradation_preempts_singleton(self):
        result = evaluate_payload({
            "domain_status": "SUPPORTED",
            "sensor_status": "DEGRADED",
            "ood_status": "KNOWN",
            "base_diagnosis": "bearing_contaminated",
            "conformal_set": ["bearing_contaminated"],
            "auxiliary_warnings": [],
        })
        self.assertEqual(result["level"], "RED")
        self.assertIn("SENSOR_DEGRADED", result["reason_codes"])
        self.assertIsNone(result["issued_diagnosis"])

    def test_red_domain_shift(self):
        result = evaluate_payload({
            "domain_status": "OUTSIDE",
            "sensor_status": "HEALTHY",
            "ood_status": "UNKNOWN",
            "base_diagnosis": "healthy",
            "conformal_set": [],
            "auxiliary_warnings": [],
        })
        self.assertEqual(result["level"], "RED")
        self.assertIn("DOMAIN_OUTSIDE_SUPPORT", result["reason_codes"])

    def test_policy_version_exposed(self):
        result = evaluate_payload({
            "domain_status": "SUPPORTED",
            "sensor_status": "HEALTHY",
            "ood_status": "KNOWN",
            "base_diagnosis": "healthy",
            "conformal_set": ["healthy"],
            "auxiliary_warnings": [],
        })
        self.assertEqual(result["policy_version"], "TrustTwin-runtime-policy-v1")


if __name__ == "__main__":
    unittest.main()
