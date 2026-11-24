# Flight Price Tracker Integration Specification

## 1. Architectural Overview & Topology

The Flight Price Tracker integration couples the existing enterprise Java/Spring Boot & Playwright microservice suite located at `/Users/admin/Documents/FlightPriceTracker` with the Personal Technology Platform monorepo under `@tools/flight-price-tracker`.

```
+-------------------------------------------------------------+
|                Personal Technology Platform                 |
|             (@tools/flight-price-tracker)                   |
+-------------------------------------------------------------+
                              |
                     [Tool SDK Adapter]
                              |
       +----------------------+----------------------+
       |                                             |
       v                                             v
+------------------------+              +------------------------+
| Spring Boot Backend    |              | Playwright Scraper     |
| (Port 8080)            |              | (Port 3000)            |
| - PricePredictionSvc   | <---Kafka--> | - Multi-portal Scraper |
| - DateSuggestionSvc    |              | - Headless Chromium    |
| - AlertEngine          |              +------------------------+
+------------------------+
       |
       v
+------------------------+
| Transactional Email    |
| Notification Pipeline  |
| (SMTP / SES)           |
+------------------------+
```

### 1.1 Components & Microservices
- **Platform Tool SDK Adapter (`@tools/flight-price-tracker`)**: Ports & Adapters wrapper implementing `BaseTool` from `@platform/tool-sdk` and strictly adhering to `ToolExecutionContext` from `@platform/contracts`.
- **Spring Boot Analytics Core**: Calculates historical trends, price drop probability via decay curves, and date flexibility opportunities.
- **Kafka Event Streaming**: Decouples scraping requests (`ScrapeRequestEvent`) from price collection responses (`ScrapeResultEvent`).
- **Playwright Headless Scraper**: Automated browser agent scraping real-time airfares across domestic and international portals.
- **Transactional Alert Engine**: Dispatches real-time price drop notifications when current airfare drops below target price thresholds.

---

## 2. Authentication & Session Context Protocol

In compliance with the platform security constitution (`AGENTS.md` and `docs/architecture/security.md`):

1. **User Authentication Guard**: The tool manifest specifies `"visibility": "authenticated"`. The tool execution pipeline rejects any invocation lacking a verified `userId` in `ToolExecutionContext`.
2. **Access Control**: Users can only track routes, configure alerts, and view historical price predictions under their authenticated tenant/user session.
3. **Session Verification**: Invocations validate `context.userId` before forwarding requests to the Spring Boot backend or calculation engine.

---

## 3. Price Prediction & Alternative Date Engine

### 3.1 Drop Probability Calculation
The predictive engine computes the probability of a price drop based on days remaining until departure:
$$\text{Drop Probability} = f(\Delta t)$$
- **$\Delta t > 60$ days**: 72% probability of price fluctuation/drop. Recommendation: `wait`.
- **$30 \le \Delta t \le 60$ days**: 48% probability. Recommendation: `monitor`.
- **$14 \le \Delta t < 30$ days**: 28% probability. Recommendation: `monitor`.
- **$\Delta t < 14$ days**: 10% probability. Recommendation: `buy_now`.

### 3.2 Flexible Date Scanning (>15% Discount Threshold)
Scans $\pm 3$ days around the target departure date. Alternative dates with $\ge 15\%$ estimated savings are surfaced to the user as viable cost-saving alternatives.

---

## 4. End-to-End Email Alert Notification Protocol

Per `docs/integrations/email.md`:
- **Trigger Condition**: Automatically triggered when `currentPrice <= targetPrice`.
- **Payload Schema**:
  - `to`: User's authenticated email address (`userEmail` or `${userId}@platform.internal`).
  - `subject`: `✈️ Flight Price Alert: [Origin] -> [Destination] dropped to [Price]!`
  - `template`: `flight-price-drop-alert`
  - `referenceId`: Unique routing tracking token (e.g., `FLT-[Origin]-[Destination]-[Timestamp]`).
- **SMTP Gateway**: Forwarded to the platform's transactional email service or local mail agent.

---

## 5. Tool SDK Manifest & Schema

Located at `tools/productivity/flight-price-tracker/tool.manifest.json`:
- **ID**: `tool-productivity-flight-price-tracker`
- **Visibility**: `authenticated`
- **Category**: `productivity`
- **Required Inputs**: `origin`, `destination`, `departureDate`
- **Optional Inputs**: `currentPrice`, `targetPrice`, `currency`, `userEmail`, `userName`

---

## 6. Docker & Production Deployment

Included in `deploy/docker-compose.tools.yml`:
- Service: `flight-tracker-backend` (Port 8080)
- Service: `flight-scraper-service` (Port 3000)
- Managed via `deploy/deploy-tools.sh` with automated health check polling and zero-downtime rollback capability.
