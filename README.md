# FastAPI-mini-project
FastAPI mini project demonstrating REST API development with Student, Employee, and Laptop endpoints using Pydantic validation and Swagger UI.


# FastAPI Endpoints Practice

## Project Description

This project demonstrates FastAPI basics by creating REST API endpoints for:

- Students
- Employees
- Laptops

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Endpoints

### Students

POST /students

Attributes

- student_id
- name
- age
- course
- city

### Employees

POST /employees

Attributes

- emp_id
- name
- department
- salary
- experience

### Laptops

POST /laptops

Attributes

- laptop_id
- brand
- model
- processor
- price

## Run Project

```bash
uvicorn main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```
