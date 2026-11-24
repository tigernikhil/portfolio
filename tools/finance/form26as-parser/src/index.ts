import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { parser } from './parser';
import manifest from '../tool.manifest.json';

export class ParserTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await parser(input);
  }
}

export function createTool(): ParserTool {
  return new ParserTool();
}
