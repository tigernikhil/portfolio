# CONTRIBUTING.md

## Monorepo Workflow with pnpm

This project uses a monorepo workflow with `pnpm` as the package manager. This allows for efficient dependency management and easy development of tools and packages.

## Code Standards

### Prettier
Prettier is used for code formatting. Ensure that your code is formatted correctly by running `pnpm format` before committing.

### ESLint
ESLint is used for static code analysis. Ensure that your code passes ESLint checks by running `pnpm lint` before committing.

### Zod
Zod is used for schema validation. Ensure that your tool's schema is correctly defined by running `pnpm validate` before committing.

## Building a New Tool Using @platform/tool-sdk

To build a new tool, you will need to use the `@platform/tool-sdk`. Follow these steps:

1. Clone the repository and navigate to the directory.
2. Install dependencies with `pnpm install`.
3. Create a new tool by running `pnpm run create-tool <tool-name>`.
4. Implement the tool's functionality.
5. Run tests with `pnpm test`.
6. Commit your changes with `pnpm commit`.

## Testing Requirements

### Vitest
Vitest is used for testing. Ensure that your tool passes all tests by running `pnpm test` before submitting a pull request.

## PR Checklists

### Before Submitting a PR
- Ensure that your code is formatted with `pnpm format`.
- Run ESLint checks with `pnpm lint`.
- Validate your tool's schema with `pnpm validate`.
- Run all tests with `pnpm test`.
- Ensure that your tool's documentation is up-to-date.

### After Submitting a PR
- Address any comments or issues raised by the maintainers.
- Ensure that your PR is ready for merge.

---

This guide provides a comprehensive overview of contributing to this project. For more detailed information, refer to the project's documentation and guidelines.
```

Please note that the above content is a template and should be adjusted to fit the specific requirements and structure of the project.
