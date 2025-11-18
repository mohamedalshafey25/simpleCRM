from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import crud, schemas

router = APIRouter()


@router.post("/offers/", response_model=schemas.Offer, status_code=201)
def create_offer(offer: schemas.OfferCreate, db: Session = Depends(get_db)):
    try:
        db_offer = crud.create_offer(db=db, offer=offer)
        return db_offer
    except Exception:
        # For now, treat any DB error as a 400 with a generic message
        raise HTTPException(status_code=400, detail="Could not create offer")


@router.get("/offers/", response_model=list[schemas.Offer])
def read_offers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_offers(db=db, skip=skip, limit=limit)
