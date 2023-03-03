# import fastAPI
from fastapi import FastAPI
from models import Languages, Programmer

# mock db

# start and instance
app = FastAPI()

db: list[Programmer] = [
    Programmer(id= 1, name="Mahtab", languages=[Languages.javascript]),
    Programmer(id= 2, name="Patrick", languages=[Languages.pascal, Languages.javascript]),
    Programmer(id= 3, name="Morteza", languages=[Languages.c_plus_plus, Languages.javascript]),
    Programmer(id= 4, name="Viviana", languages=[Languages.java, Languages.javascript]),
    Programmer(id= 5, name="Xiaodan", languages=[Languages.javascript, Languages.c_sharp]),
    Programmer(id= 6, name="Renu", languages=[Languages.javascript, Languages.java]),
    Programmer(id= 7, name="Prathima", languages=[Languages.javascript, Languages.c])
]

# create an endpoint
@app.get("/", response_model=str)
async def hello():
    return "Hello from FastAPI"

# send list of programmers
@app.get("/programmers", response_model=list[Programmer])
async def get_programmers():
    return db

@app.get("/programmers/{id}", response_model=list[Programmer])
async def get_programmer(id: int):
    response = next((programmer for programmer in db if programmer.id == id), None)
    return response