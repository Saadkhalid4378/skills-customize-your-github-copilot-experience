# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Learn how to build RESTful APIs using the FastAPI framework. Practice defining endpoints, request validation, and generating automatic API documentation.

## 📝 Tasks

### 🛠️ Create CRUD API Endpoints

#### Description

Build a FastAPI application that provides create, read, update, and delete operations for a simple resource.

#### Requirements
Completed program should:

- Use FastAPI to define a web application
- Implement at least one `GET`, `POST`, `PUT`/`PATCH`, and `DELETE` endpoint
- Use an in-memory data store (list or dictionary) for the resource data
- Return JSON responses with meaningful status data
- Include example input and output in the code comments if helpful

### 🛠️ Add Validation and API Documentation

#### Description

Use Pydantic models to validate request bodies and enable FastAPI's built-in documentation pages.

#### Requirements
Completed program should:

- Define a Pydantic model for the resource schema
- Validate incoming request data for creation and updates
- Serve automatic API docs at `/docs` and `/redoc`
- Return appropriate error responses for invalid input
