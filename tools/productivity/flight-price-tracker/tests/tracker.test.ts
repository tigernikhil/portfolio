import { describe, it, expect } from 'vitest';
import { FlightPriceTrackerEngine, createTool, FlightPriceTrackerTool } from '../src';
import { BaseTool } from '@platform/tool-sdk';
import { ToolExecutionContext } from '@platform/contracts';

describe('FlightPriceTracker', () => {
  const engine = new FlightPriceTrackerEngine();
  const validContext: ToolExecutionContext = {
    userId: 'usr_flight_789',
    toolId: 'tool-productivity-flight-price-tracker',
    executionId: 'exec_flt_001',
    permissions: ['tools:execute'],
    timestamp: new Date().toISOString()
  };

  it('Successful route tracking and price prediction when user is authenticated', async () => {
    const input = {
      origin: 'JFK',
      destination: 'LAX',
      departureDate: '2026-12-15',
      currentPrice: 380,
      targetPrice: 400,
      userEmail: 'traveler@platform.com'
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.routeId).toContain('JFK-LAX');
    expect(result.currentPrice).toBe(380);
    expect(result.predictedDropProbability).toBeGreaterThan(0);
    expect(result.recommendation).toBeDefined();
  });

  it('Price drop alert email triggered when currentPrice <= targetPrice', async () => {
    const input = {
      origin: 'LHR',
      destination: 'DXB',
      departureDate: '2026-11-30',
      currentPrice: 320,
      targetPrice: 350,
      userEmail: 'alerts@traveler.com'
    };

    const result = await engine.process(input, validContext.userId);
    expect(result.alertTriggered).toBe(true);
    expect(result.emailSent).toBe(true);
    expect(result.emailDetails).toBeDefined();
    expect(result.emailDetails?.to).toBe('alerts@traveler.com');
    expect(result.emailDetails?.subject).toContain('Flight Price Alert');
  });

  it('Cheaper alternative dates suggested with >15% savings', () => {
    const suggestions = engine.suggestCheaperDates('2026-12-01', 500);
    expect(suggestions.length).toBeGreaterThan(0);
    suggestions.forEach(opt => {
      expect(opt.savingsPercent).toBeGreaterThanOrEqual(15);
      expect(opt.estimatedPrice).toBeLessThan(500);
    });
  });

  it('Rejection with Error when userId is missing from ToolExecutionContext (auth enforcement)', async () => {
    const tool = createTool();
    const input = {
      origin: 'BOM',
      destination: 'DEL',
      departureDate: '2026-12-10'
    };
    const unauthenticatedContext: ToolExecutionContext = {
      userId: '',
      toolId: 'tool-productivity-flight-price-tracker',
      executionId: 'exec_flt_002',
      permissions: [],
      timestamp: new Date().toISOString()
    };

    await expect(tool.run(input, unauthenticatedContext)).rejects.toThrow(
      'User authentication required for Flight Price Tracker'
    );
  });

  it('createTool() instantiates BaseTool subclass with valid manifest', () => {
    const tool = createTool();
    expect(tool).toBeInstanceOf(BaseTool);
    expect(tool).toBeInstanceOf(FlightPriceTrackerTool);
    expect(tool.manifest.id).toBe('tool-productivity-flight-price-tracker');
    expect(tool.manifest.visibility).toBe('authenticated');
    expect(tool.manifest.capabilities).toContain('flight-tracking');
    expect(tool.manifest.capabilities).toContain('email-alerting');
  });
});
