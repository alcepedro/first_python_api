from fastapi import FastAPI, status
import requests
from fastapi.responses import JSONResponse
from models import *


app = FastAPI()


    
    


@app.get("/")
def root():
    return "todooo"

@app.post("/todo/{id}", status_code=status.HTTP_201_CREATED)
def create_todo(id: int):
    number.append(id)
    return "create todo item"

@app.get("/todo/{id}")
def read_todo(id: int):
    print(id)
    return f"read todo item with id {id}"

@app.put("/todo/{id}")
def update_todo(id: int):
    return f"update todo item with id {id}"

@app.delete("/todo/{id}")
def delete_todo(id: int):
    number.remove(id)
    return f"delete todo item with id {id}"

@app.get("/todo")
def read_todo_list():
    print(number)
    return "read todo list"



