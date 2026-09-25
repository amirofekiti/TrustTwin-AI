const state = {
  scenarios: [],
  currentScenario: null,
  audit: []
};

const $ = (id) => document.getElementById(id);

const scenarioSelect = $("scenarioSelect");
const domainStatus = $("domainStatus");
const sensorStatus = $("sensorStatus");
const oodStatus = $("oodStatus");
const baseDiagnosis = $("baseDiagnosis");
const conformalSet = $("conformalSet");
const warnings = $("warnings");
const evaluateButton = $("evaluateButton");

function splitList(value) {
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function pretty(value) {
  if (value === null || value === undefined || value === "") return "—";
  return String(value).replaceAll("_", " ");
}

function statusText(level) {
  if (level === "GREEN") {
    return {
      title: "Diagnosis may proceed",
      subtitle: "All frozen TrustTwin evidence gates passed. Human maintenance authority remains in force."
    };
  }
  if (level === "AMBER") {
    return {
      title: "Human review required",
      subtitle: "The upstream trust gates passed, but the diagnostic evidence remains ambiguous or carries a review warning."
    };
  }
  return {
    title: "Diagnosis withheld",
    subtitle: "At least one hard trust gate failed. The model output must not be treated as an automated diagnosis."
  };
}

function renderScenarioMeta(scenario) {
  $("machineName").textContent = scenario.machine;
  $("datasetContext").textContent = scenario.dataset_context;
  $("operatingPoint").textContent = scenario.operating_point;
  $("researchNote").textContent = scenario.research_note;
  $("targetLabel").textContent = `Target: ${scenario.target}`;

  const entries = Object.entries(scenario.demo_probabilities || {})
    .sort((a, b) => b[1] - a[1]);

  $("probabilityBars").innerHTML = entries.map(([label, value]) => `
    <div class="bar-row">
      <div class="bar-label" title="${label}">${pretty(label)}</div>
      <div class="bar-track"><div class="bar-fill" style="width:${Math.round(value * 100)}%"></div></div>
      <div class="bar-value">${(value * 100).toFixed(0)}%</div>
    </div>
  `).join("");
}

function loadScenario(scenario) {
  state.currentScenario = scenario;
  domainStatus.value = scenario.domain_status;
  sensorStatus.value = scenario.sensor_status;
  oodStatus.value = scenario.ood_status;
  baseDiagnosis.value = scenario.base_diagnosis ?? "";
  conformalSet.value = scenario.conformal_set.join(", ");
  warnings.value = (scenario.auxiliary_warnings || []).join(", ");
  renderScenarioMeta(scenario);
}

function gateClass(kind, value) {
  if (kind === "domain") return value === "SUPPORTED" ? "pass" : "fail";
  if (kind === "sensor") return value === "HEALTHY" ? "pass" : "fail";
  if (kind === "ood") return value === "KNOWN" ? "pass" : "fail";
  return "warn";
}

function renderGates(payload, result) {
  const conformalCount = result.candidate_classes.length;
  const conformalState = conformalCount === 1 ? "pass" : (conformalCount > 1 ? "warn" : "fail");

  const gates = [
    ["Operating-domain support", payload.domain_status, gateClass("domain", payload.domain_status)],
    ["Sensor health", payload.sensor_status, gateClass("sensor", payload.sensor_status)],
    ["OOD / novelty", payload.ood_status, gateClass("ood", payload.ood_status)],
    ["Conformal prediction set", `${conformalCount} class${conformalCount === 1 ? "" : "es"}`, conformalState],
    ["Human authority", "RETAINED", "pass"]
  ];

  $("gateList").innerHTML = gates.map(([name, value, cls]) => `
    <div class="gate ${cls}">
      <span class="gate-dot"></span>
      <span class="gate-name">${name}</span>
      <span class="gate-value">${pretty(value)}</span>
    </div>
  `).join("");
}

function renderChips(elementId, values, emptyLabel = "None") {
  const target = $(elementId);
  if (!values || values.length === 0) {
    target.innerHTML = `<span class="reason-chip">${emptyLabel}</span>`;
    return;
  }
  target.innerHTML = values.map((value) =>
    `<span class="reason-chip">${pretty(value)}</span>`
  ).join("");
}

function addAudit(result) {
  const now = new Date();
  state.audit.unshift({
    level: result.level,
    time: now.toLocaleTimeString(),
    diagnosis: result.issued_diagnosis,
    reasons: result.reason_codes
  });
  state.audit = state.audit.slice(0, 8);

  $("auditLog").innerHTML = state.audit.map((entry) => `
    <div class="audit-entry ${entry.level.toLowerCase()}">
      <strong>${entry.time} · ${entry.level}</strong>
      <div>${entry.diagnosis ? `Diagnosis: ${pretty(entry.diagnosis)}` : "No diagnosis issued"} · ${entry.reasons.join(", ")}</div>
    </div>
  `).join("");
}

function renderDecision(payload, result) {
  const hero = $("decisionHero");
  hero.className = `decision-hero ${result.level.toLowerCase()}-state`;
  $("statusOrb").innerHTML = `<span>${result.level}</span>`;

  const copy = statusText(result.level);
  $("decisionTitle").textContent = copy.title;
  $("decisionSubtitle").textContent = copy.subtitle;
  $("issuedDiagnosis").textContent = result.issued_diagnosis ? pretty(result.issued_diagnosis) : "WITHHELD";
  $("reviewRequired").textContent = result.human_review_required ? "REQUIRED" : "NOT REQUIRED";
  $("autonomousMaintenance").textContent = result.autonomous_maintenance_allowed ? "AUTHORISED" : "NOT AUTHORISED";
  $("policyVersion").textContent = result.policy_version;

  renderChips("reasonCodes", result.reason_codes);
  renderChips("candidateClasses", result.candidate_classes, "Empty set");
  renderGates(payload, result);
  addAudit(result);
}

async function evaluate() {
  const payload = {
    domain_status: domainStatus.value,
    sensor_status: sensorStatus.value,
    ood_status: oodStatus.value,
    base_diagnosis: baseDiagnosis.value.trim() || null,
    conformal_set: splitList(conformalSet.value),
    auxiliary_warnings: splitList(warnings.value)
  };

  evaluateButton.disabled = true;
  evaluateButton.textContent = "Evaluating…";

  try {
    const response = await fetch("/api/decision", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });

    const result = await response.json();

    if (!response.ok) {
      throw new Error(result.error || "Decision service error.");
    }

    renderDecision(payload, result);
  } catch (error) {
    $("decisionTitle").textContent = "Decision service unavailable";
    $("decisionSubtitle").textContent = error.message;
    $("decisionHero").className = "decision-hero red-state";
    $("statusOrb").innerHTML = "<span>ERROR</span>";
  } finally {
    evaluateButton.disabled = false;
    evaluateButton.textContent = "Evaluate trust state";
  }
}

async function initialise() {
  const response = await fetch("/api/scenarios");
  state.scenarios = await response.json();

  scenarioSelect.innerHTML = state.scenarios.map((scenario) =>
    `<option value="${scenario.id}">${scenario.name}</option>`
  ).join("");

  scenarioSelect.addEventListener("change", () => {
    const scenario = state.scenarios.find((item) => item.id === scenarioSelect.value);
    if (scenario) {
      loadScenario(scenario);
      evaluate();
    }
  });

  evaluateButton.addEventListener("click", evaluate);

  if (state.scenarios.length) {
    loadScenario(state.scenarios[0]);
    await evaluate();
  }
}

initialise().catch((error) => {
  $("researchNote").textContent = `Unable to load demo scenarios: ${error.message}`;
});
