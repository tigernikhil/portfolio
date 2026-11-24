import os
import sys
import json
import urllib.request
import urllib.error
from typing import Dict, Any, List

OLLAMA_ENDPOINT = os.environ.get("OLLAMA_ENDPOINT", "http://localhost:11434")

def query_ollama(model: str, prompt: str, timeout: int = 240) -> str:
    url = f"{OLLAMA_ENDPOINT}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,
            "num_predict": 4096
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result.get("response", "").strip()

def strip_outer_fences(content: str) -> str:
    text = content.strip()
    if text.startswith("```"):
        first_newline = text.find("\n")
        if first_newline != -1:
            text = text[first_newline + 1:]
        if text.endswith("```"):
            text = text[:-3]
    return text.strip()

def save_file(path: str, content: str):
    full_path = os.path.abspath(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✓ Saved {path} ({len(content)} bytes)")

def get_integrated_tasks() -> List[Dict[str, Any]]:
    return [
        # 1. Flight Tracker Manifest
        {
            "path": "tools/productivity/flight-price-tracker/tool.manifest.json",
            "model": "qwen2.5-coder:7b",
            "prompt": """Generate a valid JSON tool manifest for a Flight Price Tracker Tool matching @platform/contracts ToolManifestSchema.
Requirements:
- id: "tool-productivity-flight-price-tracker"
- name: "Flight Price Tracker & Alert Engine"
- version: "1.0.0"
- description: "Event-driven flight tracking, price prediction, date suggestion, and email alert dispatch engine connected to external microservices at /Users/admin/Documents/FlightPriceTracker."
- category: "productivity"
- visibility: "authenticated"
- execution: {"type": "api", "reference": "/Users/admin/Documents/FlightPriceTracker"}
- capabilities: ["flight-tracking", "price-prediction", "email-alerting", "route-analytics", "user-auth"]
- inputSchema: JSON schema defining { "action": "track_route" | "predict_price" | "check_alerts", "origin": string, "destination": string, "departureDate": string, "returnDate"?: string, "targetPrice"?: number, "currency"?: string, "userEmail"?: string }
- outputSchema: JSON schema defining { "routeId": string, "currentPrice": number, "predictedDropProbability": number, "recommendation": "buy_now" | "wait" | "monitor", "alertTriggered": boolean, "emailSent": boolean, "emailDetails"?: object, "cheaperAlternativeDates"?: array }
Output ONLY raw valid JSON."""
        },
        # 2. Flight Tracker Package.json
        {
            "path": "tools/productivity/flight-price-tracker/package.json",
            "model": "qwen2.5-coder:7b",
            "prompt": """Generate package.json for @tools/flight-price-tracker.
Dependencies:
- @platform/contracts: "workspace:*"
- @platform/tool-sdk: "workspace:*"
- zod: "^3.22.4"
Scripts: "test": "vitest run".
Output ONLY raw valid JSON."""
        },
        # 3. Flight Tracker Business Logic
        {
            "path": "tools/productivity/flight-price-tracker/src/tracker.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write strict TypeScript business logic in tools/productivity/flight-price-tracker/src/tracker.ts for the Flight Price Tracker and Alert Engine.
Requirements:
- Clean Architecture / Ports & Adapters, decoupled from framework.
- User Authentication check: Requires valid user context (userId, auth permission 'tools:execute'). Throws Error('Authentication required: user session context is missing or unauthorized') if missing.
- Interfaces:
  - FlightRouteInput { action: 'track_route' | 'predict_price' | 'check_alerts'; origin: string; destination: string; departureDate: string; returnDate?: string; targetPrice?: number; currency?: string; userEmail?: string }
  - FlightPriceResult { routeId: string; origin: string; destination: string; departureDate: string; currentPrice: number; currency: string; predictedDropProbability: number; recommendation: 'buy_now' | 'wait' | 'monitor'; alertTriggered: boolean; emailSent: boolean; emailDetails?: { to: string; subject: string; template: string; sentAt: string }; cheaperAlternativeDates?: Array<{ date: string; estimatedPrice: number; savingsPercent: number }> }
- Functions / Class FlightPriceTrackerEngine:
  - calculateDropProbability(departureDate: string, currentPrice: number): number
    (Computes time-to-departure decay curve: daysLeft > 60 -> 0.72 probability, 30-60 -> 0.45, 14-30 -> 0.25, <14 -> 0.10)
  - suggestCheaperDates(departureDate: string, currentPrice: number): Array<{ date: string; estimatedPrice: number; savingsPercent: number }>
    (Scans +/- 3 days and identifies cheaper dates > 15% discount)
  - sendPriceDropEmail(to: string, route: string, currentPrice: number, targetPrice: number, currency: string): { to: string; subject: string; template: string; sentAt: string }
    (Generates transactional alert email matching docs/integrations/email.md Tool Completion / Alert template)
  - processFlightTracking(input: FlightRouteInput, userId: string, userEmail?: string): Promise<FlightPriceResult>
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 4. Flight Tracker Tool SDK Wrapper
        {
            "path": "tools/productivity/flight-price-tracker/src/index.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write tools/productivity/flight-price-tracker/src/index.ts.
Requirements:
- Import BaseTool from '@platform/tool-sdk'
- Import ToolExecutionContext from '@platform/contracts'
- Import FlightPriceTrackerEngine from './tracker'
- Import manifest from '../tool.manifest.json'
- Class FlightPriceTrackerTool extends BaseTool:
  - constructor(): calls super(manifest)
  - run(input: any, context: ToolExecutionContext):
    - Validates context.userId is present; if not, throws error 'User authentication required for Flight Price Tracker'
    - Uses FlightPriceTrackerEngine to process input
    - Returns output
- export function createTool(): FlightPriceTrackerTool
- export * from './tracker'
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 5. Flight Tracker Vitest Tests
        {
            "path": "tools/productivity/flight-price-tracker/tests/tracker.test.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write comprehensive Vitest unit tests in tools/productivity/flight-price-tracker/tests/tracker.test.ts.
Requirements:
- Test suite with 'describe', 'it', 'expect' from 'vitest'
- Test 1: Successful route tracking and price prediction when user is authenticated.
- Test 2: Price drop alert email triggered when currentPrice <= targetPrice.
- Test 3: Cheaper alternative dates suggested (>15% savings).
- Test 4: Rejection with Error when userId is missing from ToolExecutionContext (auth enforcement).
- Test 5: createTool() instantiates BaseTool subclass with valid manifest.
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 6. ClearTax Manifest
        {
            "path": "tools/finance/cleartax-filing/tool.manifest.json",
            "model": "qwen2.5-coder:7b",
            "prompt": """Generate a valid JSON tool manifest for ClearTax Tax Filing & Calculation Engine matching @platform/contracts ToolManifestSchema.
Requirements:
- id: "tool-finance-cleartax-filing"
- name: "ClearTax Filing & Computation Engine"
- version: "1.0.0"
- description: "Enterprise Indian Income Tax calculation, AIS/TIS ingestion, dual regime optimization (Old vs New), ITR generation, and transactional email filing confirmation linked to /Users/admin/Documents/Projects/ClearTax."
- category: "finance"
- visibility: "authenticated"
- execution: {"type": "embedded", "reference": "/Users/admin/Documents/Projects/ClearTax"}
- capabilities: ["itr-filing", "tax-computation", "old-vs-new-regime", "ais-tis-ingestion", "email-confirmation", "user-auth"]
- inputSchema: JSON schema defining { "pan": string, "assessmentYear": string, "salaryIncome": number, "capitalGains"?: number, "housePropertyIncome"?: number, "otherIncome"?: number, "section80C"?: number, "section80D"?: number, "hra"?: number, "userEmail"?: string, "userName"?: string }
- outputSchema: JSON schema defining { "filingId": string, "pan": string, "assessmentYear": string, "oldRegime": object, "newRegime": object, "recommendedRegime": "old" | "new", "taxSavings": number, "itrXmlGenerated": boolean, "emailConfirmationSent": boolean, "emailDetails"?: object }
Output ONLY raw valid JSON."""
        },
        # 7. ClearTax Package.json
        {
            "path": "tools/finance/cleartax-filing/package.json",
            "model": "qwen2.5-coder:7b",
            "prompt": """Generate package.json for @tools/cleartax-filing.
Dependencies:
- @platform/contracts: "workspace:*"
- @platform/tool-sdk: "workspace:*"
- zod: "^3.22.4"
Scripts: "test": "vitest run".
Output ONLY raw valid JSON."""
        },
        # 8. ClearTax Business Logic
        {
            "path": "tools/finance/cleartax-filing/src/tax-engine.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write strict TypeScript business logic in tools/finance/cleartax-filing/src/tax-engine.ts.
Requirements:
- Clean Architecture / Ports & Adapters, decoupled from express/db.
- User Authentication check: Requires valid user context (userId, PAN validation pattern [A-Z]{5}[0-9]{4}[A-Z]{1}). Throws Error if user is unauthenticated or PAN is invalid.
- Interfaces:
  - TaxInputData { pan: string; assessmentYear: string; salaryIncome: number; capitalGains?: number; housePropertyIncome?: number; otherIncome?: number; section80C?: number; section80D?: number; hra?: number; userEmail?: string; userName?: string }
  - TaxComputationResult { taxableIncome: number; incomeTax: number; surcharge: number; cess: number; rebate: number; totalTax: number }
  - ClearTaxFilingResult { filingId: string; pan: string; assessmentYear: string; grossIncome: number; oldRegime: TaxComputationResult; newRegime: TaxComputationResult; recommendedRegime: 'old' | 'new'; taxSavings: number; itrXmlSummary: string; emailConfirmationSent: boolean; emailDetails?: { to: string; subject: string; referenceId: string; sentAt: string } }
- Functions:
  - calculateOldRegime(grossIncome: number, deductions: number): TaxComputationResult
    (Slabs: <=2.5L 0%, 2.5-5L 5%, 5-10L 20%, >10L 30%; Cess 4%; Rebate 87A if taxableIncome <= 3.5L/5L)
  - calculateNewRegime(grossIncome: number): TaxComputationResult
    (Standard deduction 50,000; Slabs: <=3L 0%, 3-6L 5%, 6-9L 10%, 9-12L 15%, 12-15L 20%, >15L 30%; Rebate 87A up to 7L; Cess 4%)
  - generateItrXml(pan: string, ay: string, regime: 'old' | 'new', tax: number): string
  - sendFilingConfirmationEmail(email: string, userName: string, filingId: string, taxPayable: number, regime: string): { to: string; subject: string; referenceId: string; sentAt: string }
    (Generates transactional email matching docs/integrations/email.md and ClearTax emailService.js)
  - processClearTaxReturn(input: TaxInputData, userId: string): Promise<ClearTaxFilingResult>
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 9. ClearTax Tool SDK Wrapper
        {
            "path": "tools/finance/cleartax-filing/src/index.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write tools/finance/cleartax-filing/src/index.ts.
Requirements:
- Import BaseTool from '@platform/tool-sdk'
- Import ToolExecutionContext from '@platform/contracts'
- Import { processClearTaxReturn } from './tax-engine'
- Import manifest from '../tool.manifest.json'
- Class ClearTaxFilingTool extends BaseTool:
  - constructor(): calls super(manifest)
  - run(input: any, context: ToolExecutionContext):
    - Validates context.userId is present; if not, throws error 'User authentication required for ClearTax Filing'
    - Calls processClearTaxReturn(input, context.userId)
    - Returns output
- export function createTool(): ClearTaxFilingTool
- export * from './tax-engine'
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 10. ClearTax Vitest Tests
        {
            "path": "tools/finance/cleartax-filing/tests/tax-engine.test.ts",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write comprehensive Vitest unit tests in tools/finance/cleartax-filing/tests/tax-engine.test.ts.
Requirements:
- Test suite with 'describe', 'it', 'expect' from 'vitest'
- Test 1: Calculates Old and New regime accurately and selects New regime when deductions are low.
- Test 2: Selects Old regime when 80C and 80D deductions exceed threshold.
- Test 3: Dispatches email confirmation with reference ID and tax summary.
- Test 4: Rejects with Error when PAN is invalid or userId is missing in ToolExecutionContext.
- Test 5: Generates valid ITR XML summary.
- Test 6: createTool() instantiates BaseTool subclass with valid manifest.
Output ONLY valid TypeScript code, no markdown fences."""
        },
        # 11. Docker Compose for Deployments
        {
            "path": "deploy/docker-compose.tools.yml",
            "model": "qwen2.5-coder:7b",
            "prompt": """Generate production-grade docker-compose.tools.yml orchestrating the integrated tools.
Services:
- flight-tracker-backend:
  image: eclipse-temurin:21-jre-alpine
  environment: POSTGRES_URL, KAFKA_BOOTSTRAP_SERVERS, SMTP_USER, SMTP_PASSWORD
  ports: 8080:8080
- flight-scraper-service:
  image: mcr.microsoft.com/playwright:v1.40.0-focal
  environment: KAFKA_BOOTSTRAP_SERVERS
- cleartax-service:
  image: node:20-alpine
  environment: PORT=5000, DATABASE_URL, JWT_SECRET, SMTP_USER, SMTP_PASSWORD
  ports: 5000:5000
- platform-tool-runtime:
  image: node:20-alpine
  environment: PORT=3000, NODE_ENV=production
  ports: 3000:3000
Networks: platform-network
Volumes: pgdata, kafkadata
Output ONLY raw valid YAML without markdown fences."""
        },
        # 12. Deployment Script
        {
            "path": "deploy/deploy-tools.sh",
            "model": "qwen2.5-coder:7b",
            "prompt": """Write an executable bash production deployment script deploy/deploy-tools.sh.
Requirements:
- set -euo pipefail
- Preflight environment verification (Docker, pnpm, node 20, SMTP credentials, JWT_SECRET).
- Monorepo build step (pnpm build and test verification).
- Health check polling loop for /health endpoints on flight-tracker (8080) and cleartax (5000).
- Zero-downtime cutover and automated rollback on failure.
Output ONLY raw bash script without markdown fences."""
        },
        # 13. Integration Doc for Flight Tracker
        {
            "path": "docs/integrations/flight-price-tracker.md",
            "model": "qwen2.5:3b",
            "prompt": """Write a comprehensive integration specification in docs/integrations/flight-price-tracker.md linking /Users/admin/Documents/FlightPriceTracker with the Personal Technology Platform.
Sections:
1. Architecture Overview (Spring Boot 3, Kafka event-driven choreography, Playwright scraper).
2. User Authentication & Login Boundary (JWT claims, user context requirement).
3. End-to-End Email Notification Architecture (price drop trigger, threshold evaluation, SMTP delivery).
4. Tool SDK Adapter (@tools/flight-price-tracker).
5. Operational Runbook & Deployment (Kafka topics, Docker Compose, failover)."""
        },
        # 14. Integration Doc for ClearTax
        {
            "path": "docs/integrations/cleartax.md",
            "model": "qwen2.5:3b",
            "prompt": """Write a comprehensive integration specification in docs/integrations/cleartax.md linking /Users/admin/Documents/Projects/ClearTax with the Personal Technology Platform.
Sections:
1. Architecture Overview (Express backend, calculation engines, AIS/TIS ingestion).
2. User Authentication & PAN Verification Protocol (session context, RBAC).
3. Dual-Regime Tax Computation Engine (Old vs New regime mathematical rules).
4. End-to-End Email Service Protocol (filing reminder, filing confirmation, reference ID).
5. Tool SDK Adapter (@tools/cleartax-filing).
6. Operational Runbook & Deployment (PostgreSQL, Docker Compose, compliance)."""
        },
        # 15. Learned Skill for Authenticated Tool Integration
        {
            "path": "agent-resources/learned-skills/authenticated-tool-integration/SKILL.md",
            "model": "qwen2.5:3b",
            "prompt": """Write an in-depth agent skill in agent-resources/learned-skills/authenticated-tool-integration/SKILL.md following the agent governance policy in AGENTS.md.
Frontmatter:
---
name: authenticated-tool-integration
description: Blueprint for integrating external legacy or microservice tools requiring user authentication, session validation, and transactional email notification into the Personal Technology Platform monorepo.
---
Body:
1. Architectural Pattern (Hexagonal Ports & Adapters, wrapping external REST/Microservice systems into BaseTool).
2. Authentication Enforcement Guard (rejecting unauthenticated requests, validating context.userId and permissions).
3. Transactional Email Pipeline (matching docs/integrations/email.md, decoupled notification dispatcher).
4. Test Verification Pattern with Vitest (testing auth guards, domain calculation, and email delivery).
5. Continuous Self-Improvement Protocol."""
        }
    ]

def main():
    print("Starting generation of integrated tools via local Ollama...")
    tasks = get_integrated_tasks()
    total = len(tasks)
    
    for idx, task in enumerate(tasks, start=1):
        path = task["path"]
        model = task["model"]
        prompt = task["prompt"]
        print(f"[{idx}/{total}] [{model}] Generating {path}...")
        try:
            raw_content = query_ollama(model=model, prompt=prompt, timeout=240)
            cleaned_content = strip_outer_fences(raw_content)
            save_file(path, cleaned_content)
            print(f"[{idx}/{total}] Successfully finished {path}")
        except Exception as e:
            print(f"[{idx}/{total}] Error generating {path}: {e}")

    print("\nAll integrated tools generated!")

if __name__ == "__main__":
    main()
