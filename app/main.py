from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import contacts
from app.routers import offers

# Create the FastAPI app
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the contacts router
app.include_router(contacts.router)
# Include the offers router
app.include_router(offers.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple CRM API!"}
