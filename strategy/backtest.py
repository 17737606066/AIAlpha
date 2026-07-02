def simple_backtest(returns: list[float]) -> dict[str, float]:
    if not returns:
        return {"total_return": 0.0, "max_drawdown": 0.0, "win_rate": 0.0}

    equity = 1.0
    peak = 1.0
    max_drawdown = 0.0
    wins = 0

    for item in returns:
        equity *= 1 + item
        peak = max(peak, equity)
        max_drawdown = min(max_drawdown, equity / peak - 1)
        wins += int(item > 0)

    return {
        "total_return": round(equity - 1, 4),
        "max_drawdown": round(max_drawdown, 4),
        "win_rate": round(wins / len(returns), 4),
    }
