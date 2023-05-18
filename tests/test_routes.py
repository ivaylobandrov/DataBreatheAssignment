from fastapi import FastAPI
from starlette.testclient import TestClient

from src import models
from src.config import engine
from src.routes import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router)


def test_get_birthday_customers():
    with TestClient(app) as client:
        response = client.get("/customers/birthday")
        assert response.status_code == 200


def test_get_top_selling_products():
    with TestClient(app) as client:
        response = client.get("/products/top-selling-products/2022")
        assert response.status_code == 200


def test_last_order_per_customer():
    with TestClient(app) as client:
        response = client.get("/customers/last-order-per-customer")
        assert response.status_code == 200
