from src.ext import db
import random
from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship

class User(db.Model):

    id = Column(Integer, primary_key=True)

    email = Column(String, unique=True)
    password = Column(String(256))
    username = Column(String, unique=True)
    slug = Column(String, index= True)
