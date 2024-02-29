from fastapi.testclient import TestClient
from interview_helper.app.run import app

client = TestClient(app)


def test_heath():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": 200, "description": "Server running"}
