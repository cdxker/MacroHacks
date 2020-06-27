from src.ext import db
from datetime import datetime
import random
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship

user_conversation = db.Table('user_conversation',
        Column('user_id', Integer, db.ForeignKey('user.id')),
        Column('conversation_id', Integer, db.ForeignKey('conversation.id'))
)

class User(db.Model):

    id = Column(Integer, primary_key=True)

    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String(256))
    slug = Column(String, index= True)

    firstName = Column(String)
    lastName = Column(String)
    age = Column(Integer())
    timezone = Column(String)
    description = Column(String(175))
    speciality = Column(String)

    conversations = relationship('Conversation', secondary=user_conversation, backref=db.backref('users', lazy='dynamic'))
    skills = relationship('Skills', backref=db.backref('skills', lazy='dynamic'))
    messages = relationship('Message', backref=db.backref('user', lazy='dynamic'))



class Conversation(db.Model):

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime(), default=datetime.utcnow)

    messages = relationship('Conversation', backref=db.backref('conversation', lazy='dynamic'))

class Message(db.Model):

    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, db.ForeignKey('user.id'))
    conversation_id = Column('conversation_id', Integer, db.ForeignKey('conversation.id'))
    body = Column(String)
    sent_time = Column(DateTime(), default=datetime.utcnow)

class Skill(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column('user_id', Integer, db.ForeignKey('user.id'))
    body = Column(String)
