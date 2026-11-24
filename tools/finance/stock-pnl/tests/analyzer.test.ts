import { describe, it, expect } from 'vitest';
import { analyzer } from '../src/analyzer';

describe('Stock P&L Analyzer Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await analyzer({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toHaveProperty('profit');
    expect(res).toHaveProperty('loss');
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await analyzer(null);
    }).rejects.toThrow('Invalid input');

    await expect(async () => {
      await analyzer('');
    }).rejects.toThrow('Invalid input');
  });

  it('should return zero profit and loss for no transactions', async () => {
    const res = await analyzer({ content: 'No transactions' });
    expect(res).toBeDefined();
    expect(res.profit).toBe(0);
    expect(res.loss).toBe(0);
  });

  it('should calculate profit and loss correctly for transactions', async () => {
    const res = await analyzer({ content: 'Buy 100 shares at $10 each\nSell 50 shares at $15 each' });
    expect(res).toBeDefined();
    expect(res.profit).toBe(250);
    expect(res.loss).toBe(0);
  });

  it('should handle negative profit and loss correctly', async () => {
    const res = await analyzer({ content: 'Buy 100 shares at $15 each\nSell 50 shares at $10 each' });
    expect(res).toBeDefined();
    expect(res.profit).toBe(0);
    expect(res.loss).toBe(250);
  });

  it('should ignore non-transaction lines', async () => {
    const res = await analyzer({ content: 'Buy 100 shares at $10 each\nIgnore this line\nSell 50 shares at $15 each' });
    expect(res).toBeDefined();
    expect(res.profit).toBe(250);
    expect(res.loss).toBe(0);
  });
});
