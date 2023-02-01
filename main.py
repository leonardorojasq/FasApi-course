from typing import Union
from fastapi import FastAPI

#creacion de una aplicacion FastAPIclear
app = FastAPI()

@app.get('/hola')
def index():
    return {"saludo":"hola"}



