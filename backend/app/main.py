from fastapi import FastAPI

from app.schemas.findings import ScanRequest, ScanResult
from app.services.scanner import run_pipeline

app = FastAPI(title="SecureFlow")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/scan", response_model=ScanResult)
def scan(req: ScanRequest):
    return run_pipeline(req.source)  # patches are proposals only; never auto-merged
