import os
import pytest
from httpx import AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_health():
    os.environ["API_KEY"] = "testkey"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.get("/health/")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_score():
    os.environ["API_KEY"] = "testkey"
    payload = {
        "wallet_address": "0xabc123",
        "tx_count": 120,
        "balance": 5000,
        "risk_inputs": []
    }
    headers = {"x-api-key": "testkey"}
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/score/", json=payload, headers=headers)
    assert resp.status_code == 200
    data = resp.json()
    assert "score" in data
    assert data["wallet_address"] == "0xabc123"
