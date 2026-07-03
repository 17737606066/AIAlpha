from datetime import datetime
from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class JournalEntryCreate(BaseModel):
    title: str = Field(min_length=1, max_length=80)
    decision: str = Field(min_length=1, max_length=40)
    reason: str = Field(min_length=1, max_length=300)
    symbol: str | None = Field(default=None, max_length=40)


journal_entries: list[dict[str, object]] = [
    {
        "id": "seed-1",
        "created_at": "2026-07-03T09:30:00",
        "title": "系统启动",
        "symbol": None,
        "decision": "观察",
        "reason": "启动宏观、资金、产业、技术、风险模块。",
        "review_status": "pending",
    },
    {
        "id": "seed-2",
        "created_at": "2026-07-03T09:35:00",
        "title": "高位题材风险提示",
        "symbol": "高位题材股",
        "decision": "控仓",
        "reason": "风险雷达提示短线情绪股回撤风险上升。",
        "review_status": "pending",
    },
]


@router.get("/entries")
def list_entries() -> dict[str, object]:
    return {"entries": journal_entries}


@router.post("/entries")
def create_entry(entry: JournalEntryCreate) -> dict[str, object]:
    payload = {
        "id": str(uuid4()),
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "title": entry.title,
        "symbol": entry.symbol,
        "decision": entry.decision,
        "reason": entry.reason,
        "review_status": "pending",
    }
    journal_entries.insert(0, payload)
    return payload
