from pydantic import BaseModel

class Students(BaseModel):
    id:int
    name:str
    age:int
    course:str
    city:str

class Employees(BaseModel):
    emp:int
    name:str
    salary:int
    department:str
    city:str


class Laptops(BaseModel):
    laptop_id: int
    brand: str
    model: str
    processor:str
    price:int
    

