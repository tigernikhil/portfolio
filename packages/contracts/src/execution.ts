import { z } from 'zod';

// Define the ExecutionStatus enum
export enum ExecutionStatus {
  pending = 'pending',
  running = 'running',
  completed = 'completed',
  failed = 'failed',
  cancelled = 'cancelled',
}

// Define the ToolExecutionContext interface
export interface ToolExecutionContext {
  userId?: string;
  toolId: string;
  executionId: string;
  permissions: string[];
  timestamp: string;
  metadata?: Record<string, unknown>;
}

// Define the ToolExecutionResult interface
export interface ToolExecutionResult {
  executionId: string;
  status: 'completed' | 'failed' | 'cancelled';
  output?: unknown;
  error?: { message: string; code?: string; details?: unknown };
  durationMs: number;
  completedAt: string;
}

// Define the ToolExecutor interface
export interface ToolExecutor {
  execute(input: unknown, context: ToolExecutionContext): Promise<ToolExecutionResult>;
  healthCheck(): Promise<{ healthy: boolean; details?: string }>;
}

// Define Zod schemas for validation
export const executionStatusSchema = z.enum([
  ExecutionStatus.pending,
  ExecutionStatus.running,
  ExecutionStatus.completed,
  ExecutionStatus.failed,
  ExecutionStatus.cancelled,
]);

export const toolExecutionContextSchema: z.ZodType<ToolExecutionContext> = z.object({
  userId: z.string().optional(),
  toolId: z.string(),
  executionId: z.string(),
  permissions: z.array(z.string()),
  timestamp: z.string(),
  metadata: z.record(z.unknown()).optional(),
});

export const toolExecutionResultSchema: z.ZodType<ToolExecutionResult> = z.object({
  executionId: z.string(),
  status: executionStatusSchema.refine((status) => status !== ExecutionStatus.pending),
  output: z.unknown().optional(),
  error: z
    .object({
      message: z.string(),
      code: z.string().optional(),
      details: z.unknown().optional(),
    })
    .optional(),
  durationMs: z.number(),
  completedAt: z.string(),
});

export const toolExecutorSchema: z.ZodType<ToolExecutor> = z.object({
  execute: z.function().args(z.unknown(), toolExecutionContextSchema).returns(toolExecutionResultSchema),
  healthCheck: z.function().returns(z.object({ healthy: z.boolean(), details: z.string().optional() })),
});
