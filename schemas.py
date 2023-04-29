from typing import List, Optional, Generic, TypeVar
from datetime import date, datetime
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel

T = TypeVar('T')


class CustomerSchema(BaseModel):
    customer_id: int
    home_store: int
    customer_first_name: str
    customer_email: str
    customer_since: date
    loyalty_card_number: str
    birthdate: date
    gender: str
    birth_year: int

    class Config:
        orm_mode = True


class Product(BaseModel):
    product_id: int
    product_group: str
    product_category: str
    product_type: str
    product: str
    product_description: str
    unit_of_measure: str
    current_wholesale_price: float
    current_retail_price: str
    tax_exampt_yn: str
    promo_yn: str
    new_product_yn: str

    class Config:
        orm_mode = True


class Request(GenericModel, Generic[T]):
    parameter: Optional[T] = Field(...)


class RequestCustomer(BaseModel):
    parameter: CustomerSchema = Field(...)


class Response(GenericModel, Generic[T]):
    # code: str
    # status: str
    # message: str
    result: Optional[T]


class LastOrderPerCustomer(BaseModel):
    customer_id: int
    customer_email: str
    last_order_date: datetime


class LastOrderResponse(BaseModel):
    customers: List[LastOrderPerCustomer]
