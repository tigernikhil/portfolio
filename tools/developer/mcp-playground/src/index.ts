import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { playground } from './playground';
import manifest from '../tool.manifest.json';

export class PlaygroundTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await playground(input);
  }
}

export function createTool(): PlaygroundTool {
  return new PlaygroundTool();
}
