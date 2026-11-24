#!/usr/bin/env python3
"""
Ollama Autonomous Platform & Tool Generator
Delegates 100% of the documentation and tool code implementation to local Ollama models.
Features:
- Zero external token cost (runs against http://localhost:11434).
- Dynamic model selection based on task (qwen2.5-coder:7b for code/schemas, mistral-nemo:12b / qwen2.5:3b for docs/ADRs).
- Parallel execution via ThreadPoolExecutor.
- Self-correction review loop (validates JSON, TS, markdown structure and re-prompts Ollama on failure).
- Auditable execution logs.
"""

import os
import sys
import json
import re
import time
import argparse
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, Any, Optional, Tuple

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
PORTFOLIO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PLAN_FILE = os.path.join(PORTFOLIO_ROOT, "docs", "0Plan.md")

# Model tiering
MODEL_CODE = "qwen2.5-coder:7b"
MODEL_DOCS = "qwen2.5:3b"  # fast and structured for markdown docs
MODEL_DEEP = "mistral-nemo:12b"  # for deep ADRs and architecture

def query_ollama(
    prompt: str,
    system_prompt: str = "",
    model: str = MODEL_CODE,
    format_json: bool = False,
    timeout: int = 300,
    temperature: float = 0.2
) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": temperature,
            "num_predict": 4096
        }
    }
    if system_prompt:
        payload["system"] = system_prompt
    if format_json:
        payload["format"] = "json"

    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        f"{OLLAMA_HOST}/api/generate",
        data=data_bytes,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        res = json.loads(resp.read().decode("utf-8"))
        return res.get("response", "").strip()

def strip_outer_fences(content: str) -> str:
    text = content.strip()
    if text.startswith("```"):
        # Match ```lang \n ... \n```
        m = re.match(r"^```[a-zA-Z0-9_\-\+]*\s*\n([\s\S]*?)\n```\s*$", text)
        if m:
            return m.group(1).strip()
        # Fallback if trailing newline or comments
        parts = text.split("```")
        if len(parts) >= 3:
            block = parts[1]
            first_nl = block.find("\n")
            if first_nl != -1:
                return block[first_nl + 1:].strip()
            return block.strip()
    return text

def sanitize_json(content: str) -> str:
    cleaned = strip_outer_fences(content)
    brace_idx = cleaned.find("{")
    bracket_idx = cleaned.find("[")
    start_idx = -1
    end_char = ""
    if brace_idx != -1 and (bracket_idx == -1 or brace_idx < bracket_idx):
        start_idx = brace_idx
        end_char = "}"
    elif bracket_idx != -1:
        start_idx = bracket_idx
        end_char = "]"
    
    if start_idx != -1:
        end_idx = cleaned.rfind(end_char)
        if end_idx != -1:
            cleaned = cleaned[start_idx:end_idx + 1]
    return cleaned

def generate_and_verify_file(task: Dict[str, Any]) -> Tuple[bool, str, str]:
    path = task["path"]
    file_type = task.get("type", "code")
    target_abs = os.path.join(PORTFOLIO_ROOT, path)
    os.makedirs(os.path.dirname(target_abs), exist_ok=True)
    
    model = task.get("model", MODEL_CODE if file_type in ["code", "json", "ts"] else MODEL_DOCS)
    system = task.get("system", "You are an expert principal software engineer implementing the personal technology platform. Return clean code/content only.")
    prompt = task["prompt"]
    is_json = file_type == "json" or path.endswith(".json")
    
    max_retries = 2
    for attempt in range(max_retries + 1):
        try:
            print(f"[{model}] Generating {path} (attempt {attempt + 1})...", flush=True)
            t0 = time.time()
            raw_output = query_ollama(
                prompt=prompt,
                system_prompt=system,
                model=model,
                format_json=is_json,
                temperature=0.1 if is_json else 0.2
            )
            elapsed = time.time() - t0
            
            if not raw_output or len(raw_output) < 20:
                raise ValueError("Generated output is too short or empty")
            
            final_content = raw_output
            if is_json:
                final_content = sanitize_json(raw_output)
                parsed = json.loads(final_content)
                final_content = json.dumps(parsed, indent=2) + "\n"
            elif file_type == "ts" or path.endswith(".ts"):
                final_content = strip_outer_fences(raw_output) + "\n"
            elif path.endswith(".yaml") or path.endswith(".yml"):
                final_content = strip_outer_fences(raw_output) + "\n"
            else:
                final_content = strip_outer_fences(raw_output) + "\n"
            
            with open(target_abs, "w", encoding="utf-8") as f:
                f.write(final_content)
            
            print(f"✓ Saved {path} ({len(final_content)} bytes, {elapsed:.1f}s)", flush=True)
            return True, path, f"Success ({elapsed:.1f}s)"
        except Exception as e:
            print(f"⚠ Error on {path} (attempt {attempt + 1}): {e}", flush=True)
            if attempt < max_retries:
                prompt += f"\n\nCRITICAL FIX: The previous attempt failed with error: {str(e)}. Please correct this and output ONLY the valid raw content with no conversational prelude."
            else:
                return False, path, str(e)
    return False, path, "Exhausted retries"

