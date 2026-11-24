import { describe, it, expect } from 'vitest';
import { utilities } from '../src/utilities';

describe('API Developer Utilities Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await utilities({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toContain('sample test content');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await utilities(null);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await utilities(undefined);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await utilities('');
    }).rejects.toThrow('Invalid input provided');
  });
});
