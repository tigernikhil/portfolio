import { describe, it, expect } from 'vitest';
import { generator } from '../src/generator';

describe('AI Micro-Drama Story Generator Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await generator({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(typeof res).toBe('string');
    expect(res.length).toBeGreaterThan(0);
  });

  it('should handle empty input', async () => {
    await expect(async () => {
      await generator({ content: '' });
    }).rejects.toThrow();
  });

  it('should handle null input', async () => {
    await expect(async () => {
      await generator(null);
    }).rejects.toThrow();
  });

  it('should handle undefined input', async () => {
    await expect(async () => {
      await generator(undefined);
    }).rejects.toThrow();
  });

  it('should handle input with only whitespace', async () => {
    await expect(async () => {
      await generator({ content: ' ' });
    }).rejects.toThrow();
  });
});
