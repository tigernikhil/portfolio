import { describe, it, expect } from 'vitest';
import { extractor } from '../src/extractor';

describe('Structured Document Extractor Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await extractor({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toHaveProperty('content');
    expect(res.content).toBe('sample test content');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await extractor(null);
    }).rejects.toThrow('Invalid input: null');

    await expect(async () => {
      await extractor(undefined);
    }).rejects.toThrow('Invalid input: undefined');

    await expect(async () => {
      await extractor('');
    }).rejects.toThrow('Invalid input: empty string');
  });
});