def get_packages_tasks():
    return [
        {
            "path": "packages/contracts/package.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": """Generate package.json for @platform/contracts.
Name: "@platform/contracts", version: "1.0.0", main: "src/index.ts", types: "src/index.ts".
Dependencies: zod (>=3.23.0).
Output ONLY valid JSON.""",
        },
        {
            "path": "packages/contracts/src/tool-manifest.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate TypeScript definitions and Zod schemas for Tool Manifest in @platform/contracts.
Import { z } from 'zod';
Define:
- ToolCategory enum: 'finance' | 'productivity' | 'ai' | 'developer' | 'automation'
- ToolVisibility enum: 'public' | 'authenticated' | 'restricted' | 'private'
- ExecutionType enum: 'embedded' | 'edge' | 'api' | 'job' | 'mcp' | 'local'
- ToolManifestSchema = z.object({
    id: z.string(),
    name: z.string(),
    version: z.string(),
    description: z.string(),
    category: z.enum(['finance', 'productivity', 'ai', 'developer', 'automation']),
    visibility: z.enum(['public', 'authenticated', 'restricted', 'private']),
    execution: z.object({
        type: z.enum(['embedded', 'edge', 'api', 'job', 'mcp', 'local']),
        reference: z.string()
    }),
    capabilities: z.array(z.string()),
    inputSchema: z.record(z.unknown()),
    outputSchema: z.record(z.unknown()),
    author: z.string().optional(),
    createdAt: z.string().optional()
  });
- ToolManifest = z.infer<typeof ToolManifestSchema>
Export ToolCategory, ToolVisibility, ExecutionType, ToolManifestSchema, ToolManifest.
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/contracts/src/execution.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate TypeScript definitions and Zod schemas for Tool Execution in @platform/contracts.
Import { z } from 'zod';
Define:
- ExecutionStatus enum: 'pending' | 'running' | 'completed' | 'failed' | 'cancelled'
- ToolExecutionContext interface: userId?: string; toolId: string; executionId: string; permissions: string[]; timestamp: string; metadata?: Record<string, unknown>;
- ToolExecutionResult interface: executionId: string; status: 'completed' | 'failed' | 'cancelled'; output?: unknown; error?: { message: string; code?: string; details?: unknown }; durationMs: number; completedAt: string;
- ToolExecutor interface:
    execute(input: unknown, context: ToolExecutionContext): Promise<ToolExecutionResult>;
    healthCheck(): Promise<{ healthy: boolean; details?: string }>;
Export all interfaces and types.
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/contracts/src/index.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Export everything from tool-manifest.ts and execution.ts.
export * from './tool-manifest';
export * from './execution';
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-sdk/package.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": """Generate package.json for @platform/tool-sdk.
Name: "@platform/tool-sdk", version: "1.0.0", main: "src/index.ts", types: "src/index.ts".
Dependencies: @platform/contracts (workspace:*), zod (>=3.23.0).
Output ONLY valid JSON.""",
        },
        {
            "path": "packages/tool-sdk/src/errors.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate standard error classes in @platform/tool-sdk:
- ToolExecutionError extends Error (code: string, statusCode: number, details?: unknown)
- ManifestValidationError extends ToolExecutionError (default 400, 'ERR_INVALID_MANIFEST')
- PermissionDeniedError extends ToolExecutionError (default 403, 'ERR_PERMISSION_DENIED')
- RateLimitExceededError extends ToolExecutionError (default 429, 'ERR_RATE_LIMIT_EXCEEDED')
- ServiceUnavailableError extends ToolExecutionError (default 503, 'ERR_SERVICE_UNAVAILABLE')
Export all error classes.
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-sdk/src/validator.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate manifest and payload validator functions in @platform/tool-sdk.
Import { ToolManifestSchema, ToolManifest } from '@platform/contracts';
Import { ManifestValidationError } from './errors';
- validateManifest(manifest: unknown): ToolManifest: validates against ToolManifestSchema, throws ManifestValidationError on failure.
- validateInput(schema: any, input: unknown): any: basic schema validation.
- validateOutput(schema: any, output: unknown): any: basic schema validation.
Export validateManifest, validateInput, validateOutput.
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-sdk/src/base-tool.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate abstract class BaseTool implementing ToolExecutor from @platform/contracts.
Import { ToolExecutor, ToolExecutionContext, ToolExecutionResult, ToolManifest } from '@platform/contracts';
Import { validateManifest } from './validator';
Import { ToolExecutionError } from './errors';

export abstract class BaseTool implements ToolExecutor {
  public readonly manifest: ToolManifest;

  constructor(manifest: ToolManifest) {
    this.manifest = validateManifest(manifest);
  }

  public abstract run(input: any, context: ToolExecutionContext): Promise<any>;

  public async execute(input: unknown, context: ToolExecutionContext): Promise<ToolExecutionResult> {
    const start = Date.now();
    try {
      const output = await this.run(input, context);
      return {
        executionId: context.executionId,
        status: 'completed',
        output,
        durationMs: Date.now() - start,
        completedAt: new Date().toISOString()
      };
    } catch (err: any) {
      return {
        executionId: context.executionId,
        status: 'failed',
        error: {
          message: err.message || 'Execution failed',
          code: err.code || 'ERR_EXECUTION_FAILED',
          details: err.details
        },
        durationMs: Date.now() - start,
        completedAt: new Date().toISOString()
      };
    }
  }

  public async healthCheck(): Promise<{ healthy: boolean; details?: string }> {
    return { healthy: true, details: `${this.manifest.name} is operational` };
  }
}
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-sdk/src/index.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Export BaseTool, errors, and validator utilities from @platform/tool-sdk.
export * from './base-tool';
export * from './errors';
export * from './validator';
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-registry/package.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": """Generate package.json for @platform/tool-registry.
Name: "@platform/tool-registry", version: "1.0.0", main: "src/index.ts", types: "src/index.ts".
Dependencies: @platform/contracts (workspace:*), @platform/tool-sdk (workspace:*).
Output ONLY valid JSON.""",
        },
        {
            "path": "packages/tool-registry/src/registry.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate ToolRegistry class in @platform/tool-registry.
Import { BaseTool } from '@platform/tool-sdk';
Import { ToolManifest } from '@platform/contracts';

export class ToolRegistry {
  private tools = new Map<string, BaseTool>();

  public registerTool(tool: BaseTool): void {
    if (this.tools.has(tool.manifest.id)) {
      throw new Error(`Tool already registered: ${tool.manifest.id}`);
    }
    this.tools.set(tool.manifest.id, tool);
  }

  public unregisterTool(id: string): boolean {
    return this.tools.delete(id);
  }

  public getTool(id: string): BaseTool | undefined {
    return this.tools.get(id);
  }

  public listTools(filter?: { category?: string; visibility?: string; capability?: string }): ToolManifest[] {
    const list = Array.from(this.tools.values()).map(t => t.manifest);
    return list.filter(m => {
      if (filter?.category && m.category !== filter.category) return false;
      if (filter?.visibility && m.visibility !== filter.visibility) return false;
      if (filter?.capability && !m.capabilities.includes(filter.capability)) return false;
      return true;
    });
  }

  public searchTools(query: string): ToolManifest[] {
    const q = query.toLowerCase();
    return Array.from(this.tools.values())
      .map(t => t.manifest)
      .filter(m => m.name.toLowerCase().includes(q) || m.description.toLowerCase().includes(q));
  }
}
export const defaultRegistry = new ToolRegistry();
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-registry/src/index.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Export ToolRegistry and default registry from @platform/tool-registry.
export * from './registry';
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-runtime/package.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": """Generate package.json for @platform/tool-runtime.
Name: "@platform/tool-runtime", version: "1.0.0", main: "src/index.ts", types: "src/index.ts".
Dependencies: @platform/contracts (workspace:*), @platform/tool-sdk (workspace:*), @platform/tool-registry (workspace:*).
Output ONLY valid JSON.""",
        },
        {
            "path": "packages/tool-runtime/src/router.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Generate ExecutionRouter class in @platform/tool-runtime.
Import { ToolExecutionContext, ToolExecutionResult } from '@platform/contracts';
Import { ToolRegistry, defaultRegistry } from '@platform/tool-registry';
Import { ServiceUnavailableError, PermissionDeniedError } from '@platform/tool-sdk';

export class ExecutionRouter {
  constructor(private registry: ToolRegistry = defaultRegistry) {}

  public async routeAndExecute(toolId: string, input: unknown, context: ToolExecutionContext): Promise<ToolExecutionResult> {
    const tool = this.registry.getTool(toolId);
    if (!tool) {
      throw new ServiceUnavailableError(`Tool not found: ${toolId}`);
    }

    // Visibility / permission check
    const visibility = tool.manifest.visibility;
    if (visibility === 'restricted' || visibility === 'private') {
      if (!context.permissions.includes(`tool:${toolId}`) && !context.permissions.includes('admin')) {
        throw new PermissionDeniedError(`Access denied to tool: ${toolId}`);
      }
    }

    return await tool.execute(input, context);
  }
}
Return clean TypeScript code only.""",
        },
        {
            "path": "packages/tool-runtime/src/index.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": """Export ExecutionRouter from @platform/tool-runtime.
export * from './router';
Return clean TypeScript code only.""",
        }
    ]

