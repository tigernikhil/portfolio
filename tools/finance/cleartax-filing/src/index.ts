import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { processClearTaxReturn } from './tax-engine';
import manifest from '../tool.manifest.json';

class ClearTaxFilingTool extends BaseTool {
  constructor() {
    super(manifest);
  }

  async run(input: any, context: ToolExecutionContext): Promise<any> {
    if (!context.userId) {
      throw new Error('User authentication required for ClearTax Filing');
    }
    const output = await processClearTaxReturn(input, context.userId);
    return output;
  }
}

export function createTool(): ClearTaxFilingTool {
  return new ClearTaxFilingTool();
}

export * from './tax-engine';