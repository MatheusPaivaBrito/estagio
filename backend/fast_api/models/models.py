from sqlalchemy import Column, Integer, String
from config.db import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(length=50))
    email = Column(String(length=100), unique=True)