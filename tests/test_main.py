from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_chat_gia_lap():
    from llm import goi_llm

    assert "cau hoi" in goi_llm("xin chao")
