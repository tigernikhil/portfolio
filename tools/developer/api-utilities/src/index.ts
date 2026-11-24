import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { utilities } from './utilities';
import manifest from '../tool.manifest.json';

export class UtilitiesTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await utilities(input);
  }
}

export function createTool(): UtilitiesTool {
  return new UtilitiesTool();
}
