import { describe, it, expect } from 'vitest';
import { ClearTaxEngine, createTool, processClearTaxReturn, TaxInputData } from '../src';
import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';

describe('ClearTaxEngine & Tool', () => {
  const engine = new ClearTaxEngine();
  const validContext: ToolExecutionContext = {
    userId: 'usr_tax_456',
    toolId: 'tool-finance-cleartax-filing',
    executionId: 'exec_tax_001',
    permissions: ['finance:tax-filing'],
    timestamp: new Date().toISOString()
  };

  it('Calculates Old and New regime accurately and selects New regime when deductions are low', async () => {
    const input: TaxInputData = {
      pan: 'ABCDE1234F',
      assessmentYear: '2024-25',
      salaryIncome: 800000,
      section80C: 10000,
      userEmail: 'taxpayer@platform.com'
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.recommendedRegime).toBe('new');
    expect(result.newRegime.totalTax).toBeLessThanOrEqual(result.oldRegime.totalTax);
    expect(result.taxSavings).toBeGreaterThanOrEqual(0);
    expect(result.emailConfirmationSent).toBe(true);
    expect(result.emailDetails?.to).toBe('taxpayer@platform.com');
  });

  it('Selects Old regime when 80C, 80D, and HRA deductions exceed the breakeven threshold', async () => {
    const input: TaxInputData = {
      pan: 'ABCDE1234F',
      assessmentYear: '2024-25',
      salaryIncome: 1200000,
      section80C: 150000,
      section80D: 50000,
      hra: 150000,
      userEmail: 'taxpayer@platform.com'
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.recommendedRegime).toBe('old');
    expect(result.oldRegime.totalTax).toBeLessThan(result.newRegime.totalTax);
    expect(result.taxSavings).toBe(result.newRegime.totalTax - result.oldRegime.totalTax);
  });

  it('Dispatches email confirmation with reference ID and tax summary', async () => {
    const input: TaxInputData = {
      pan: 'ABCDE1234F',
      assessmentYear: '2024-25',
      salaryIncome: 650000,
      userEmail: 'confirm@platform.com',
      userName: 'Rohan Sharma'
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.emailConfirmationSent).toBe(true);
    expect(result.emailDetails).toBeDefined();
    expect(result.emailDetails?.referenceId).toBe(result.filingId);
    expect(result.emailDetails?.subject).toContain(result.filingId);
    expect(result.emailDetails?.to).toBe('confirm@platform.com');
  });

  it('Rejects with Error when PAN format is invalid', async () => {
    const input: TaxInputData = {
      pan: 'INVALID_PAN',
      assessmentYear: '2024-25',
      salaryIncome: 500000
    };

    await expect(engine.process(input, validContext.userId)).rejects.toThrow(
      /Invalid PAN format/
    );
  });

  it('Rejects with Error when userId is missing (auth enforcement)', async () => {
    const tool = createTool();
    const input = {
      pan: 'ABCDE1234F',
      assessmentYear: '2024-25',
      salaryIncome: 600000
    };
    const unauthenticatedContext: ToolExecutionContext = {
      userId: '',
      toolId: 'tool-finance-cleartax-filing',
      executionId: 'exec_tax_002',
      permissions: [],
      timestamp: new Date().toISOString()
    };

    await expect(tool.run(input, unauthenticatedContext)).rejects.toThrow(
      'User authentication required for ClearTax Filing'
    );
  });

  it('Generates valid ITR XML summary', async () => {
    const input: TaxInputData = {
      pan: 'ABCDE1234F',
      assessmentYear: '2024-25',
      salaryIncome: 700000
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.itrXmlGenerated).toBe(true);
    expect(result.itrXmlContent).toContain('<taxSummary>');
    expect(result.itrXmlContent).toContain('<PAN>ABCDE1234F</PAN>');
    expect(result.itrXmlContent).toContain('<FilingId>');
  });

  it('createTool() instantiates BaseTool subclass with valid manifest', () => {
    const tool = createTool();
    expect(tool).toBeInstanceOf(BaseTool);
    expect(tool.manifest.id).toBe('tool-finance-cleartax-filing');
    expect(tool.manifest.visibility).toBe('authenticated');
    expect(tool.manifest.capabilities).toContain('itr-filing');
    expect(tool.manifest.capabilities).toContain('user-auth');
  });
});
