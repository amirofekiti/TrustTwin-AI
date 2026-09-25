from dataclasses import dataclass, asdict
from enum import Enum
from typing import Iterable, Optional, Tuple


class DecisionLevel(str, Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"


class DomainStatus(str, Enum):
    SUPPORTED = "SUPPORTED"
    OUTSIDE = "OUTSIDE"
    UNKNOWN = "UNKNOWN"


class SensorStatus(str, Enum):
    HEALTHY = "HEALTHY"
    DEGRADED = "DEGRADED"
    UNKNOWN = "UNKNOWN"


class OODStatus(str, Enum):
    KNOWN = "KNOWN"
    NOVEL = "NOVEL"
    UNKNOWN = "UNKNOWN"


@dataclass(frozen=True)
class TrustTwinInput:
    domain_status: DomainStatus
    sensor_status: SensorStatus
    ood_status: OODStatus
    conformal_set: Tuple[str, ...]
    base_diagnosis: Optional[str] = None
    auxiliary_warnings: Tuple[str, ...] = ()


@dataclass(frozen=True)
class TrustTwinDecision:
    level: DecisionLevel
    issued_diagnosis: Optional[str]
    candidate_classes: Tuple[str, ...]
    reason_codes: Tuple[str, ...]
    human_review_required: bool
    autonomous_maintenance_allowed: bool = False

    def to_dict(self):
        return asdict(self)


def _normalise_classes(values: Iterable[str]) -> Tuple[str, ...]:
    cleaned = []
    seen = set()
    for value in values:
        item = str(value).strip()
        if item and item not in seen:
            seen.add(item)
            cleaned.append(item)
    return tuple(cleaned)


def decide(evidence: TrustTwinInput) -> TrustTwinDecision:
    """Apply the frozen TrustTwin hierarchy.

    GREEN means the current evidence gates permit a diagnosis to proceed to a
    human-facing workflow. It is not a guarantee of correctness and it never
    grants autonomous maintenance authority.
    """
    conformal = _normalise_classes(evidence.conformal_set)
    reasons = []

    if evidence.domain_status == DomainStatus.OUTSIDE:
        reasons.append("DOMAIN_OUTSIDE_SUPPORT")
    elif evidence.domain_status == DomainStatus.UNKNOWN:
        reasons.append("DOMAIN_STATUS_UNKNOWN")

    if evidence.sensor_status == SensorStatus.DEGRADED:
        reasons.append("SENSOR_DEGRADED")
    elif evidence.sensor_status == SensorStatus.UNKNOWN:
        reasons.append("SENSOR_STATUS_UNKNOWN")

    if evidence.ood_status == OODStatus.NOVEL:
        reasons.append("OOD_NOVEL")
    elif evidence.ood_status == OODStatus.UNKNOWN:
        reasons.append("OOD_STATUS_UNKNOWN")

    if reasons:
        return TrustTwinDecision(
            DecisionLevel.RED, None, conformal, tuple(reasons), True
        )

    if len(conformal) == 0:
        return TrustTwinDecision(
            DecisionLevel.RED, None, (), ("CONFORMAL_EMPTY",), True
        )

    if len(conformal) > 1:
        reasons = ["CONFORMAL_AMBIGUOUS"]
        if evidence.auxiliary_warnings:
            reasons.append("AUXILIARY_WARNING")
        return TrustTwinDecision(
            DecisionLevel.AMBER, None, conformal, tuple(reasons), True
        )

    singleton = conformal[0]

    if (
        evidence.base_diagnosis is not None
        and str(evidence.base_diagnosis).strip()
        and str(evidence.base_diagnosis).strip() != singleton
    ):
        return TrustTwinDecision(
            DecisionLevel.RED,
            None,
            conformal,
            ("BASE_DIAGNOSIS_DISAGREES_WITH_SINGLETON",),
            True,
        )

    if evidence.auxiliary_warnings:
        return TrustTwinDecision(
            DecisionLevel.AMBER,
            None,
            conformal,
            ("CONFORMAL_SINGLETON", "AUXILIARY_WARNING"),
            True,
        )

    return TrustTwinDecision(
        DecisionLevel.GREEN,
        singleton,
        conformal,
        ("CONFORMAL_SINGLETON", "GREEN_SUPPORTED_DIAGNOSIS"),
        False,
    )
