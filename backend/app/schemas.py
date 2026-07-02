from pydantic import BaseModel, Field


class Holding(BaseModel):
    code: str
    name: str
    quantity: int = Field(ge=0)
    cost_price: float = Field(gt=0)
    last_price: float = Field(gt=0)


class SignalRequest(BaseModel):
    code: str
    name: str
    factors: dict[str, float] = Field(default_factory=dict)


class SignalResponse(BaseModel):
    code: str
    name: str
    score: int
    probability_up: float
    probability_flat: float
    probability_down: float
    rating: str
    reasons: list[str]
    risks: list[str]
