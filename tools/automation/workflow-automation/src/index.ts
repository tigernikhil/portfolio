import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';
import { workflow } from './workflow';
import manifest from '../tool.manifest.json';

export class WorkflowTool extends BaseTool {
  constructor() {
    super(manifest as any);
  }

  public async run(input: any, context: ToolExecutionContext): Promise<any> {
    return await workflow(input);
  }
}

export function createTool(): WorkflowTool {
  return new WorkflowTool();
}
