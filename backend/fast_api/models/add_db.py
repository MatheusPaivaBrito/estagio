from sqlalchemy import create_engine
from models.models import *
from config.db import engine, Base

def add_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

