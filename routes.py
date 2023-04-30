from fastapi import APIRouter
from fastapi import Depends
from datetime import date
from sqlalchemy import extract, func, cast, TIMESTAMP
from sqlalchemy.orm import Session


from config import SessionLocal
from models import Product, Sales, Customer

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/customers/birthday")
async def get_birthday_customers(db: Session = Depends(get_db)):
    """Get endpoint for birthday customers"""
    today: date = date.today()
    customers = (
        db.query(Customer)
        .filter(
            extract("month", Customer.birthdate) == today.month,
            extract("day", Customer.birthdate) == today.day,
        )
        .all()
    )
    customers_list: list = [
        {
            "customer_id": customer.customer_id,
            "customer_first_name": customer.customer_first_name,
        }
        for customer in customers
    ]
    return customers_list


# Endpoint to get top 10 selling products for a specific year
@router.get("/products/top-selling-products/{year}")
async def get_top_selling_products(year: int, db: Session = Depends(get_db)):
    """Get endpoint for top-selling products for a given 'year'"""
    # Query the database for total sales for each product for the specified year
    sales_query = (
        db.query(Sales.product_id, func.sum(Sales.quantity).label("total_sales"))
        .filter(extract("year", Sales.transaction_date) == year)
        .group_by(Sales.product_id)
        .order_by(func.sum(Sales.quantity).desc())
        .limit(10)
        .subquery()
    )

    # Join the sales_query with the Product table to get the product names
    products_query = (
        db.query(Product.product, sales_query.c.total_sales.label("total_sales"))
        .join(sales_query, Product.product_id == sales_query.c.product_id)
        .all()
    )

    # Return the results as a list of dictionaries in the desired format
    result = [
        {"product_name": p.product, "total_sales": p.total_sales}
        for p in products_query
    ]

    return {"products": result}


@router.get("/customers/last-order-per-customer")
def last_order_per_customer(db: Session = Depends(get_db)):
    """Get endpoint for last order for every customer"""
    subquery = (
        db.query(
            Sales.customer_id, func.max(Sales.transaction_date).label("last_order_date")
        )
        .group_by(Sales.customer_id)
        .subquery()
    )

    result = (
        db.query(
            Customer.customer_id,
            Customer.customer_email,
            cast(subquery.c.last_order_date, TIMESTAMP).label("last_order_date"),
        )
        .join(subquery, Customer.customer_id == subquery.c.customer_id)
        .all()
    )

    response: dict = {"customers": []}
    for row in result:
        response["customers"].append(
            {
                "customer_id": row.customer_id,
                "customer_email": row.customer_email,
                "last_order_date": row.last_order_date.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    return response
