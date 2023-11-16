#Models imita las tablas de la base de datos 
from pydantic import BaseModel 
from typing import List

class Alumno(BaseModel):
    id: int = 1
    name: str = "richi"
    lastname: str = "valens"
    age: int = 25
    phone: str = "921894342"
    email: str = "richi_valens@gmail.com"


    class Config:
        json_schema_extra = {
            "example": { 
                "id": 1, 
                "name": "richy",
                "lastname": "valens",
                "age": 23,
                "phone": "921894342",
                "email": "richi_valens@gmail.com",      
            }
        }
 

class ListAlumnos(BaseModel):
    alumnos: List[Alumno]

    class Config:
        json_schema_extra = {
            "example": {
                "alumnos":[
                    {
                        "id": 1, 
                        "name": "richy",
                        "lastname": "valens",
                        "age": 23,
                        "phone": "921894342",
                        "email": "richi_valens@gmail.com",
                    },
                    {
                        "id": 2, 
                        "name": "john",
                        "lastname": "lennon",
                        "age": 35,
                        "phone": "11122342",
                        "email": "john_lennon@gmail.com",
                    }
                ] 
            }
        }