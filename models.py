from sqlalchemy import Column, Integer, DATE, TEXT, DECIMAL, DATETIME
from config import Base


class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    home_store = Column(Integer)
    customer_first_name = Column(TEXT)
    customer_email = Column(TEXT)
    customer_since = Column(DATE)
    loyalty_card_number = Column(TEXT)
    birthdate = Column(DATE)
    gender = Column(TEXT)
    birth_year = Column(Integer)


class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True)
    product_group = Column(TEXT)
    product_category = Column(TEXT)
    product_type = Column(TEXT)
    product = Column(TEXT)
    product_description = Column(TEXT)
    unit_of_measure = Column(TEXT)
    current_wholesale_price = Column(DECIMAL)
    current_retail_price = Column(TEXT)
    tax_exampt_yn = Column(TEXT)
    promo_yn = Column(TEXT)
    new_product_yn = Column(TEXT)


class Sales(Base):
    __tablename__ = "sales_reciepts"

    transaction_id = Column(Integer, primary_key=True)
    transaction_date = Column(DATE)
    transaction_time = Column(DATETIME)
    sales_outlet_id = Column(Integer)
    staff_id = Column(Integer)
    customer_id = Column(Integer)
    instore_yn = Column(TEXT)
    order_number = Column(Integer)
    line_item_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer)
    line_item_amount = Column(DECIMAL)
    unit_price = Column(DECIMAL)
    promo_item_yn = Column(TEXT)

