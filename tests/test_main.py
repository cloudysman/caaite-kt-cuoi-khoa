from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    # Co y sai de lan chay CI bi do.
    assert response.status_code == 500
