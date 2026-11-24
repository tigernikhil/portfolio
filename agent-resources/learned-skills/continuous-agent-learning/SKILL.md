---
name: continuous-agent-learning
description: Mandatory protocol for every coding agent to consult, apply, update, and improve reusable skills in agent-resources with each task.
---

# Continuous Agent Learning & Skill Governance

## 1. Mandatory Policy
Every coding agent (Gemini, local Ollama, Claude, Cursor, Copilot) operating on this repository **MUST**:
1. **Consult Prior Art**: Read all relevant skills in `agent-resources/` and documentation in `docs/` before implementing or modifying code.
2. **Strict Adherence**: Follow established architectural rules, port/adapter boundaries, and zero-token waste policies.
3. **Capture Lessons**: With each task completed, if a new pattern, edge case, failure mode, or improvement was discovered, update the respective skill in `agent-resources/` or author a new one.
4. **Link to Docs**: Never keep hardcoded facts or data findings in isolated silos; all data findings, architectural decisions, and schemas must be documented under `docs/` and cross-referenced.

## 2. Skill Directory Structure
```
agent-resources/
├── learned-skills/
│   ├── continuous-agent-learning/SKILL.md
│   ├── ollama-autonomous-engineering/SKILL.md
│   ├── tool-sdk-authoring/SKILL.md
│   └── financial-tool-security/SKILL.md
├── superpowers/
│   └── skills/
└── elephant-goldfish-model/
```

## 3. Skill Update Lifecycle
1. **Pre-flight**: Agent identifies task scope -> loads relevant skill.
2. **Execution**: Implements code or documentation following skill constraints.
3. **Verification**: Verifies code with tests (Vitest) and type checks.
4. **Self-Improvement**: Updates the skill markdown with any newly learned edge cases, configuration optimizations, or model prompts.
