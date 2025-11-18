# Simple CRM Application

This is a simple CRM (Customer Relationship Management) web application built using FastAPI, SQLite, and SQLAlchemy. The application allows for managing customers, offers, orders, and follow-ups.

## Project Structure

```
simple-crm
├── app
│   ├── main.py          # Main entry point for the FastAPI application
│   ├── database.py      # Database connection and session management
│   ├── models.py        # SQLAlchemy models for the database tables
│   ├── crud.py          # Functions for database operations (CRUD)
│   ├── schemas.py       # Pydantic schemas for data validation
│   ├── routers
│   │   └── contacts.py  # API routes for customer management
│   └── core
│       └── config.py    # Configuration settings for the application
├── tests
│   └── test_main.py     # Unit tests for the FastAPI application
├── requirements.txt      # Project dependencies
├── pyproject.toml        # Project configuration and metadata
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd simple-crm
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   # Simple CRM

   A small FastAPI-based CRM example (customers, offers, orders, follow-ups).

   ## Development (local)

   1. Create a virtual environment and install requirements:

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

   2. Copy `.env.example` to `.env` and edit values if needed.

   3. Run the app:

   ```powershell
   $env:PYTHONPATH="c:\Users\A store\simple-crm"
   uvicorn app.main:app --reload
   ```

   4. Open Swagger UI: http://127.0.0.1:8000/docs

   ## Using Docker (with Postgres)

   ```powershell
   docker-compose up --build
   ```

   This runs Postgres and the FastAPI app. The web service uses the `DATABASE_URL` environment variable.

   ## Database migrations (Alembic)

   Install alembic (if not installed):

   ```powershell
   pip install alembic
   ```

   Create a new migration (auto):

   ```powershell
   alembic revision --autogenerate -m "message"
   ```

   Apply migrations:

   ```powershell
   alembic upgrade head
   ```

   The repository includes an initial migration at `alembic/versions/0001_initial.py`.

   ## Frontend

   There's a minimal placeholder in `frontend/` demonstrating how the UI might call the API.

   ## Notes

   - CORS is enabled for `http://localhost:3000` to ease local frontend development.
   - Configuration is read from environment variables or `.env` using `app/core/config.py`.
   - Consider using Postgres in production instead of SQLite.

   ## Contributing

   Contributions welcome — open an issue or PR.

   ---
