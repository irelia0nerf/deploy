from datetime import datetime

def calculate_score(req):
    base_score = 600
    if req.tx_count > 100:
        base_score += 50
    if req.balance > 10000:
        base_score += 100
    flags = []
    reasons = []
    if "mixer" in req.risk_inputs:
        base_score -= 200
        flags.append("high_risk_mixer")
        reasons.append("Mixer detected")
    status = "allow" if base_score > 700 else "review" if base_score > 500 else "block"
    spread = round(base_score * 0.01, 2)
    return {
        "wallet_address": req.wallet_address,
        "score": base_score,
        "spread": spread,
        "status": status,
        "flags": flags,
        "reasons": reasons,
        "timestamp": datetime.utcnow().isoformat()
    }
