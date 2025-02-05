
import pytest
from fastapi.testclient import TestClient
from app.main import create_application
from app.database import create_db_and_tables, drop_db_and_tables


@pytest.fixture(scope="module")
def client():
    app = create_application()
    with TestClient(app) as client:
        create_db_and_tables()
        yield client
        drop_db_and_tables()


def test_create_item(client: TestClient):
    response = client.post(
        "/items/",
        json={"name": "xxxx", "description": "xxxx"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["name"] == "xxxx"
    assert data["description"] == "xxxx"


def test_get_items(client: TestClient):
    response = client.get("/items/")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
