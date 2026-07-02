from dataclasses import dataclass


@dataclass(frozen=True)
class Signal:
    code: str
    name: str
    score: int
    rating: str
    reasons: list[str]


def score_stock(code: str, name: str, factors: dict[str, float]) -> Signal:
    score = round(sum(factors.values()) / max(len(factors), 1))
    rating = "watch"
    if score >= 80:
        rating = "strong"
    elif score >= 65:
        rating = "constructive"
    elif score < 45:
        rating = "avoid"

    return Signal(
        code=code,
        name=name,
        score=score,
        rating=rating,
        reasons=["Composite score generated from supplied factors."],
    )
