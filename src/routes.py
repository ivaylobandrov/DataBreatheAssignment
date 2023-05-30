from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from src.queries import (
    birthday_customers_query,
    top_selling_products_query,
    last_order_per_customer_query,
)
from src.database import get_db

router = APIRouter()


@router.get("/customers/birthday")
async def get_birthday_customers(db: Session = Depends(get_db)):  # TODO Check if it is possible to move get_db in a different file
    """Get endpoint for today's birthday customers"""
    customers = birthday_customers_query(db)

    return customers


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
