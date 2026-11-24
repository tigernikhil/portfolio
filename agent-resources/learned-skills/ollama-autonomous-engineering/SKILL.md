---
name: ollama-autonomous-engineering
description: Protocol for delegating mechanical, heavy, and repetitive coding and documentation tasks to local Ollama models with zero token usage.
---

# Ollama Autonomous Engineering Protocol

## 1. Overview
This skill guides agents on how to leverage local Ollama models (`http://localhost:11434`) for offline, zero-token, autonomous task execution and self-correction.

Reference:
- Architecture: [docs/integrations/local-ai.md](file:///Users/admin/Downloads/Portfolio/docs/integrations/local-ai.md)
- ADR: [docs/decisions/ADR-004-tool-execution.md](file:///Users/admin/Downloads/Portfolio/docs/decisions/ADR-004-tool-execution.md)

## 2. Model Routing Matrix
| Task Type | Recommended Model | Why |
|---|---|---|
| Code implementation, TypeScript, Tests, Schemas | `qwen2.5-coder:7b` | Exceptional TypeScript strict fidelity, Zod accuracy, and unit test generation. |
| Deep Architectural Documents & ADRs | `mistral-nemo:12b` | 128k context, nuanced reasoning, comprehensive technical prose. |
| High-Speed Documentation & Text summaries | `qwen2.5:3b` | 30-50 tokens/sec, low memory, structured markdown. |

## 3. Concurrency & Resource Management
- Default to **2 parallel worker threads** for Ollama to avoid memory thrashing on unified memory macOS.
- Enforce explicit `strip_outer_fences` to eliminate accidental nested markdown block generation.
- Enforce self-correction loops: validate JSON with `json.loads()` and re-prompt immediately on syntax failures.

## 4. Execution Pattern
Agents should invoke the Python automation harness at `scripts/generate_platform_via_ollama.py` or use standard HTTP POST requests to `http://localhost:11434/api/generate`.
