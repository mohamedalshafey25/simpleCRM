from pydantic import BaseModel
from pydantic import ConfigDict
from typing import Optional


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    referrer_id: Optional[int] = None


class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    referrer_id: Optional[int] = None


class Customer(CustomerBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class OfferBase(BaseModel):
    title: str
    description: str
    price: float


class OfferCreate(OfferBase):
    pass


class Offer(OfferBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class OrderBase(BaseModel):
    customer_id: int
    offer_id: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class FollowUpBase(BaseModel):
    order_id: int
    notes: str


class FollowUpCreate(FollowUpBase):
    pass


class FollowUp(FollowUpBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
