from pydantic import BaseModel


class Finding(BaseModel):
    line: int
    rule: str
    severity: str
    why: str
    code: str


class ScanRequest(BaseModel):
    source: str


class ScanResult(BaseModel):
    findings: list[Finding]
    patched: str
    regression_passed: bool
