import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import FlightPriceTrackerEngine from './tracker';
import manifest from '../tool.manifest.json';

export class FlightPriceTrackerTool extends BaseTool {
  constructor() {
    super(manifest);
  }

  async run(input: any, context: ToolExecutionContext): Promise<any> {
    if (!context || !context.userId) {
      throw new Error('User authentication required for Flight Price Tracker');
    }
    const engine = new FlightPriceTrackerEngine();
    return await engine.process(input, context.userId);
  }
}

export function createTool(): FlightPriceTrackerTool {
  return new FlightPriceTrackerTool();
}

export * from './tracker';
