---
name: ollama-delegate
description: Generic, agent-agnostic protocol for delegating local, non-research, or mechanical LLM tasks (prompt compression, content calendars, drafting, data parsing, metadata) to local Ollama endpoints (http://localhost:11434). Conserves online tokens, enforces deterministic JSON schemas, and enables seamless cross-agent handovers.
---

# Universal Ollama Task Delegation Skill

## 1. Purpose & Scope
This skill defines an **agent-agnostic protocol** for any AI agent, subagent, or automation pipeline to offload local, repetitive, or token-heavy processing to local Ollama instances. 

### Why Use This Skill:
- **Zero Token Cost**: Run bulk transformations, drafting, and JSON formatting completely offline.
- **Privacy & Speed**: Process sensitive or large context documents locally with zero network latency.
- **Online Token Optimization**: Compress large prompts by 50–80% before submitting to paid external LLMs (GPT-4o, Claude 3.5, Gemini Pro).
- **Inter-Agent Continuity**: All delegated jobs write standardized JSON/Markdown outputs to disk so any other agent or system can resume execution seamlessly.

---

## 2. Universal Division of Labor Matrix

| Category | High-Tier Online Agent (Cloud) | Local Delegated Agent (Ollama) |
|---|---|---|
| **Architecture** | High-level system design, multi-repository planning | Implementing individual file changes from plan |
| **Reasoning** | Complex root-cause analysis, subtle debugging | Drafting repetitive unit tests, mocking boilerplate |
| **Research** | Live web browsing, evaluating recent SDKs | Summarizing existing local documentation files |
| **Writing** | Final editorial review, critical client copy | Generating 30-day content queues, first drafts |
| **Data & SEO** | Strategic keyword research & audience profiling | Formatting tags, generating alt-text, JSON parsing |
| **Token Prep** | Final execution with compressed prompt | Compressing raw verbose prompts via `token-optimizer` |

---

## 3. Generic Model Capability Tiers
Agents MUST route tasks to the appropriate model tier based on compute weight:

| Tier | Typical Models | Characteristics | Best Suited Tasks |
|---|---|---|---|
| **Tier 1: Ultra-Fast** | `llama3.2:3b`, `token-optimizer` | ~30-50 tok/s, ~2GB VRAM/RAM | Token compression, keyword extraction, JSON calendar batches, alt-text, schema validation |
| **Tier 2: Balanced** | `llama3:8b`, `qwen2.5:7b`, `mistral:7b` | ~15-25 tok/s, ~4-5GB VRAM/RAM | Episode scripts, technical guides, code boilerplate, structured summaries |
| **Tier 3: Deep Reasoning** | `mistral-nemo:12b`, `qwen2.5:14b`, `command-r` | ~6-12 tok/s, ~7-9GB VRAM/RAM | Complex creative writing, nuance-heavy philosophy, detailed code refactoring |

---

## 4. Universal Protocol Implementation

Any agent in any environment can invoke this protocol using standard HTTP REST requests. No external libraries required.

### A. Python (Zero-Dependency / Standard Library)
```python
import json
import urllib.request
from typing import Dict, Any, Optional

def delegate_to_ollama(
    prompt: str,
    system_prompt: str = "",
    model_tier: str = "fast",  # "fast", "balanced", or "deep"
    format_json: bool = False,
    host: str = "http://localhost:11434"
) -> Dict[str, Any]:
    """
    Generic execution contract for Ollama delegation.
    Returns: {"success": bool, "content": str, "model": str, "error": Optional[str]}
    """
    tier_map = {
        "fast": "llama3.2:3b",
        "balanced": "llama3:8b",
        "deep": "mistral-nemo:12b"
    }
    model = tier_map.get(model_tier, "llama3.2:3b")
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2 if format_json else 0.7,
            "num_predict": 2048
        }
    }
    if system_prompt:
        payload["system"] = system_prompt
    if format_json:
        payload["format"] = "json"

    try:
        req = urllib.request.Request(
            f"{host}/api/generate",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {
                "success": True,
                "content": data.get("response", "").strip(),
                "model": model,
                "error": None
            }
    except Exception as exc:
        return {
            "success": False,
            "content": "",
            "model": model,
            "error": str(exc)
        }
```

### B. Shell / cURL (Universal CLI)
```bash
# Generic JSON prompt invocation
curl -s http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3.2:3b",
    "prompt": "Extract 5 SEO keywords from this text: ...",
    "stream": false,
    "format": "json"
  }' | jq -r '.response'
```

---

## 5. Standardized Agent Execution Rules
1. **STRICT MANDATORY POLICY — ZERO BACKGROUND TASKS**:
   Agents must NEVER launch asynchronous background tasks or leave background processes running in the conversation environment. If a task is computationally heavy, repetitive, or long-running, it MUST be offloaded synchronously to local Ollama (`http://localhost:11434`) or executed synchronously with immediate return. Background polling loops and unmonitored background tasks are strictly forbidden.
2. **Always Verify Availability First**:
   Send a `GET http://localhost:11434/api/tags` request. If status is not `200`, report that Ollama service is stopped or fallback to synchronous local execution.
3. **Mandatory Output Persistence**:
   Never hold delegated results solely in memory. Immediately persist outputs to:
   - Markdown documents (`docs/` or `skills/`) for human-readable content.
   - Structured JSON files (`pages/*/` or `data/`) for programmatic pipeline ingestion.
4. **Inter-Agent Handover Documentation**:
   Every persistent artifact must include a metadata header specifying:
   - `created_at`: Timestamp
   - `model_used`: e.g., `llama3:8b`
   - `task_type`: e.g., `content_generation`, `token_optimization`
   - `status`: `draft`, `reviewed`, or `complete`

---

## 6. Token Optimization Protocol
Before sending any prompt exceeding 500 words to an online model, agents SHOULD route the prompt through the local `token-optimizer` model or `scripts/optimize_tokens.py` to compress token density while preserving 100% of functional requirements and constraints.
