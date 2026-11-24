import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { generator } from './generator';
import manifest from '../tool.manifest.json';

export class GeneratorTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await generator(input);
  }
}

export function createTool(): GeneratorTool {
  return new GeneratorTool();
}
