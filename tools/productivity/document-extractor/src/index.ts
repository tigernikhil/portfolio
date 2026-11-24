import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { extractor } from './extractor';
import manifest from '../tool.manifest.json';

export class ExtractorTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await extractor(input);
  }
}

export function createTool(): ExtractorTool {
  return new ExtractorTool();
}
