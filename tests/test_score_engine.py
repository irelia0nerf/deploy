from app.score_engine import calculate_score
from app.schemas import ScoreRequest


def test_calculate_score_high_risk():
    req = ScoreRequest(wallet_address="0x1", tx_count=50, balance=0, risk_inputs=["mixer", "sanctioned"])
    result = calculate_score(req)
    assert result["status"] == "block"
    assert "sanctioned" in result["flags"]


def test_calculate_score_high_balance():
    req = ScoreRequest(wallet_address="0x2", tx_count=250, balance=60000, risk_inputs=[])
    result = calculate_score(req)
    assert result["score"] > 900
    assert result["rule_version"] == "1.1"

