import { describe, it, expect } from 'vitest';
import { workflow } from '../src/workflow';

describe('Workflow Automation Runner Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await workflow({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res.content).toBe('sample test content');
  });

  it('should handle empty input', async () => {
    await expect(async () => {
      await workflow({});
    }).rejects.toThrow();
  });

  it('should handle invalid input', async () => {
    await expect(async () => {
      await workflow('not an object');
    }).rejects.toThrow();
  });

  it('should handle input with missing content property', async () => {
    await expect(async () => {
      await workflow({});
    }).rejects.toThrow();
  });
});
