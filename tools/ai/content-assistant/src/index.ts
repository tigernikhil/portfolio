import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { assistant } from './assistant';
import manifest from '../tool.manifest.json';

export class AssistantTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await assistant(input);
  }
}

export function createTool(): AssistantTool {
  return new AssistantTool();
}
