import requests

BASE_URL = "http://localhost:8000"

def test_health():
    r = requests.get(f"{BASE_URL}/health/")
    assert r.status_code == 200

def test_score():
    payload = {
        "wallet_address": "0xabc123",
        "tx_count": 120,
        "balance": 5000,
        "risk_inputs": []
    }
    headers = {"x-api-key": "testkey"}
    r = requests.post(f"{BASE_URL}/score/", json=payload, headers=headers)
    assert r.status_code == 200
    assert "score" in r.json()
