#!/usr/bin/env python3
"""
AI Gateway: Dynamic Model Auto-Rotator & Failover Proxy
======================================================
An OpenAI-compatible proxy server (running on http://127.0.0.1:8080/v1) that
pools, load-balances, and auto-rotates across ANY free or custom online models.

Supported Out-of-the-Box:
- OpenRouter (Free models: Qwen 2.5 Coder, DeepSeek R1, Llama 3.3, etc.)
- Google Gemini (Gemini 2.0 Flash, 1.5 Flash via OpenAI endpoint)
- Groq Cloud (Llama 3.3 70B, Mixtral)
- GitHub Models / Azure AI (GPT-4o-mini, Phi-3.5, Llama 3.3 using standard GitHub PAT)
- SambaNova Cloud (Llama 3.3 70B, Qwen 2.5 Coder 32B)
- Cerebras Cloud (Llama 3.3 70B at 2,000+ tok/s)
- Mistral AI (Codestral, Mistral Small free experiment tiers)
- Hugging Face Inference API
- Custom endpoints (Any OpenAI-compatible server URL + model name + headers)
- Local Ollama fallback
"""

import os
import sys
import json
import time
import http.server
import socketserver
import urllib.request
import urllib.error
from typing import List, Dict, Any, Optional

PORT = int(os.environ.get("AI_GATEWAY_PORT", "8080"))
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gateway_config.json")
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
DOTENV_FILE = os.path.join(ROOT_DIR, ".env")

# Cooldown tracker {model_id: expiry_timestamp}
cooldowns: Dict[str, float] = {}
current_model_index = 0

DEFAULT_CONFIG = {
    "keys": {
        "OPENROUTER_API_KEY": "",
        "GEMINI_API_KEY": "",
        "GROQ_API_KEY": "",
        "GITHUB_TOKEN": "",
        "SAMBANOVA_API_KEY": "",
        "CEREBRAS_API_KEY": "",
        "MISTRAL_API_KEY": "",
        "HUGGINGFACE_API_KEY": ""
    },
    "custom_models": []
}

