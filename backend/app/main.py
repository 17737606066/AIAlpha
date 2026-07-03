from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.routers import dashboard, journal, portfolio, reports, signals

app = FastAPI(title=settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.allowed_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, prefix="/api/dashboard", tags=["dashboard"])
app.include_router(journal.router, prefix="/api/journal", tags=["journal"])
app.include_router(portfolio.router, prefix="/api/portfolio", tags=["portfolio"])
app.include_router(signals.router, prefix="/api/signals", tags=["signals"])
app.include_router(reports.router, prefix="/api/reports", tags=["reports"])


@app.get("/api/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "service": settings.app_name}
