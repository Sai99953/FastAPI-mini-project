# In FastAPI, there are 3 main ways to send data from the client to the server:
# Parameter Type	Sent In	                  Used For                           Example
# Path Parameter	URL Path	              Identify a specific resource       /students/101
# Query Parameter	After ? in URL            Filter, Search, Sort               /students?city=Hyderabad
# Body Parameter	Request Body(JSON)        Create or Update data              { "name": "Sai" }

from fastapi import FastAPI 
from data_Storage import student,employee,laptop
from Base_model import Students,Employees,Laptops

app = FastAPI() 

# Path Parameter
@app.get("/employee/{emp_id}")
def employee_details(emp_id: int):
    for emp in employee:
        if emp["EMP_id"] == emp_id:
            return {
                "message": "Welcome to FastAPI",
                "employee_details": emp
            }
    return {
        "message": "Welcome to FastAPI",
        "error": f"No employee found with ID {emp_id}"
    }

# # Quary Parameter
@app.get("/employee")  #Used with ? mark
def employee(EMP_id:int, Name:str, Salary:int, Department: str, City: str):
    return [EMP_id,Name,Salary,Department,City]


# Body Parameters
@app.post("/students")
def create_student(student:Students):
    return {
        "Message":"Student details created successfully","Data":student
    }
# --------------------------Employee------------------------------ #

# Employee
@app.post("/employees")
def create_employee(employee: Employees):
    return {
        "message": "Employee Created Successfully",
        "employee": employee
    }
# --------------------------Laptop--------------------------------- #

# Laptop
@app.post("/laptops")
def create_laptop(laptop: Laptops):
    return {
        "message": "Laptop Created Successfully",
        "laptop": laptop
    }







