from sqlalchemy import Column, Integer, DATE, TEXT, DECIMAL, TIMESTAMP, TIME
from decimal import Decimal
from datetime import date, datetime, time
from src.config import Base


class Customer(Base):
    """Customer model"""

    __tablename__ = "customer"

    customer_id: Column[int] = Column(Integer, primary_key=True)
    home_store: Column[int] = Column(Integer)
    customer_first_name: Column[str] = Column(TEXT)
    customer_email: Column[str] = Column(TEXT)
    customer_since: Column[date] = Column(DATE)
    loyalty_card_number: Column[str] = Column(TEXT)
    birthdate: Column[date] = Column(DATE)
    gender: Column[str] = Column(TEXT)
    birth_year: Column[int] = Column(Integer)


class Product(Base):
    """Product model"""

    __tablename__ = "product"

    product_id: int = Column(Integer, primary_key=True)
    product_group: str = Column(TEXT)
    product_category: str = Column(TEXT)
    product_type: str = Column(TEXT)
    product: str = Column(TEXT)
    product_description: str = Column(TEXT)
    unit_of_measure: str = Column(TEXT)
    current_wholesale_price: Decimal = Column(DECIMAL)
    current_retail_price: str = Column(TEXT)
    tax_exampt_yn: str = Column(TEXT)
    promo_yn: str = Column(TEXT)
    new_product_yn: str = Column(TEXT)


class Sales(Base):
    """Sales model"""

    __tablename__ = "sales"

    transaction_id: int = Column(Integer, primary_key=True)
    transaction_date: date = Column(DATE)
    transaction_time: time = Column(TIME)
    sales_outlet_id: int = Column(Integer)
    staff_id: int = Column(Integer)
    customer_id: int = Column(Integer)
    instore_yn: str = Column(TEXT)
    order_number: int = Column(Integer)
    line_item_id: int = Column(Integer)
    product_id: int = Column(Integer)
    quantity: int = Column(Integer)
    line_item_amount: Decimal = Column(DECIMAL)
    unit_price: Decimal = Column(DECIMAL)
    promo_item_yn: str = Column(TEXT)
