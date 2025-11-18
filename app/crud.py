from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from . import models, schemas


def get_customer_by_email(db: Session, email: str) -> models.Customer | None:
    return db.query(models.Customer).filter(models.Customer.email == email).first()


def get_customer(db: Session, customer_id: int) -> models.Customer | None:
    return db.query(models.Customer).filter(models.Customer.id == customer_id).first()


def get_customers(db: Session, skip: int = 0, limit: int = 10) -> List[models.Customer]:
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CustomerCreate) -> models.Customer:
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    try:
        db.commit()
        db.refresh(db_customer)
        return db_customer
    except IntegrityError:
        db.rollback()
        raise


def update_customer(
    db: Session, customer_id: int, customer: schemas.CustomerUpdate
) -> models.Customer | None:
    db_customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if db_customer:
        for key, value in customer.model_dump(exclude_unset=True).items():
            setattr(db_customer, key, value)
        db.commit()
        db.refresh(db_customer)
    return db_customer


def delete_customer(db: Session, customer_id: int) -> models.Customer | None:
    db_customer = (
        db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    )
    if db_customer:
        db.delete(db_customer)
        db.commit()
    return db_customer


def get_offers(db: Session, skip: int = 0, limit: int = 10) -> List[models.Offer]:
    return db.query(models.Offer).offset(skip).limit(limit).all()


def create_offer(db: Session, offer: schemas.OfferCreate) -> models.Offer:
    db_offer = models.Offer(**offer.model_dump())
    db.add(db_offer)
    try:
        db.commit()
        db.refresh(db_offer)
        return db_offer
    except IntegrityError:
        db.rollback()
        raise
