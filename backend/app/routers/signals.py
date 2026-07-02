from fastapi import APIRouter

from app.schemas import SignalRequest, SignalResponse
from app.services.alpha_engine import evaluate_signal

router = APIRouter()


@router.post("/evaluate", response_model=SignalResponse)
def evaluate(request: SignalRequest) -> SignalResponse:
    return evaluate_signal(request)
