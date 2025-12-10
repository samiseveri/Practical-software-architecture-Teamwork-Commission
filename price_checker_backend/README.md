# Price Checker Backend

This is the backend system for the Price Checker application (TWC - PSA - 2025).

## Architecture
The system uses a layered architecture (Clean Architecture) using FastAPI and SQLAlchemy.
- **API Layer (`app/api`)**: Handles HTTP requests and input validation.
- **Service Layer (`app/services`)**: Contains business logic (e.g., Price Labeling Strategy).
- **CRUD Layer (`app/crud`)**: Handles direct database interactions (Repository Pattern).
- **Models (`app/models`)**: Database entities.
- **Schemas (`app/schemas`)**: Pydantic models for data transfer (DTOs).

## Features
- **User Management**: Admin (review, lock, delete), Store Users, Shoppers (implied).
- **Price Comparison**: Logic to find nearby stores and label prices (Strategy Pattern).
- **Security**: OAuth2 with JWT, password hashing.
- **Deployment**: Dockerized.

## How to Run

### Option 1: Docker (Recommended)
1. Ensure Docker is installed.
2. Run `docker-compose up --build`.
3. Open `http://localhost:8000/docs` to see the Swagger UI.

### Option 2: Local
1. `pip install -r requirements.txt`
2. `uvicorn app.main:app --reload`
