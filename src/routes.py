from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.config import SessionLocal
from src.queries import (
    birthday_customers_query,
    top_selling_products_query,
    last_order_per_customer_query,
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/customers/birthday")
async def get_birthday_customers(db: Session = Depends(get_db)):
    """Get endpoint for today's birthday customers"""
    customers = birthday_customers_query(db)

    return customers


# Endpoint to get top 10 selling products for a specific year
@router.get("/products/top-selling-products/{year}")
async def get_top_selling_products(year: int, db: Session = Depends(get_db)):
    """Get endpoint for top-selling products for a given 'year'"""
    top_selling_products = top_selling_products_query(year, db)

    return {"products": top_selling_products}


@router.get("/customers/last-order-per-customer")
def last_order_per_customer(db: Session = Depends(get_db)):
    """Get endpoint for last order of every customer"""
    last_order_per_each_customer = last_order_per_customer_query(db)

    return last_order_per_each_customer
