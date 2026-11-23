from pathlib import Path

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_scan():
    src = (Path(__file__).parent / "vulnerable_app.py").read_text()
    r = client.post("/scan", json={"source": src}).json()
    assert {f["rule"] for f in r["findings"]} == {"hardcoded-secret", "sql-injection", "eval-usage"}
    assert r["regression_passed"]
