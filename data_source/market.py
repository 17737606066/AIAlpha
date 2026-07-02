class MarketDataAdapter:
    """Base adapter for market data providers."""

    provider_name = "base"

    def latest_quote(self, code: str) -> dict[str, object]:
        raise NotImplementedError


class MockMarketDataAdapter(MarketDataAdapter):
    provider_name = "mock"

    def latest_quote(self, code: str) -> dict[str, object]:
        return {"code": code, "price": 0.0, "change_pct": 0.0, "provider": self.provider_name}