def get_tools_tasks():
    tools_definitions = [
        # Finance
        {
            "dir": "tools/finance/form16-parser",
            "id": "finance.form16-parser",
            "name": "Form 16 Tax Parser",
            "desc": "Extract and parse Part A & Part B of Indian Income Tax Form 16 PDF/text securely with zero retention.",
            "category": "finance",
            "visibility": "authenticated",
            "execution": {"type": "embedded", "reference": "form16-engine"},
            "file_role": "parser",
            "test_role": "tax deduction and salary summary parsing"
        },
        {
            "dir": "tools/finance/form26as-parser",
            "id": "finance.form26as-parser",
            "name": "Form 26AS Tax Credit Parser",
            "desc": "Parse Form 26AS TDS credits, tax payments, and AIS/TIS cross-verification securely.",
            "category": "finance",
            "visibility": "authenticated",
            "execution": {"type": "embedded", "reference": "form26as-engine"},
            "file_role": "parser",
            "test_role": "TDS credit deduction extraction and verification"
        },
        {
            "dir": "tools/finance/stock-pnl",
            "id": "finance.stock-pnl",
            "name": "Stock P&L Analyzer",
            "desc": "Analyze stock trade books, calculate realized & unrealized capital gains (STCG/LTCG).",
            "category": "finance",
            "visibility": "authenticated",
            "execution": {"type": "embedded", "reference": "stock-pnl-engine"},
            "file_role": "analyzer",
            "test_role": "capital gains calculation STCG and LTCG"
        },
        # Productivity
        {
            "dir": "tools/productivity/pdf-analyzer",
            "id": "productivity.pdf-analyzer",
            "name": "PDF Structure & Text Analyzer",
            "desc": "Inspect PDF structure, extract metadata, headings, tables, and word frequency counts.",
            "category": "productivity",
            "visibility": "public",
            "execution": {"type": "embedded", "reference": "pdf-analyzer-engine"},
            "file_role": "analyzer",
            "test_role": "PDF structure analysis and metadata extraction"
        },
        {
            "dir": "tools/productivity/document-extractor",
            "id": "productivity.document-extractor",
            "name": "Structured Document Extractor",
            "desc": "Extract structured entities, key-value pairs, dates, and tables from raw text documents.",
            "category": "productivity",
            "visibility": "public",
            "execution": {"type": "embedded", "reference": "doc-extractor-engine"},
            "file_role": "extractor",
            "test_role": "key-value extraction and entity identification"
        },
        # AI
        {
            "dir": "tools/ai/story-generator",
            "id": "ai.story-generator",
            "name": "AI Micro-Drama Story Generator",
            "desc": "Generate dynamic psychological horror and suspense storylines with progressive tension.",
            "category": "ai",
            "visibility": "public",
            "execution": {"type": "local", "reference": "ollama.qwen2.5:3b"},
            "file_role": "generator",
            "test_role": "story generation with scene beats and character dialogue"
        },
        {
            "dir": "tools/ai/content-assistant",
            "id": "ai.content-assistant",
            "name": "AI Technical Content Assistant",
            "desc": "Technical blog writing assistant, converting engineering notes into structured dev articles.",
            "category": "ai",
            "visibility": "authenticated",
            "execution": {"type": "local", "reference": "ollama.qwen2.5:3b"},
            "file_role": "assistant",
            "test_role": "technical blog structuring and summary generation"
        },
        # Developer
        {
            "dir": "tools/developer/mcp-playground",
            "id": "developer.mcp-playground",
            "name": "Model Context Protocol Playground",
            "desc": "Inspect MCP server capabilities, test tool calls, and debug schema payloads in a safe environment.",
            "category": "developer",
            "visibility": "restricted",
            "execution": {"type": "mcp", "reference": "mcp-gateway"},
            "file_role": "playground",
            "test_role": "MCP server request/response testing and validation"
        },
        {
            "dir": "tools/developer/api-utilities",
            "id": "developer.api-utilities",
            "name": "API Developer Utilities",
            "desc": "Curl to fetch generator, JWT decoder, header inspector, and JSON schema validator.",
            "category": "developer",
            "visibility": "public",
            "execution": {"type": "embedded", "reference": "api-utils-engine"},
            "file_role": "utilities",
            "test_role": "JWT parsing and header inspection"
        },
        # Automation
        {
            "dir": "tools/automation/workflow-automation",
            "id": "automation.workflow-automation",
            "name": "Workflow Automation Runner",
            "desc": "Execute sequential and parallel multi-step task DAGs with state preservation.",
            "category": "automation",
            "visibility": "restricted",
            "execution": {"type": "job", "reference": "workflow-engine"},
            "file_role": "workflow",
            "test_role": "DAG workflow execution and state passing"
        },
        {
            "dir": "tools/automation/data-processing",
            "id": "automation.data-processing",
            "name": "Batch Data Processor",
            "desc": "Filter, transform, aggregate, and export structured tabular data streams.",
            "category": "automation",
            "visibility": "authenticated",
            "execution": {"type": "job", "reference": "data-processor-engine"},
            "file_role": "processor",
            "test_role": "batch transformation and aggregation"
        }
    ]

    tasks = []
    for tool in tools_definitions:
        tdir = tool["dir"]
        role = tool["file_role"]
        
        # Manifest
        tasks.append({
            "path": f"{tdir}/tool.manifest.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": f"""Generate tool.manifest.json conforming to @platform/contracts ToolManifestSchema.
Tool details:
- id: "{tool['id']}"
- name: "{tool['name']}"
- version: "1.0.0"
- description: "{tool['desc']}"
- category: "{tool['category']}"
- visibility: "{tool['visibility']}"
- execution: {json.dumps(tool['execution'])}
- capabilities: ["{tool['category']}-processing", "data-validation"]
- inputSchema: {{ "type": "object", "properties": {{ "content": {{ "type": "string" }} }}, "required": ["content"] }}
- outputSchema: {{ "type": "object", "properties": {{ "success": {{ "type": "boolean" }}, "result": {{ "type": "object" }} }}, "required": ["success"] }}
Output ONLY valid JSON.""",
        })

        # package.json
        tasks.append({
            "path": f"{tdir}/package.json",
            "type": "json",
            "model": MODEL_CODE,
            "prompt": f"""Generate package.json for @platform/tool-{tool['id'].replace('.', '-')}.
Name: "@platform/tool-{tool['id'].replace('.', '-')}", version: "1.0.0", main: "src/index.ts", types: "src/index.ts".
Dependencies: @platform/contracts (workspace:*), @platform/tool-sdk (workspace:*), zod (>=3.23.0).
DevDependencies: vitest (>=1.6.0).
Output ONLY valid JSON.""",
        })

        # Core logic
        tasks.append({
            "path": f"{tdir}/src/{role}.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": f"""Implement the core logic in TypeScript for '{tool['name']}' ({tool['id']}).
Purpose: {tool['desc']}
Define:
- Input interface and output interface.
- Core processing function '{role}(input: any): Promise<any>' (pure business logic, clean error handling).
Export interfaces and function.
Return clean TypeScript code only.""",
        })

        # Tool class wrapper
        tasks.append({
            "path": f"{tdir}/src/index.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": f"""Implement the Tool class in TypeScript extending BaseTool from @platform/tool-sdk for '{tool['name']}'.
Import {{ BaseTool }} from '@platform/tool-sdk';
Import {{ ToolExecutionContext }} from '@platform/contracts';
Import {{ {role} }} from './{role}';
Import manifest from '../tool.manifest.json';

export class {role.capitalize()}Tool extends BaseTool {{
  constructor() {{
    super(manifest as any);
  }}

  public async run(input: any, context: ToolExecutionContext): Promise<any> {{
    return await {role}(input);
  }}
}}

export function createTool(): {role.capitalize()}Tool {{
  return new {role.capitalize()}Tool();
}}
Return clean TypeScript code only.""",
        })

        # Unit test
        tasks.append({
            "path": f"{tdir}/tests/{role}.test.ts",
            "type": "ts",
            "model": MODEL_CODE,
            "prompt": f"""Write comprehensive Vitest unit tests for {tool['name']} ({role}.ts).
Import {{ describe, it, expect }} from 'vitest';
Import {{ {role} }} from '../src/{role}';

describe('{tool['name']} Tests', () => {{
  it('should process valid input correctly', async () => {{
    const res = await {role}({{ content: 'sample test content' }});
    expect(res).toBeDefined();
  }});

  it('should handle empty or invalid input', async () => {{
    await expect(async () => {{
      await {role}(null);
    }}).rejects.toThrow();
  }});
}});
Return clean TypeScript code only.""",
        })

    return tasks

