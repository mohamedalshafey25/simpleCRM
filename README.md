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
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

5. **Access the API:**
   Open your browser and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## Usage

- Use the API endpoints to manage customers, offers, orders, and follow-ups.
- Refer to the API documentation for detailed information on available endpoints and their usage.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.


# مشروع نظام إدارة العملاء والمبيعات البسيط (Simple CRM)

## الهدف
إنشاء تطبيق ويب يعتمد على جداول بيانات علائقية (Relational Database) لإدارة العملاء، العروض، الطلبات، والمتابعات.

## التقنيات المطلوبة
1.  **Backend:** Python 3.10+
2.  **Web Framework:** FastAPI
3.  **Database:** SQLite (باستخدام ملف محلي `crm.db`)
4.  **ORM:** SQLAlchemy (لإدارة الجداول والعلاقات)

## تفاصيل الجداول العلائقية (SQLAlchemy Models)
1.  **Customer:** `id`, `name`, `email`, `phone`, `referrer_id` (Self-referential link to another Customer).
2.  **Offer:** `id`, `customer_id`, `title`, `amount`, `status`.
3.  **Order:** `id`, `customer_id`, `offer_id` (Optional link), `total_amount`, `order_date`.
4.  **FollowUp:** `id`, `customer_id`, `followup_date`, `notes`, `is_completed`.