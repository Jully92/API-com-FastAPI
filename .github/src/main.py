import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Pydantic é um pré requisito para usar o BaseModel
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

#Cadastrando alunos
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

#Atualiza algo no sistema (cadastro)
@app.put ("/estudantes/update/{id_estudante}")
async def update_estudante(id_estudante: int):
    return id_estudante > 0

#Remove algo do sistema (cadastro)
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0