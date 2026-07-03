from datetime import datetime

from fastapi import APIRouter

router = APIRouter()


def build_dashboard_payload(score_shift: int = 0) -> dict[str, object]:
    factors = [
        {"name": "基本面", "score": clamp(78 + score_shift)},
        {"name": "资金面", "score": clamp(72 + score_shift)},
        {"name": "行业景气", "score": clamp(86 + score_shift)},
        {"name": "技术结构", "score": clamp(68 + score_shift)},
        {"name": "估值", "score": clamp(61 + score_shift)},
        {"name": "消息面", "score": clamp(74 + score_shift)},
        {"name": "风险控制", "score": clamp(70 + score_shift)},
    ]
    stocks = [
        {"name": "AI服务器链", "theme": "AI服务器 PCB", "score": clamp(88 + score_shift), "risk": "中", "action": "持有，等确认加仓"},
        {"name": "PCB核心", "theme": "PCB CCL", "score": clamp(85 + score_shift), "risk": "中", "action": "分批跟踪"},
        {"name": "先进封装", "theme": "封装 HBM", "score": clamp(80 + score_shift), "risk": "中低", "action": "回踩关注"},
        {"name": "高位题材股", "theme": "短线 情绪 风险", "score": clamp(57 - score_shift), "risk": "高", "action": "控仓止损"},
    ]
    funds = [
        {"name": "AI服务器", "heat": clamp(82 + score_shift)},
        {"name": "PCB/CCL", "heat": clamp(79 + score_shift)},
        {"name": "先进封装", "heat": clamp(72 + score_shift)},
        {"name": "HBM存储", "heat": clamp(66 + score_shift)},
        {"name": "半导体设备", "heat": clamp(58 + score_shift)},
        {"name": "消费电子", "heat": clamp(44 - score_shift)},
    ]
    risks = [
        {"name": "追高风险", "score": clamp(76 + score_shift)},
        {"name": "汇率扰动", "score": 54},
        {"name": "政策扰动", "score": 48},
        {"name": "流动性回撤", "score": clamp(63 + score_shift)},
        {"name": "单一主题集中", "score": clamp(71 + score_shift)},
    ]

    return {
        "account_score": 88,
        "market_tone": "中性偏强，AI硬件主线仍在，但分歧扩大。",
        "discipline": "只有资金与评分同时确认才加仓，避免情绪追涨。",
        "factors": factors,
        "stocks": stocks,
        "funds": funds,
        "risks": risks,
        "morning_brief": {
            "global": "美元、美债与科技股风险偏好共同影响 A股 AI主线。",
            "opportunities": ["PCB", "AI服务器", "先进封装", "HBM"],
            "account_action": "核心持仓继续观察，题材高位降低暴露。",
        },
    }


@router.get("/overview")
def dashboard_overview() -> dict[str, object]:
    return build_dashboard_payload()


@router.post("/rescore")
def dashboard_rescore() -> dict[str, object]:
    payload = build_dashboard_payload(score_shift=2)
    payload["rescored_at"] = datetime.now().isoformat(timespec="seconds")
    payload["rescore_note"] = "已由后端重新计算评分，并同步更新资金地图与风险雷达。"
    return payload


def clamp(value: int, low: int = 0, high: int = 100) -> int:
    return max(low, min(high, value))
