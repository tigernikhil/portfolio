import { describe, it, expect } from 'vitest';
import { parser } from '../src/parser';

describe('Form 26AS Tax Credit Parser Tests', () => {
  it('should process valid input correctly', async () => {
    const res = await parser({ content: 'sample test content' });
    expect(res).toBeDefined();
    // Add more specific assertions based on the expected output
  });

  it('should handle empty or invalid input', async () => {
    await expect(async () => {
      await parser(null);
    }).rejects.toThrow();
  });

  it('should correctly parse tax credit information', async () => {
    const input = {
      content: 'Tax Credit Amount: 5000\nTax Credit Type: Education'
    };
    const res = await parser(input);
    expect(res.taxCreditAmount).toBe(5000);
    expect(res.taxCreditType).toBe('Education');
  });

  it('should handle missing tax credit information gracefully', async () => {
    const input = {
      content: 'Sample content without tax credit information'
    };
    const res = await parser(input);
    expect(res.taxCreditAmount).toBeUndefined();
    expect(res.taxCreditType).toBeUndefined();
  });

  it('should handle unexpected input format', async () => {
    const input = {
      content: 'Unexpected input format'
    };
    await expect(async () => {
      await parser(input);
    }).rejects.toThrow();
  });
});
