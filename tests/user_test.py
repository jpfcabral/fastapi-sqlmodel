from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_user():
    response = client.post('/users', data={
            "username": "test",
            "email": "test@gmail.com",
            "password": "mysecret"
        })   
    assert response.status_code == 201
    assert response.json() != {}