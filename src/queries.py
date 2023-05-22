from datetime import date
from sqlalchemy import extract, func, cast, TIMESTAMP

from src.models import Customer, Sales, Product


def birthday_customers_query(db):
    """Today's birthday customers query."""
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


def top_selling_products_query(year, db):
    """10 Top-selling products query for a specific year."""
    sales_query = (
        db.query(Sales.product_id, func.sum(Sales.quantity).label("total_sales"))
        .filter(extract("year", Sales.transaction_date) == year)
        .group_by(Sales.product_id)
        .order_by(func.sum(Sales.quantity).desc())
        .limit(10)
        .subquery()
    )

    products_query = (
        db.query(Product.product, sales_query.c.total_sales.label("total_sales"))
        .join(sales_query, Product.product_id == sales_query.c.product_id)
        .all()
    )

    result = [
        {"product_name": p.product, "total_sales": p.total_sales}
        for p in products_query
    ]

    return result


def last_order_per_customer_query(db):
    """Last order per customer query."""
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