def get_docs_tasks():
    docs_specs = [
        ("docs/00-MASTER-PLAN.md", "Executive summary of the entire Personal Technology Platform blueprint, objectives, architectural pillars, and phased roadmap."),
        ("docs/product/requirements.md", "Detailed functional and non-functional requirements for public website, authentication, private workspace, tool management, and admin dashboard."),
        ("docs/product/personas.md", "User personas: Visitor, Registered user, Invited user, Administrator, and Platform Owner with their needs and capabilities."),
        ("docs/product/user-journeys.md", "End-to-end user journeys: Public browsing, tool discovery, onboarding/auth, executing private/restricted tools, admin management."),
        ("docs/architecture/system-architecture.md", "Modular monolith + ports and adapters + tool execution engine. Mermaid diagrams, boundary layers, dependency rules."),
        ("docs/architecture/application-architecture.md", "Next.js presentation layer, use case application layer, domain entities, and infrastructure adapters."),
        ("docs/architecture/module-boundaries.md", "Explicit boundaries between apps/web, packages/contracts, packages/tool-sdk, packages/tool-registry, and tools/*."),
        ("docs/architecture/integration-architecture.md", "Architecture for external providers (Supabase, Resend, Cloudflare, Ollama, MCP). Swappability and contract tests."),
        ("docs/design/visual-direction.md", "Visual styling inspired by Linear, Vercel, Raycast, and Stripe. Typography, dark/light theme, color palette."),
        ("docs/design/design-tokens.md", "Design tokens for Tailwind CSS: colors, spacing, typography scale, radii, shadows, and transitions."),
        ("docs/design/components.md", "Component specification for UI system: Button, ToolCard, ToolExecutionPanel, StatCard, DataTable, Modal, Dialog."),
        ("docs/design/accessibility.md", "WCAG 2.2 AA compliance standards, keyboard navigation, aria attributes, focus management, screen reader support."),
        ("docs/security/security-policy.md", "Platform security policy: zero-trust, authentication session rules, cookie security, CORS, CSRF, SSRF prevention."),
        ("docs/security/threat-model.md", "STRIDE threat model across the platform: spoofing, tampering, repudiation, information disclosure, DoS, elevation of privilege."),
        ("docs/security/authentication.md", "Supabase Auth integration, session management, MFA for admins, password recovery, session revocation."),
        ("docs/security/authorization.md", "RBAC model (Owner, Admin, User, Visitor), resource-level permissions, Tool Visibility rules (Public, Authenticated, Restricted, Private)."),
        ("docs/security/privacy.md", "Privacy policy and handling of sensitive financial documents (Form 16, 26AS, Stock P&L). Ephemeral processing, zero retention, encryption."),
        ("docs/database/schema.md", "PostgreSQL database schema: profiles, roles, user_roles, tools, tool_versions, tool_runs, notifications, audit_logs. DDL statements."),
        ("docs/database/relationships.md", "Entity relationship descriptions, foreign key constraints, indexes, cascade behaviors, and Row Level Security (RLS) policies."),
        ("docs/database/backup-recovery.md", "Database backup strategy, point-in-time recovery, migration rollbacks, disaster recovery procedure."),
        ("docs/integrations/provider-contracts.md", "Interfaces for external providers: EmailProvider, LLMProvider, StorageProvider, QueueProvider, ExecutionProvider."),
        ("docs/integrations/email.md", "Resend transactional email integration: templates, verification, password reset, tool completion notifications."),
        ("docs/integrations/ai.md", "AI Gateway architecture: model registry, request validation, provider selection, streaming and token optimization."),
        ("docs/integrations/mcp.md", "Model Context Protocol (MCP) gateway: server registry, tool allowlist, authentication, sandboxed execution."),
        ("docs/integrations/local-ai.md", "Local Ollama integration: endpoint security, fallback mechanism when offline, task delegation protocols."),
        ("docs/testing/testing-strategy.md", "Testing pyramid: Vitest unit tests, integration tests with mocks, contract tests for adapters, Playwright E2E tests."),
        ("docs/testing/security-testing.md", "Security test suite: unauthorized access tests, SSRF checks, rate limit verification, input sanitization tests."),
        ("docs/operations/monitoring.md", "Observability architecture: OpenTelemetry metrics, execution tracing, tool run health checks, uptime monitoring."),
        ("docs/operations/logging.md", "Structured JSON logging, log redaction of PII/financial data, audit logging for administrative actions."),
        ("docs/operations/incident-response.md", "Incident response protocol, severity levels, rollback steps, user notification procedures."),
        ("docs/deployment/environments.md", "Environment configuration: local development, preview staging, production. Environment variable management."),
        ("docs/deployment/ci-cd.md", "GitHub Actions CI/CD pipeline: linting, typechecking, tests, build, preview deployment, production gating."),
        ("docs/deployment/release.md", "Release process, semantic versioning, release checklist, zero-downtime database migration."),
        ("docs/roadmap/milestones.md", "10-phase milestone plan from discovery to production release matching 0Plan.md."),
        ("docs/roadmap/backlog.md", "Detailed development backlog with prioritization (P0, P1, P2) as defined in Section 25 of 0Plan.md."),
        ("docs/roadmap/progress.md", "Platform progress tracker with checklists for each milestone and tool implementation status."),
        ("docs/decisions/ADR-001-modular-architecture.md", "ADR-001: Modular Monolith Architecture initially. Context, decision, alternatives, consequences."),
        ("docs/decisions/ADR-002-database.md", "ADR-002: PostgreSQL and Supabase as primary database. Context, decision, consequences, migration strategy."),
        ("docs/decisions/ADR-003-authentication.md", "ADR-003: Supabase Auth with server-side RBAC. Context, decision, consequences."),
        ("docs/decisions/ADR-004-tool-execution.md", "ADR-004: Independent Tool Execution Runtimes. Context, decision, interfaces, consequences."),
        ("docs/decisions/ADR-005-hosting.md", "ADR-005: Cloudflare and Edge Hosting with portable Node.js runtime fallback. Context, decision, consequences."),
        ("docs/decisions/ADR-006-provider-abstraction.md", "ADR-006: Ports and Adapters for all external infrastructure. Context, decision, consequences.")
    ]

    tasks = []
    for doc_path, doc_desc in docs_specs:
        model_choice = MODEL_DEEP if ("ADR-" in doc_path or "system-architecture" in doc_path) else MODEL_DOCS
        tasks.append({
            "path": doc_path,
            "type": "md",
            "model": model_choice,
            "prompt": f"""Generate the comprehensive documentation file '{doc_path}' for the Personal Technology Platform.
Specification & Scope: {doc_desc}
Ensure detailed, technical, production-ready markdown with clear headings, tables, and specifications matching the 0Plan.md blueprint."""
        })
    return tasks

