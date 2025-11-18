from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Simple CRM API!"}


def test_create_customer():
    response = client.post(
        "/customers/", json={"name": "John Doe", "email": "john@example.com"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"
    assert response.json()["email"] == "john@example.com"


def test_create_duplicate_customer():
    # Attempt to create another customer with the same email should return 400
    response = client.post(
        "/customers/", json={"name": "Jane Doe", "email": "john@example.com"}
    )
    assert response.status_code == 400
    assert "Email already registered" in response.json().get("detail", "")


def test_read_customer():
    response = client.get("/customers/1")
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"


def test_update_customer():
    response = client.put("/customers/1", json={"name": "John Smith"})
    assert response.status_code == 200
    assert response.json()["name"] == "John Smith"


def test_delete_customer():
    response = client.delete("/customers/1")
    assert response.status_code == 204
    response = client.get("/customers/1")
    assert response.status_code == 404


def test_create_offer_and_list():
    # Create an offer
    response = client.post(
        "/offers/", json={"title": "Test Offer", "description": "Desc", "price": 19.99}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Offer"
    assert data["price"] == 19.99

    # List offers
    response = client.get("/offers/")
    assert response.status_code == 200
    offers = response.json()
    assert any(o["title"] == "Test Offer" for o in offers)
