import { ToolExecutor, ToolExecutionContext, ToolExecutionResult, ToolManifest } from '@platform/contracts';
import { validateManifest } from './validator';
import { ToolExecutionError } from './errors';

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
