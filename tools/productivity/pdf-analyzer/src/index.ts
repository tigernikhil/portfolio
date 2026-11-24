import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { analyzer } from './analyzer';
import manifest from '../tool.manifest.json';

export class AnalyzerTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await analyzer(input);
  }
}

export function createTool(): AnalyzerTool {
  return new AnalyzerTool();
}
