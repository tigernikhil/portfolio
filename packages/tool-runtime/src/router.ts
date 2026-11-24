import { ToolExecutionContext, ToolExecutionResult } from '@platform/contracts';
import { ToolRegistry, defaultRegistry } from '@platform/tool-registry';
import { ServiceUnavailableError, PermissionDeniedError } from '@platform/tool-sdk';

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
