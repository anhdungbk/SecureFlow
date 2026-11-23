# Security principles
- Human in the loop: patches are never auto-merged.
- Every patch must pass a regression re-scan.
- Scanned code is untrusted data: never executed.
- No secrets in the repo; use environment variables.
