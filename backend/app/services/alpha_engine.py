from app.schemas import SignalRequest, SignalResponse


FACTOR_WEIGHTS = {
    "fundamental": 0.18,
    "capital_flow": 0.18,
    "industry": 0.16,
    "technical": 0.14,
    "valuation": 0.12,
    "news": 0.10,
    "risk": 0.12,
}


def evaluate_signal(request: SignalRequest) -> SignalResponse:
    weighted_score = 0.0
    total_weight = 0.0

    for factor, weight in FACTOR_WEIGHTS.items():
        value = request.factors.get(factor, 50)
        weighted_score += max(0, min(value, 100)) * weight
        total_weight += weight

    score = round(weighted_score / total_weight)
    probability_up = min(0.82, max(0.18, score / 100))
    probability_down = min(0.65, max(0.08, (100 - score) / 140))
    probability_flat = max(0.05, 1 - probability_up - probability_down)

    rating = "watch"
    if score >= 80:
        rating = "strong"
    elif score >= 65:
        rating = "constructive"
    elif score < 45:
        rating = "avoid"

    return SignalResponse(
        code=request.code,
        name=request.name,
        score=score,
        probability_up=round(probability_up, 2),
        probability_flat=round(probability_flat, 2),
        probability_down=round(probability_down, 2),
        rating=rating,
        reasons=[
            "Multi-factor score combines fundamentals, capital flow, industry, technicals, valuation, and news.",
            "Signal is probability-based and should be checked against position risk before execution.",
        ],
        risks=[
            "Market-wide liquidity can override company-level signals.",
            "Crowded AI-chain positions may amplify drawdowns.",
        ],
    )
