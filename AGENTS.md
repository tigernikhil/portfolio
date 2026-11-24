# AGENTS.md: Multi-Agent Governance Policy for Coding Agents

## Constitution

### No Secrets in Git
All business logic and secrets should be kept outside of Git. Secrets should be managed through secure vaults or environment variables. Business logic should be encapsulated in modules or services that are versioned and auditable.

### Business Logic Separation from Infrastructure
Business logic should be decoupled from infrastructure. This separation ensures that changes in infrastructure do not affect the business logic, and vice versa. Business logic should be defined and tested independently.

### Interfaces for External Providers
All interfaces to external providers (e.g., databases, APIs, etc.) should be defined and documented. These interfaces should be tested to ensure they are reliable and secure.

### Definition of Done
The definition of done for coding agents should include:
- Code is free of bugs and meets all requirements.
- Code is well-documented and follows the coding standards.
- Code is reviewed and approved by peers.
- Code is tested and passes all unit tests.
- Code is deployed and verified in a staging environment.
- Code is deployed to production with a rollback plan.

## Architecture Rules

### Ports & Adapters
All external interactions should be through well-defined ports and adapters. This approach ensures loose coupling and makes it easier to replace or extend the underlying infrastructure.

### TypeScript Strict
All code should be written in TypeScript with strict mode enabled. This helps catch errors early and ensures that the codebase is consistent and maintainable.

### Vitest for Unit Tests
Unit tests should be written using Vitest. These tests should cover all aspects of the codebase, including edge cases and integration points with external systems.

## Division of Labor

### Cloud Orchestration
Cloud orchestration tasks should be handled by dedicated cloud orchestrators. These orchestrators are responsible for deploying, scaling, and managing the infrastructure. They should not be involved in the coding logic of the agents.

### Local Ollama Agents
Local Ollama agents are responsible for running the Ollama coding agent locally. These agents are responsible for executing the business logic and interacting with the external providers. They should be isolated from the cloud environment to ensure security and isolation.

## Preflight Checks and Commit Policies

### Preflight Checks
Before a commit is made, the following checks should be performed:
- Code is linted and passes all linters.
- Code is formatted according to the coding standards.
- Code is reviewed by a peer.
- Code passes all unit tests.
- Code passes all pre-commit checks (e.g., linters, formatters, etc.).

### Commit Policies
Commits should follow these guidelines:
- Each commit should be small and focused on a single change.
- Commits should include a clear commit message that describes the changes.
- Commits should be squashed into a single commit if they are part of a single feature or bug fix.
- Commits should not include any code that is not part of the current feature or bug fix.
- Commits should not include any code that is not part of the current feature or bug fix.

### Continuous Self-Improvement & Mandatory Skill Protocol
All reusable and learned skills MUST go into `agent-resources/learned-skills/`. Every agent (Gemini, Ollama, Copilot, Cursor) operating in this repository has to use the respective skills mandatorily, and accordingly code or make changes. Agents must continuously update the skills and improve self with each and every task. Actual data findings, architectural decisions, and blueprints must be maintained in the `docs/` folders where skills can cross-reference them directly.

By adhering to these governance policies, we can ensure that our coding agents are secure, maintainable, and reliable.
