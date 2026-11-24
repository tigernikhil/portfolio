---
name: financial-tool-security
description: Mandatory security and privacy policy for Form 16, Form 26AS, and Stock P&L parsers and financial tools.
---

# Financial Tool Security & Privacy Policy

## 1. Zero-Retention Principle
- **No Document Retention**: Uploaded tax documents (Form 16 PDFs, Form 26AS JSON/PDFs, broker tradebooks) must NOT be persisted to disk or databases by default.
- **Ephemeral In-Memory Processing**: Parse, extract summary metrics, stream results to client, and discard binary buffers.
- **Explicit User Consent**: If a user explicitly chooses to save summary figures (e.g. total taxable income or capital gains), save only aggregated non-PII numerical metrics.

## 2. Redaction & Masking
- **PAN / Aadhaar / Account Numbers**: Never log Permanent Account Numbers (PAN), Aadhaar numbers, bank account numbers, or demat IDs in plain text.
- If display is required, mask all but the last 4 characters (e.g., `XXXXX1234X`).

## 3. Isolated Execution
- Financial parsers must run in sandboxed or isolated execution environments to prevent cross-process data leakage.

Reference:
- Security Policy: [docs/security/security-policy.md](file:///Users/admin/Downloads/Portfolio/docs/security/security-policy.md)
- Privacy Architecture: [docs/security/privacy.md](file:///Users/admin/Downloads/Portfolio/docs/security/privacy.md)
