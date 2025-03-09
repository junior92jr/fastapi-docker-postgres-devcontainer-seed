from fastapi.testclient import TestClient


def test_create_item(client: TestClient):
    """Tests creating an item with valid data."""
    response = client.post(
        "/items/",
        json={
            "name": "Gaming Laptop",
            "description": "A high-performance laptop for gaming.",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "Gaming Laptop"
    assert data["description"] == "A high-performance laptop for gaming."


def test_create_item_invalid(client: TestClient):
    """Tests creating an item with missing required fields should fail."""
    response = client.post("/items/", json={})  # Empty payload
    # Unprocessable Entity (validation error)
    assert response.status_code == 422


def test_get_items(client: TestClient):
    """Tests retrieving all items from the database."""
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)


def test_get_item(client: TestClient):
    """Tests retrieving a specific item by ID."""
    response = client.post(
        "/items/",
        json={
            "name": "Mechanical Keyboard",
            "description": "RGB backlit mechanical keyboard.",
        },
    )
    assert response.status_code == 200
    item_id = response.json()["id"]

    response = client.get(f"/items/{item_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == item_id
    assert data["name"] == "Mechanical Keyboard"
    assert data["description"] == "RGB backlit mechanical keyboard."


def test_get_non_existent_item(client: TestClient):
    """Tests retrieving a non-existent item should return 404."""
    response = client.get("/items/99999")  # ID that doesn't exist
    assert response.status_code == 404


def test_create_multiple_items(client: TestClient):
    """Tests if multiple items are correctly created and retrieved."""
    items = [
        {"name": "Wireless Mouse", "description": "Ergonomic wireless mouse."},
        {
            "name": "USB-C Hub",
            "description": "Multi-port adapter with HDMI, USB, and Ethernet.",
        },
    ]

    for item in items:
        response = client.post("/items/", json=item)
        assert response.status_code == 200

    response = client.get("/items/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2  # There should be at least 2 items now
