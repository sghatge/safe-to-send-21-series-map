# Safe to Send: all 28 repos

28 days of governing AI in CRM operations.

## Week 1: The Gate

| Ep | Repo | What it shows |
|---|---|---|
| 01 | [safe-to-send-01-agent-blast-radius](https://github.com/sghatge/safe-to-send-01-agent-blast-radius) | Agent blast radius |
| 02 | [safe-to-send-02-five-decisions](https://github.com/sghatge/safe-to-send-02-five-decisions) | Five decisions, not two |
| 03 | [safe-to-send-03-policy-as-code](https://github.com/sghatge/safe-to-send-03-policy-as-code) | Policy is a file, not a prompt |
| 04 | [safe-to-send-04-black-friday-replay](https://github.com/sghatge/safe-to-send-04-black-friday-replay) | Black Friday replay |
| 05 | [safe-to-send-05-presend-qa](https://github.com/sghatge/safe-to-send-05-presend-qa) | Nine pre-send checks |
| 06 | [safe-to-send-06-audit-chain](https://github.com/sghatge/safe-to-send-06-audit-chain) | Tamper-evident audit |
| 07 | [safe-to-send-07-red-team-your-guardrail](https://github.com/sghatge/safe-to-send-07-red-team-your-guardrail) | Red-team your guardrail |

## Week 2: The Workbench

| Ep | Repo | What it shows |
|---|---|---|
| 08 | [safe-to-send-08-rule-model-or-human](https://github.com/sghatge/safe-to-send-08-rule-model-or-human) | Rule, model or human? |
| 09 | [safe-to-send-09-golden-tests](https://github.com/sghatge/safe-to-send-09-golden-tests) | Golden tests before models |
| 10 | [safe-to-send-10-synthetic-market](https://github.com/sghatge/safe-to-send-10-synthetic-market) | Synthetic market with an answer key |
| 11 | [safe-to-send-11-llm-adapter](https://github.com/sghatge/safe-to-send-11-llm-adapter) | An LLM adapter that fails safe |
| 12 | [safe-to-send-12-verdict-lock](https://github.com/sghatge/safe-to-send-12-verdict-lock) | Verdict lock |
| 13 | [safe-to-send-13-approval-inbox](https://github.com/sghatge/safe-to-send-13-approval-inbox) | Approval inbox |
| 14 | [safe-to-send-14-blameless-postmortem](https://github.com/sghatge/safe-to-send-14-blameless-postmortem) | Blameless postmortem kit |

## Week 3: The Knowledge

| Ep | Repo | What it shows |
|---|---|---|
| 15 | [safe-to-send-15-playbook-linter](https://github.com/sghatge/safe-to-send-15-playbook-linter) | Playbook linter |
| 16 | [safe-to-send-16-policy-invariants-ci](https://github.com/sghatge/safe-to-send-16-policy-invariants-ci) | Policy invariants in CI |
| 17 | [safe-to-send-17-workflow-xray](https://github.com/sghatge/safe-to-send-17-workflow-xray) | Workflow x-ray |
| 18 | [safe-to-send-18-journey-patterns](https://github.com/sghatge/safe-to-send-18-journey-patterns) | Journey patterns |
| 19 | [safe-to-send-19-local-first-insights](https://github.com/sghatge/safe-to-send-19-local-first-insights) | Local-first insights |
| 20 | [safe-to-send-20-fresh-search](https://github.com/sghatge/safe-to-send-20-fresh-search) | Fresh search over runbooks |
| 21 | [safe-to-send-21-series-map](https://github.com/sghatge/safe-to-send-21-series-map) | The series map (this repo) |

## Week 4: The Operating Model

| Ep | Repo | What it shows |
|---|---|---|
| 22 | [safe-to-send-22-readiness-score](https://github.com/sghatge/safe-to-send-22-readiness-score) | AI readiness score |
| 23 | [safe-to-send-23-what-if-simulator](https://github.com/sghatge/safe-to-send-23-what-if-simulator) | What-if simulator |
| 24 | [safe-to-send-24-team-roadmap](https://github.com/sghatge/safe-to-send-24-team-roadmap) | From scores to a 90-day plan |
| 25 | [safe-to-send-25-honest-roi](https://github.com/sghatge/safe-to-send-25-honest-roi) | Honest ROI |
| 26 | [safe-to-send-26-cmo-translator](https://github.com/sghatge/safe-to-send-26-cmo-translator) | Explain it to a CMO |
| 27 | [safe-to-send-27-data-leak-guard](https://github.com/sghatge/safe-to-send-27-data-leak-guard) | Data leak guard for open source |
| 28 | [safe-to-send-28-preflight](https://github.com/sghatge/safe-to-send-28-preflight) | Preflight: the series in one command |

## How the episodes connect

```mermaid
flowchart LR
  subgraph W1["Week 1: The Gate"]
    E1["01 Agent blast radius"]
    E2["02 Five decisions, not two"]
    E3["03 Policy is a file, not a prompt"]
    E4["04 Black Friday replay"]
    E5["05 Nine pre-send checks"]
    E6["06 Tamper-evident audit"]
    E7["07 Red-team your guardrail"]
  end
  subgraph W2["Week 2: The Workbench"]
    E8["08 Rule, model or human?"]
    E9["09 Golden tests before models"]
    E10["10 Synthetic market with an answer key"]
    E11["11 An LLM adapter that fails safe"]
    E12["12 Verdict lock"]
    E13["13 Approval inbox"]
    E14["14 Blameless postmortem kit"]
  end
  subgraph W3["Week 3: The Knowledge"]
    E15["15 Playbook linter"]
    E16["16 Policy invariants in CI"]
    E17["17 Workflow x-ray"]
    E18["18 Journey patterns"]
    E19["19 Local-first insights"]
    E20["20 Fresh search over runbooks"]
    E21["21 The series map (this repo)"]
  end
  subgraph W4["Week 4: The Operating Model"]
    E22["22 AI readiness score"]
    E23["23 What-if simulator"]
    E24["24 From scores to a 90-day plan"]
    E25["25 Honest ROI"]
    E26["26 Explain it to a CMO"]
    E27["27 Data leak guard for open source"]
    E28["28 Preflight: the series in one command"]
  end
  E1 --> E2
  E2 --> E3
  E2 --> E4
  E3 --> E4
  E2 --> E7
  E8 --> E9
  E5 --> E10
  E8 --> E11
  E11 --> E12
  E5 --> E12
  E2 --> E13
  E3 --> E16
  E22 --> E23
  E22 --> E24
  E10 --> E25
  E5 --> E25
  E10 --> E27
  E2 --> E28
  E3 --> E28
  E5 --> E28
  E6 --> E28
  E12 --> E28
```

## Foundations

- [acc-agent-gate](https://github.com/sghatge/acc-agent-gate): ACC Agent Gate: governance layer between AI agents and Adobe Campaign
- [ai-readiness-calculator](https://github.com/sghatge/ai-readiness-calculator): AI Readiness Calculator
- [crm-ai-agent-platform](https://github.com/sghatge/crm-ai-agent-platform): CRM AI Agent Platform (rules-first workbench)
