# AI Alpha Ultimate

AI Alpha Ultimate is an AI-assisted investment research and decision platform. It combines market data, portfolio tracking, strategy signals, risk control, and explainable AI reports into one personal research system.

> Motto: Let data speak, let probability decide, let discipline compound.

## Scope

- Frontend: Vue 3 dashboard for portfolio, radar, signals, and reports
- Backend: FastAPI APIs for scoring, reports, portfolio, and data orchestration
- AI engine: explainable multi-factor scoring and probability-style signals
- Data source layer: adapters for AkShare, AData, TuShare, and future providers
- Strategy layer: reusable signals and backtesting modules
- Portfolio layer: holdings, sizing, risk views, and decision logs
- Reports: morning brief, account review, and daily market notes

## Principles

1. No recommendation relies on one indicator.
2. The system outputs probabilities and confidence, not certainty.
3. Every signal explains its evidence.
4. Wrong calls become feedback for model improvement.
5. Macro, industry, company, capital flow, valuation, technicals, and risk are evaluated together.
6. This is research and decision support, not guaranteed financial advice.

## Quick Start

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
npm run dev
```

## Structure

```text
AIAlpha/
├── frontend/
├── backend/
├── ai_engine/
├── data_source/
├── strategy/
├── portfolio/
├── reports/
├── docs/
├── docker-compose.yml
└── README.md
```

## Risk Notice

This project is for research, education, and decision support. It does not provide guaranteed returns and should not replace independent judgment or licensed financial advice.
