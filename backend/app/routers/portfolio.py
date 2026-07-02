from fastapi import APIRouter

from app.schemas import Holding

router = APIRouter()


@router.get("/summary")
def portfolio_summary() -> dict[str, object]:
    return {
        "account_score": 88,
        "risk_level": "medium",
        "suggestion": "Hold core positions and wait for stronger confirmation before adding exposure.",
        "exposure": {"ai_chain": 0.62, "cash": 0.18, "other": 0.20},
    }


@router.post("/holdings")
def upsert_holding(holding: Holding) -> dict[str, object]:
    market_value = holding.quantity * holding.last_price
    cost = holding.quantity * holding.cost_price
    return {
        "holding": holding,
        "market_value": round(market_value, 2),
        "unrealized_pnl": round(market_value - cost, 2),
    }
