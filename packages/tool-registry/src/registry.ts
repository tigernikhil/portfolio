import { BaseTool } from '@platform/tool-sdk';
import { ToolManifest } from '@platform/contracts';

export class ToolRegistry {
  private tools = new Map<string, BaseTool>();

  public registerTool(tool: BaseTool): void {
    if (this.tools.has(tool.manifest.id)) {
      throw new Error(`Tool already registered: ${tool.manifest.id}`);
    }
    this.tools.set(tool.manifest.id, tool);
  }

  public unregisterTool(id: string): boolean {
    return this.tools.delete(id);
  }

  public getTool(id: string): BaseTool | undefined {
    return this.tools.get(id);
  }

  public listTools(filter?: { category?: string; visibility?: string; capability?: string }): ToolManifest[] {
    const list = Array.from(this.tools.values()).map(t => t.manifest);
    return list.filter(m => {
      if (filter?.category && m.category !== filter.category) return false;
      if (filter?.visibility && m.visibility !== filter.visibility) return false;
      if (filter?.capability && !m.capabilities.includes(filter.capability)) return false;
      return true;
    });
  }

  public searchTools(query: string): ToolManifest[] {
    const q = query.toLowerCase();
    return Array.from(this.tools.values())
      .map(t => t.manifest)
      .filter(m => m.name.toLowerCase().includes(q) || m.description.toLowerCase().includes(q));
  }
}

export const defaultRegistry = new ToolRegistry();
