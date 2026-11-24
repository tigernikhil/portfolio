import { z } from 'zod';

// Define enums
export enum ToolCategory {
  finance = 'finance',
  productivity = 'productivity',
  ai = 'ai',
  developer = 'developer',
  automation = 'automation'
}

export enum ToolVisibility {
  public = 'public',
  authenticated = 'authenticated',
  restricted = 'restricted',
  private = 'private'
}

export enum ExecutionType {
  embedded = 'embedded',
  edge = 'edge',
  api = 'api',
  job = 'job',
  mcp = 'mcp',
  local = 'local'
}

// Define Zod schema
export const ToolManifestSchema = z.object({
  id: z.string(),
  name: z.string(),
  version: z.string(),
  description: z.string(),
  category: z.enum([ToolCategory.finance, ToolCategory.productivity, ToolCategory.ai, ToolCategory.developer, ToolCategory.automation]),
  visibility: z.enum([ToolVisibility.public, ToolVisibility.authenticated, ToolVisibility.restricted, ToolVisibility.private]),
  execution: z.object({
    type: z.enum([ExecutionType.embedded, ExecutionType.edge, ExecutionType.api, ExecutionType.job, ExecutionType.mcp, ExecutionType.local]),
    reference: z.string()
  }),
  capabilities: z.array(z.string()),
  inputSchema: z.record(z.unknown()),
  outputSchema: z.record(z.unknown()),
  author: z.string().optional(),
  createdAt: z.string().optional()
});

// Define TypeScript type
export type ToolManifest = z.infer<typeof ToolManifestSchema>;
