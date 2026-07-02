# Architecture

AI Alpha Ultimate is split into clear layers so each module can evolve without turning into a black box.

## Layers

- Data source layer: collects market, company, macro, and news data.
- AI engine: transforms raw data into explainable factor scores.
- Strategy layer: converts scores into signals and backtests.
- Portfolio layer: maps signals to holdings, exposure, and risk budget.
- Report layer: generates daily research briefings.
- Frontend: shows the current account, signals, alerts, and reports.

## Near-Term Roadmap

1. Add real market data adapters.
2. Persist holdings and decision logs in PostgreSQL.
3. Add daily report generation.
4. Add backtest APIs.
5. Add authentication before any personal portfolio data is stored.
