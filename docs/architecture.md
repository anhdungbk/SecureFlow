# Architecture
FastAPI backend. `POST /scan` runs the pipeline in `services/scanner.py`:
Scanner (regex rules) → Analyzer (severity + explanation; LLM later) → Remediator (patch proposal) → Tester (re-scan, must be clean).
The result is returned for human review.
