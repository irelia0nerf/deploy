from datetime import datetime

RULE_VERSION = "1.1"

def calculate_score(req):
    base_score = 600
    if req.tx_count > 100:
        base_score += 50
    if req.tx_count > 200:
        base_score += 100
    if req.balance > 10000:
        base_score += 100
    if req.balance > 50000:
        base_score += 200
    flags = []
    reasons = []
    if "mixer" in req.risk_inputs:
        base_score -= 200
        flags.append("high_risk_mixer")
        reasons.append("Mixer detected")
    if "sanctioned" in req.risk_inputs:
        base_score -= 300
        flags.append("sanctioned")
        reasons.append("Sanctioned entity")
    status = "allow" if base_score > 700 else "review" if base_score > 500 else "block"
    spread = round(base_score * 0.01, 2)
    return {
        "wallet_address": req.wallet_address,
        "score": base_score,
        "spread": spread,
        "status": status,
        "flags": flags,
        "reasons": reasons,
        "timestamp": datetime.utcnow().isoformat(),
        "rule_version": RULE_VERSION
    }
