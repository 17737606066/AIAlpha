from datetime import date

from fastapi import APIRouter

router = APIRouter()


@router.get("/morning")
def morning_report() -> dict[str, object]:
    return {
        "date": date.today().isoformat(),
        "global_market": "neutral",
        "hotspots": ["AI infrastructure", "advanced packaging", "PCB"],
        "risks": ["policy surprise", "FX volatility", "crowded trades"],
        "account_action": "review risk budget before adding new positions",
    }
