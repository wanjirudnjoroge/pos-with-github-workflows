# Retail Store POS API

This project is a FastAPI-based point-of-sale backend for managing users, products, categories, customers, suppliers, sales, payments, and receipts.

## Features

- REST endpoints for core POS resources
- SQLAlchemy models and repositories
- Basic validation and error handling
- PostgreSQL support via `DATABASE_URL`

## Project structure

- `app/models`: SQLAlchemy models
- `app/repositories`: database access logic
- `app/routers`: API endpoints
- `app/schemas`: request/response schemas
- `app/services`: business logic for selected flows

## Running the tests locally

The project uses Python 3.10. The automated test suite uses an isolated in-memory
SQLite database, so PostgreSQL does not need to be running and development data is
never modified.

Create and activate a virtual environment:

```bash
python3.10 -m venv .venv
source .venv/bin/activate
