from __future__ import annotations

import argparse
import json
import mimetypes
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from trusttwin import (  # noqa: E402
    DomainStatus,
    OODStatus,
    SensorStatus,
    TrustTwinInput,
    decide,
)

DEMO_ROOT = Path(__file__).resolve().parent
WEB_ROOT = DEMO_ROOT / "web"
SCENARIOS_PATH = DEMO_ROOT / "scenarios.json"
POLICY_VERSION = "TrustTwin-runtime-policy-v1"


def evaluate_payload(payload: dict) -> dict:
    evidence = TrustTwinInput(
        domain_status=DomainStatus(payload["domain_status"]),
        sensor_status=SensorStatus(payload["sensor_status"]),
        ood_status=OODStatus(payload["ood_status"]),
        conformal_set=tuple(payload.get("conformal_set", [])),
        base_diagnosis=payload.get("base_diagnosis"),
        auxiliary_warnings=tuple(payload.get("auxiliary_warnings", [])),
    )

    decision = decide(evidence)
    result = decision.to_dict()
    result["level"] = decision.level.value
    result["policy_version"] = POLICY_VERSION
    return result


class TrustTwinDemoHandler(BaseHTTPRequestHandler):
    server_version = "TrustTwinDemo/0.1.0"

    def _json(self, payload: dict | list, status: int = 200) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _text(self, message: str, status: int = 200) -> None:
        body = message.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_static(self, requested_path: str) -> None:
        relative = "index.html" if requested_path in {"", "/"} else requested_path.lstrip("/")
        relative = unquote(relative)
        candidate = (WEB_ROOT / relative).resolve()
        web_root = WEB_ROOT.resolve()

        if candidate != web_root and web_root not in candidate.parents:
            self._text("Forbidden", 403)
            return

        if not candidate.is_file():
            self._text("Not found", 404)
            return

        content = candidate.read_bytes()
        media_type = mimetypes.guess_type(candidate.name)[0] or "application/octet-stream"
        if media_type.startswith("text/") or media_type in {
            "application/javascript",
            "application/json",
        }:
            media_type += "; charset=utf-8"

        self.send_response(200)
        self.send_header("Content-Type", media_type)
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(content)

    def do_GET(self) -> None:  # noqa: N802
        path = urlparse(self.path).path

        if path == "/api/health":
            self._json({
                "status": "ok",
                "service": "TrustTwin Phase 9C demonstrator",
                "policy_version": POLICY_VERSION,
                "autonomous_maintenance_allowed": False,
            })
            return

        if path == "/api/scenarios":
            scenarios = json.loads(SCENARIOS_PATH.read_text(encoding="utf-8"))
            self._json(scenarios)
            return

        self._serve_static(path)

    def do_POST(self) -> None:  # noqa: N802
        path = urlparse(self.path).path
        if path != "/api/decision":
            self._text("Not found", 404)
            return

        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length <= 0 or length > 100_000:
                raise ValueError("Invalid request body length.")

            payload = json.loads(self.rfile.read(length).decode("utf-8"))
            result = evaluate_payload(payload)
        except (ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            self._json({"error": str(exc)}, 400)
            return

        self._json(result)

    def log_message(self, format: str, *args) -> None:
        sys.stdout.write(
            "[TrustTwin] %s - %s\n"
            % (self.address_string(), format % args)
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run the TrustTwin Phase 9C local research demonstrator."
    )
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    server = ThreadingHTTPServer(
        (args.host, args.port),
        TrustTwinDemoHandler,
    )

    print("TrustTwin AI — Phase 9C research demonstrator")
    print(f"Policy: {POLICY_VERSION}")
    print(f"Open: http://{args.host}:{args.port}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping TrustTwin demonstrator.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
