from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200


def test_empty_question():
    res = client.post("/chat", json={"question": ""})
    assert res.status_code == 200


def test_chat():
    res = client.post("/chat", json={"question": "What is the revaluation fee?"})
    assert res.status_code == 200