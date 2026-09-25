import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from trusttwin import DomainStatus, OODStatus, SensorStatus, TrustTwinInput, decide


def main():
    parser = argparse.ArgumentParser(
        description="Apply the frozen TrustTwin GREEN/AMBER/RED policy."
    )
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()

    payload = json.loads(args.input_json.read_text(encoding="utf-8"))
    evidence = TrustTwinInput(
        domain_status=DomainStatus(payload["domain_status"]),
        sensor_status=SensorStatus(payload["sensor_status"]),
        ood_status=OODStatus(payload["ood_status"]),
        conformal_set=tuple(payload.get("conformal_set", [])),
        base_diagnosis=payload.get("base_diagnosis"),
        auxiliary_warnings=tuple(payload.get("auxiliary_warnings", [])),
    )
    print(json.dumps(decide(evidence).to_dict(), indent=2))


if __name__ == "__main__":
    main()