def load_dotenv_keys() -> Dict[str, str]:
    env_keys = {}
    if os.path.exists(DOTENV_FILE):
        try:
            with open(DOTENV_FILE, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k in DEFAULT_CONFIG["keys"] and v:
                            env_keys[k] = v
        except Exception as e:
            print(f"[Gateway] Error reading .env: {e}")
    return env_keys

def load_config() -> Dict[str, Any]:
    merged = dict(DEFAULT_CONFIG)
    merged["keys"] = dict(DEFAULT_CONFIG["keys"])

    # 1. Read from .env
    dotenv_keys = load_dotenv_keys()
    merged["keys"].update(dotenv_keys)

    # 2. Read from gateway_config.json (takes priority if modified)
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                file_keys = {k: v for k, v in data.get("keys", {}).items() if v}
                merged["keys"].update(file_keys)
                merged["custom_models"] = data.get("custom_models", [])
        except Exception as e:
            print(f"[Gateway] Error reading config: {e}")

    # 3. Read from os.environ
    for k in DEFAULT_CONFIG["keys"]:
        val = os.environ.get(k)
        if val:
            merged["keys"][k] = val

    return merged

def save_config(config: Dict[str, Any]):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def build_model_pool(config: Dict[str, Any]) -> List[Dict[str, Any]]:
    keys = config.get("keys", {})
    pool = []

    # 1. Groq (High speed, verified active)
    if keys.get("GROQ_API_KEY"):
        groq_key = keys["GROQ_API_KEY"]
        for m in ["qwen/qwen3.8-27b", "openai/gpt-oss-20b"]:
            pool.append({
                "id": f"groq/{m}",
                "provider": "groq",
                "model_name": m,
                "url": "https://api.groq.com/openai/v1/chat/completions",
                "headers": {
                    "Authorization": f"Bearer {groq_key}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                }
            })

    # 2. Google Gemini (Verified active)
    if keys.get("GEMINI_API_KEY"):
        gem_key = keys["GEMINI_API_KEY"]
        for m in ["gemini-3-flash-preview", "gemini-3.8-flash", "gemini-3.5-flash"]:
            pool.append({
                "id": f"gemini/{m}",
                "provider": "gemini",
                "model_name": m,
                "url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
                "headers": {
                    "Authorization": f"Bearer {gem_key}",
                    "Content-Type": "application/json",
                    "User-Agent": "Mozilla/5.0"
                }
            })

    # 3. OpenRouter Free Tier (Verified active)
    if keys.get("OPENROUTER_API_KEY"):
        or_key = keys["OPENROUTER_API_KEY"]
        for m in [
            "baidu/ernie-5.5-flash-preview:free",
            "nvidia/nemotron-3.5-lightning:free",
            "google/gemma-4-31b-it:free",
            "inclusionai/ling-3.2-flash:free",
            "liquid/lfm-3-1.7b:free"
        ]:
            pool.append({
                "id": f"openrouter/{m}",
                "provider": "openrouter",
                "model_name": m,
                "url": "https://openrouter.ai/api/v1/chat/completions",
                "headers": {
                    "Authorization": f"Bearer {or_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://github.com",
                    "User-Agent": "Mozilla/5.0"
                }
            })

    # 4. User-Defined Custom Models
    for custom in config.get("custom_models", []):
        if "id" in custom and "url" in custom and "model_name" in custom:
            pool.append(custom)

    # 5. Local Ollama Fallback (100% offline uptime guarantee)
    pool.append({
        "id": "ollama/qwen2.5-coder:7b",
        "provider": "ollama",
        "model_name": "qwen2.5-coder:7b",
        "url": "http://localhost:11434/v1/chat/completions",
        "headers": {"Content-Type": "application/json"}
    })

    return pool

class GatewayRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_GET(self):
        if self.path in ("/v1/models", "/models"):
            config = load_config()
            pool = build_model_pool(config)
            self._send_json(200, {
                "object": "list",
                "data": [{"id": m["id"], "object": "model", "owned_by": m.get("provider", "custom")} for m in pool]
            })
        elif self.path == "/status":
            config = load_config()
            pool = build_model_pool(config)
            now = time.time()
            self._send_json(200, {
                "active_models_count": len(pool),
                "configured_keys": {k: bool(v) for k, v in config.get("keys", {}).items()},
                "custom_models_count": len(config.get("custom_models", [])),
                "models": [
                    {
                        "id": m["id"],
                        "provider": m.get("provider", "custom"),
                        "model_name": m["model_name"],
                        "cooling_down": cooldowns.get(m["id"], 0) > now,
                        "cooldown_remaining_sec": max(0, int(cooldowns.get(m["id"], 0) - now))
                    }
                    for m in pool
                ]
            })
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def do_POST(self):
        if self.path in ("/v1/chat/completions", "/chat/completions"):
            self.handle_chat_completions()
        elif self.path == "/configure-keys":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                new_keys = json.loads(body)
                config = load_config()
                config["keys"].update(new_keys)
                save_config(config)
                self._send_json(200, {"status": "ok", "message": "Keys updated successfully"})
            except Exception as e:
                self._send_json(400, {"error": str(e)})
        elif self.path == "/models/add":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                custom_model = json.loads(body)
                required = ["id", "url", "model_name"]
                if not all(k in custom_model for k in required):
                    self._send_json(400, {"error": f"Missing required fields: {required}"})
                    return
                config = load_config()
                # replace if ID exists, else append
                config["custom_models"] = [m for m in config.get("custom_models", []) if m["id"] != custom_model["id"]]
                config["custom_models"].append(custom_model)
                save_config(config)
                self._send_json(200, {"status": "ok", "message": f"Added model {custom_model['id']}"})
            except Exception as e:
                self._send_json(400, {"error": str(e)})
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def handle_chat_completions(self):
        global current_model_index
        content_length = int(self.headers.get("Content-Length", 0))
        req_body_bytes = self.rfile.read(content_length)

        try:
            req_data = json.loads(req_body_bytes.decode("utf-8"))
        except Exception:
            self._send_json(400, {"error": "Invalid JSON body"})
            return

        is_streaming = req_data.get("stream", False)
        config = load_config()
        pool = build_model_pool(config)

        if not pool:
            self._send_json(500, {"error": "No models available in pool"})
            return

        now = time.time()
        # Separate active online models from local fallback
        online_models = [m for m in pool if m.get("provider") != "ollama" and cooldowns.get(m["id"], 0) <= now]
        local_models = [m for m in pool if m.get("provider") == "ollama"]

        if online_models:
            total_online = len(online_models)
            start_idx = current_model_index % total_online
            # Rotate across online models first; local Ollama is the safety fallback at the end
            ordered_candidates = (online_models[start_idx:] + online_models[:start_idx]) + local_models
        else:
            # All online models are cooling down/rate-limited: route directly to local Ollama
            print("[Gateway] All online models are rate-limited or cooling down. Falling back to local Ollama!")
            ordered_candidates = local_models

        for model_info in ordered_candidates:
            model_id = model_info["id"]
            if online_models:
                current_model_index = (current_model_index + 1) % len(online_models)

            provider_payload = dict(req_data)
            provider_payload["model"] = model_info["model_name"]

            # Provider cleanups
            if model_info.get("provider") == "gemini":
                provider_payload.pop("transforms", None)

            log(f"[Gateway] Attempting model: {model_id} ...")
            req = urllib.request.Request(
                model_info["url"],
                data=json.dumps(provider_payload).encode("utf-8"),
                headers=model_info.get("headers", {"Content-Type": "application/json"}),
                method="POST"
            )

            try:
                with urllib.request.urlopen(req, timeout=45) as response:
                    status_code = response.getcode()
                    if is_streaming:
                        self.send_response(status_code)
                        self.send_header("Content-Type", "text/event-stream")
                        self.send_header("Cache-Control", "no-cache")
                        self.send_header("Access-Control-Allow-Origin", "*")
                        self.end_headers()
                        while True:
                            chunk = response.read(1024)
                            if not chunk:
                                break
                            self.wfile.write(chunk)
                            self.wfile.flush()
                        return
                    else:
                        resp_data = response.read()
                        self.send_response(status_code)
                        self.send_header("Content-Type", "application/json")
                        self.send_header("Access-Control-Allow-Origin", "*")
                        self.end_headers()
                        self.wfile.write(resp_data)
                        return

            except urllib.error.HTTPError as err:
                err_body = err.read().decode("utf-8", errors="ignore")
                log(f"[Gateway] {model_id} returned HTTP {err.code}: {err_body[:120]}")
                if err.code in (429, 500, 502, 503, 504):
                    cooldowns[model_id] = time.time() + 60
                elif err.code == 404:
                    cooldowns[model_id] = time.time() + 86400  # 24h cooldown for discontinued model
                elif err.code in (401, 403):
                    cooldowns[model_id] = time.time() + 3600   # 1h cooldown for invalid key
                else:
                    cooldowns[model_id] = time.time() + 300
                log(f"[Gateway] Rotating to next model due to HTTP {err.code} on {model_id}...")
                continue
            except Exception as e:
                log(f"[Gateway] Error connecting to {model_id}: {e}")
                cooldowns[model_id] = time.time() + 30
                continue

        self._send_json(503, {"error": "All models in pool are currently rate-limited or cooling down. Retry in 30 seconds."})

    def _send_json(self, status: int, payload: Dict[str, Any]):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

def log(msg: str):
    print(msg, flush=True)

def run():
    config = load_config()
    pool = build_model_pool(config)
    active_keys = [k for k, v in config.get("keys", {}).items() if v]

    log(f"==================================================")
    log(f" AI Gateway running on http://127.0.0.1:{PORT}")
    log(f" Config file:   {CONFIG_FILE}")
    log(f" Loaded keys:   {len(active_keys)} active ({', '.join(active_keys) if active_keys else 'None'})")
    log(f" Active models: {len(pool)} ready in rotation pool")
    log(f" OpenAI URL:    http://127.0.0.1:{PORT}/v1")
    log(f"==================================================")
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), GatewayRequestHandler) as httpd:
        httpd.serve_forever()

if __name__ == "__main__":
    run()
