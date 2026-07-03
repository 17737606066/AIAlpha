from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_dashboard_overview():
    response = client.get("/api/dashboard/overview")
    payload = response.json()

    assert response.status_code == 200
    assert payload["account_score"] >= 80
    assert payload["factors"]
    assert payload["stocks"]
    assert payload["funds"]
    assert payload["risks"]
    assert "morning_brief" in payload


def test_dashboard_rescore():
    response = client.post("/api/dashboard/rescore")
    payload = response.json()

    assert response.status_code == 200
    assert payload["rescore_note"]
    assert payload["rescored_at"]
    assert payload["factors"]
    assert payload["funds"]
    assert payload["risks"]


def test_morning_report():
    response = client.get("/api/reports/morning")
    payload = response.json()

    assert response.status_code == 200
    assert "hotspots" in payload
    assert "risks" in payload


def test_signal_evaluate():
    response = client.post(
        "/api/signals/evaluate",
        json={
            "code": "300476",
            "name": "AI Chain Candidate",
            "factors": {
                "fundamental": 80,
                "capital_flow": 75,
                "industry": 88,
                "technical": 70,
                "valuation": 62,
                "news": 72,
                "risk": 68,
            },
        },
    )
    payload = response.json()

    assert response.status_code == 200
    assert payload["score"] >= 70
    assert payload["rating"] in {"watch", "constructive", "strong"}
    assert payload["reasons"]
    assert payload["risks"]
