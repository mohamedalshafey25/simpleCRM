from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base
from app.routers import contacts
from app.routers import offers

# Create the FastAPI app
app = FastAPI()

# Enable CORS for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Include the contacts router
app.include_router(contacts.router)
# Include the offers router
app.include_router(offers.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple CRM API!"}
