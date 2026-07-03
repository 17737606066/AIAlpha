from fastapi import APIRouter

router = APIRouter()


@router.get("/overview")
def dashboard_overview() -> dict[str, object]:
    factors = [
        {"name": "基本面", "score": 78},
        {"name": "资金面", "score": 72},
        {"name": "行业景气", "score": 86},
        {"name": "技术结构", "score": 68},
        {"name": "估值", "score": 61},
        {"name": "消息面", "score": 74},
        {"name": "风险控制", "score": 70},
    ]
    stocks = [
        {"name": "AI服务器链", "theme": "AI服务器 PCB", "score": 88, "risk": "中", "action": "持有，等确认加仓"},
        {"name": "PCB核心", "theme": "PCB CCL", "score": 85, "risk": "中", "action": "分批跟踪"},
        {"name": "先进封装", "theme": "封装 HBM", "score": 80, "risk": "中低", "action": "回踩关注"},
        {"name": "高位题材股", "theme": "短线 情绪 风险", "score": 57, "risk": "高", "action": "控仓止损"},
    ]
    funds = [
        {"name": "AI服务器", "heat": 82},
        {"name": "PCB/CCL", "heat": 79},
        {"name": "先进封装", "heat": 72},
        {"name": "HBM存储", "heat": 66},
        {"name": "半导体设备", "heat": 58},
        {"name": "消费电子", "heat": 44},
    ]
    risks = [
        {"name": "追高风险", "score": 76},
        {"name": "汇率扰动", "score": 54},
        {"name": "政策扰动", "score": 48},
        {"name": "流动性回撤", "score": 63},
        {"name": "单一主题集中", "score": 71},
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
