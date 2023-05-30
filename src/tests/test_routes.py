from fastapi.testclient import TestClient

from src.main import app


def test_get_birthday_customers():
    with TestClient(app) as client:
        response = client.get("/customers/birthday")
        assert response.status_code == 200
        data = response.json()  # TODO check how to create querysets and compare the real data
        assert isinstance(data, list)


def test_get_top_selling_products():
    with TestClient(app) as client:
        response = client.get("/products/top-selling-products/2019")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "products" in data
        products = data["products"]
        assert isinstance(products, list)


def test_last_order_per_customer():
    with TestClient(app) as client:
        response = client.get("/customers/last-order-per-customer")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