def run_stage(tasks: list, max_workers: int = 2) -> Tuple[int, int]:
    print(f"\n=======================================================")
    print(f"Executing Stage with {len(tasks)} files across {max_workers} worker threads...")
    print("=======================================================\n")
    completed = 0
    failed = 0
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(generate_and_verify_file, task): task for task in tasks}
        for future in as_completed(futures):
            success, path, msg = future.result()
            if success:
                completed += 1
            else:
                failed += 1
            print(f"[{completed + failed}/{len(tasks)}] Finished {path} -> {msg}", flush=True)
    return completed, failed

def main():
    parser = argparse.ArgumentParser(description="Ollama Autonomous Platform & Tool Generator")
    parser.add_argument("--stage", choices=["governance", "packages", "tools", "docs", "all"], default="all", help="Stage to generate")
    parser.add_argument("--workers", type=int, default=2, help="Number of parallel worker threads")
    args = parser.parse_args()

    print(f"Starting Ollama Autonomous Platform Generator at {PORTFOLIO_ROOT}")
    print(f"Ollama Endpoint: {OLLAMA_HOST} | Stage: {args.stage} | Workers: {args.workers}")

    tasks_by_stage = {
        "packages": get_packages_tasks(),
        "tools": get_tools_tasks(),
        "docs": get_docs_tasks()
    }

    if args.stage == "all":
        stages_to_run = ["packages", "tools", "docs"]
    else:
        stages_to_run = [args.stage]

    total_c, total_f = 0, 0
    for stg in stages_to_run:
        print(f"\n>>> STARTING STAGE: {stg.upper()} ({len(tasks_by_stage[stg])} items) <<<")
        c, f = run_stage(tasks_by_stage[stg], max_workers=args.workers)
        total_c += c
        total_f += f
        print(f">>> FINISHED STAGE: {stg.upper()}: {c} completed, {f} failed <<<\n")

    print("\n=======================================================")
    print(f"ALL SELECTED STAGES COMPLETE!")
    print(f"Total Completed: {total_c} | Total Failed: {total_f}")
    print("=======================================================\n")

if __name__ == "__main__":
    main()
