# FastAPI Project 1

This project is a simple product management API built with FastAPI. It demonstrates how to create a RESTful backend that can create, read, update, and delete product records stored in a SQLite database.

## What this project does

- Provides a basic API for managing products.
- Supports CRUD operations through endpoints such as:
  - GET /products
  - GET /products/{id}
  - POST /products
  - PUT /products/{id}
  - DELETE /products/{id}
- Uses SQLAlchemy ORM for database interaction.
- Includes a simple frontend folder for interacting with the API.

## Why I built it

This project was a beginner-friendly way to learn the basics of FastAPI. It helped me understand how to:

- Create API routes with FastAPI.
- Use path parameters and request bodies.
- Work with Pydantic models for data validation.
- Connect FastAPI with a database using SQLAlchemy.
- Use dependency injection for database sessions.
- Build simple CRUD endpoints in a real project.

## Learning highlights

While building this project, I learned how FastAPI makes it easy to create clean and efficient APIs with minimal code. It also helped me understand the structure of a small backend project and how different pieces such as models, database setup, and routes fit together.

## How to run

1. Install the required packages:
   ```bash
   pip install fastapi uvicorn sqlalchemy
   ```

2. Start the server:
   ```bash
   uvicorn main:app --reload
   ```

3. Open the API documentation at:
   - http://127.0.0.1:8000/docs

## Project Structure

- main.py - the FastAPI app and route definitions
- models.py - Pydantic models for request and response data
- database.py - database connection setup
- database_models.py - SQLAlchemy database models
- frontend/ - a simple frontend to interact with the API
