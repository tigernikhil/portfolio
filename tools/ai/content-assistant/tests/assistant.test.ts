import { describe, it, expect } from 'vitest';
import { assistant } from '../src/assistant';

describe('AI Technical Content Assistant Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await assistant({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toContain('sample test content');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await assistant(null);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await assistant('');
    }).rejects.toThrow('Invalid input provided');
  });
});
