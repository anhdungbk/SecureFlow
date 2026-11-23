# SecureFlow
AI Security Engineer: find vulnerabilities, understand risk, fix them automatically.

Demo flow: **Orchestrator → Scanner → Analyzer → Remediator → Tester → human review**.

```
pip install -r backend/requirements.txt
cd backend && uvicorn app.main:app --reload   # GET /health, POST /scan
PYTHONPATH=backend pytest tests
```
See [docs/](docs/). Patches are never auto-merged.
