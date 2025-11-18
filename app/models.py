from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, index=True)
    referrer_id = Column(Integer, ForeignKey("customers.id"))

    referrer = relationship("Customer", remote_side=[id], backref="referrals")
    orders = relationship("Order", back_populates="customer")


class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    price = Column(Float)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    offer_id = Column(Integer, ForeignKey("offers.id"))

    customer = relationship("Customer", back_populates="orders")
    offer = relationship("Offer")


class FollowUp(Base):
    __tablename__ = "follow_ups"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    date = Column(String)
    notes = Column(String)

    order = relationship("Order")
