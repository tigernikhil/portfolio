import { describe, it, expect } from 'vitest';
import { playground } from '../src/playground';

describe('Model Context Protocol Playground Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await playground({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toBe('Processed: sample test content');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await playground(null);
    }).rejects.toThrow('Invalid input');

    await expect(async () => {
      await playground(undefined);
    }).rejects.toThrow('Invalid input');

    await expect(async () => {
      await playground('');
    }).rejects.toThrow('Invalid input');
  });
});
