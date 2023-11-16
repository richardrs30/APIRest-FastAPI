""" 
*******************
API - FASTAPI BASIC
*******************
"""

from fastapi import FastAPI
from fastapi import status
from fastapi.responses import JSONResponse
from models import Alumno, ListAlumnos


app = FastAPI()

tabla_alumnos = []

#Traer todos los elemetos:
@app.get("/all_alumnos", status_code=status.HTTP_200_OK, response_model=ListAlumnos, tags=["Alumnos"])
def get_all_alumnos():
    """ 
    ## Response
        - alumnos: List(Alumno)
    """
    return ListAlumnos(alumnos = tabla_alumnos)


#CREAR
@app.post("/create_alumno", status_code=status.HTTP_201_CREATED, response_model=Alumno, summary="Este endpoint crea alumno", tags=["Alumnos"])
def create_alumno(alumno: Alumno):
    
    """ 
    ## Args
        - alumno: Alumno
    ## Response
        - alumno: Alumno
    """
    tabla_alumnos.append(alumno)
    return alumno.dict()  


#TRAER:
@app.get("/{id}", status_code=status.HTTP_200_OK, tags=["Alumnos"], response_model=Alumno)
def get_a_alumno(id: int):

    for alumno in tabla_alumnos:
        if alumno.id == id:
            return alumno 
    return JSONResponse(content={"message": "El alumno no fue encontrado."}, status_code=status.HTTP_404_NOT_FOUND)


#ELIMINAR:
@app.delete("/{id}", status_code=status.HTTP_200_OK, tags=["Alumnos"])
def delete_alumno(id:int):

    for alumno in tabla_alumnos:
        if alumno["id"] == id:
            alumno_sel = alumno
            tabla_alumnos.remove(alumno)
            return alumno_sel
    return {}


#Actualizar solo un elemento de la tabla
@app.patch("/{id}", status_code=status.HTTP_200_OK, tags=["Alumnos"])
def update_alumno(id: int, name:str, lastname:str, age:int, phone:str, email:str):

    for alumno in tabla_alumnos:
        if alumno["id"] == id:
            alumno["name"] = name
            alumno["lastname"] = lastname
            alumno["age"] = age
            alumno["phone"] = phone
            alumno["email"] = email 
            return alumno
    return {}