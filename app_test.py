import pytest
from app import app  # Make sure this matches your app's import path

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_knows_about_dinosaurs(client):
    response = client.get("/query?q=dinosaurs")
    assert response.data.decode() == "Dinosaurs ruled the Earth 200 million years ago"

def test_does_not_know_about_asteroids(client):
    response = client.get("/query?q=asteroids")
    assert response.data.decode() == "Unknown"