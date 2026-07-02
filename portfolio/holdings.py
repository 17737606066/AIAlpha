from dataclasses import dataclass


@dataclass
class Holding:
    code: str
    name: str
    quantity: int
    cost_price: float
    last_price: float

    @property
    def market_value(self) -> float:
        return self.quantity * self.last_price

    @property
    def unrealized_pnl(self) -> float:
        return self.quantity * (self.last_price - self.cost_price)
