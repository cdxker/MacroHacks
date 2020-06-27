from src.ext import db, login_manager
from datetime import datetime
import random
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.schema import Table
from sqlalchemy.orm import relationship
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

user_conversation = db.Table('user_conversation',
        Column('user_id', Integer, db.ForeignKey('user.id')),
        Column('conversation_id', Integer, db.ForeignKey('conversation.id'))
)

class Likes(db.Model):

    id = Column(Integer, primary_key=True)
    liked_account_id = Column(Integer, db.ForeignKey('user.id'))
    current_account = Column(Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):

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

    conversations = relationship('Conversation', secondary=user_conversation, backref='users')
    skills = relationship('Skill', backref='skill')
    messages = relationship('Message', backref='user')

class Conversation(db.Model):

    id = Column(Integer, primary_key=True)
    created_on = Column(DateTime(), default=datetime.utcnow)

    messages = relationship('Message', backref='conversation')

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
