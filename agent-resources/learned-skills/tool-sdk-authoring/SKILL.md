---
name: tool-sdk-authoring
description: Mandatory standards for creating and registering new tools using @platform/tool-sdk and @platform/contracts.
---

# Tool SDK Authoring Standards

## 1. Tool Anatomy
Every tool in `tools/<category>/<tool-name>/` must have:
1. `tool.manifest.json`: Conforming to `ToolManifestSchema` from `@platform/contracts`.
2. `package.json`: Independent monorepo package with workspace dependencies on `@platform/contracts` and `@platform/tool-sdk`.
3. `src/<role>.ts`: Pure isolated business logic. No React, no Next.js, no direct vendor SDK imports.
4. `src/index.ts`: Class extending `BaseTool` from `@platform/tool-sdk`. Implements `run(input, context)`.
5. `tests/<role>.test.ts`: Vitest unit tests covering valid processing, edge cases, and error handling.

## 2. Directory Layout
```
tools/<category>/<tool-name>/
├── tool.manifest.json
├── package.json
├── src/
│   ├── <role>.ts
│   └── index.ts
└── tests/
    └── <role>.test.ts
```

## 3. Visibility Guidelines
- `public`: Available to all unauthenticated visitors.
- `authenticated`: Registered users only.
- `restricted`: Users with explicit `tool:<id>` permission.
- `private`: Admins and platform owner only.

Reference:
- System Architecture: [docs/architecture/system-architecture.md](file:///Users/admin/Downloads/Portfolio/docs/architecture/system-architecture.md)
- Module Boundaries: [docs/architecture/module-boundaries.md](file:///Users/admin/Downloads/Portfolio/docs/architecture/module-boundaries.md)
