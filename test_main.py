from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call/Search for Wiki"}


def test_read_phrases():
    response = client.get("/phrases/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API. Call/Search for Wiki"}
