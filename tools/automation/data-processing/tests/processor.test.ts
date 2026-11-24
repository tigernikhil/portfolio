import { describe, it, expect } from 'vitest';
import { processor } from '../src/processor';

describe('Batch Data Processor Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await processor({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res.content).toBe('sample test content');
  });

  it('should handle empty input', async () => {
    await expect(async () => {
      await processor({ content: '' });
    }).rejects.toThrow();
  });

  it('should handle invalid input', async () => {
    await expect(async () => {
      await processor({} as any);
    }).rejects.toThrow();
  });
});
