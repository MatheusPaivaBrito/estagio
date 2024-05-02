from typing import Union
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
from config.db import engine
from models.models import *
from pydantic import BaseModel
import json

from fastapi.middleware.cors import CORSMiddleware

Session = sessionmaker(bind=engine)
db = Session()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8101",
    "http://localhost:8100",
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    usuarios = db.query(Usuario).all()
    response = list(map(lambda usuario: {
              'id': usuario.id,
              'nome': usuario.nome,
              'email': usuario.email,
       }, usuarios))
    return response

class usuarios(BaseModel):
    name: str
    email: str

@app.post("/add/")
async def add_user(usuario: usuarios):
    print(usuario)
    user = Usuario(nome = usuario.name, email = usuario.email)
    db.add(user)
    db.commit()
    return "ok"


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}