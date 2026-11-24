import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { processor } from './processor';
import manifest from '../tool.manifest.json';

export class ProcessorTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await processor(input);
  }
}

export function createTool(): ProcessorTool {
  return new ProcessorTool();
}
