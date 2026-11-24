import { describe, it, expect } from 'vitest';
import { parser } from '../src/parser';

describe('Form 16 Tax Parser Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await parser({ content: 'sample test content' });
    expect(res).toBeDefined();
    expect(res).toHaveProperty('taxDetails');
    expect(res.taxDetails).toBeInstanceOf(Object);
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await parser(null);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await parser(undefined);
    }).rejects.toThrow('Invalid input provided');

    await expect(async () => {
      await parser('');
    }).rejects.toThrow('Invalid input provided');
  });

  it('should return default values for missing tax details', async () => {
    const res = await parser({ content: 'sample test content' });
    expect(res.taxDetails).toEqual({
      totalIncome: 0,
      deductions: 0,
      taxPayable: 0,
      taxRefund: 0,
    });
  });

  it('should correctly parse tax details from input content', async () => {
    const inputContent = `
      Total Income: 50000
      Deductions: 10000
      Tax Payable: 12000
      Tax Refund: 5000
    `;
    const res = await parser({ content: inputContent });
    expect(res.taxDetails).toEqual({
      totalIncome: 50000,
      deductions: 10000,
      taxPayable: 12000,
      taxRefund: 5000,
    });
  });
});
