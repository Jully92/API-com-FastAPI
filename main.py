import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Estudante (BaseModel):
    name: str
    curso: str
    ativo: bool

#127.0.0.1:8000/
@app.get ("/helloworld")
async def root():
    return {"message": "Hello World"}

#127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True,"num_aleatorio": random.randint(0, 2000)}

@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

#Atualiza
@app.put ("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

#Remove
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_item(id_estudante: int):
    return id_estudante > 0