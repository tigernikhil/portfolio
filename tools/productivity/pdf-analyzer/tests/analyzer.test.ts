import { describe, it, expect } from 'vitest';
import { analyzer } from '../src/analyzer';

describe('PDF Structure & Text Analyzer Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await analyzer({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res.content).toBe('sample test content');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await analyzer(null);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await analyzer(undefined);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await analyzer('');
    }).rejects.toThrow('Invalid input provided');
  });

  it('should return structured data for valid input', async () => {
    const res = await analyzer({ content: 'sample test content' });
    expect(res).toHaveProperty('structure');
    expect(res).toHaveProperty('text');
  });

  it('should handle large input without errors', async () => {
    const largeContent = 'a'.repeat(100000); // 100,000 'a' characters
    const res = await analyzer({ content: largeContent });
    expect(res).toBeDefined();
    expect(res.content).toBe(largeContent);
  });
});
