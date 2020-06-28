from src.ext import ma
from .models import User, Message
from marshmallow import fields, Schema

class LoginSchema(Schema):

    username = fields.String()
    password = fields.String()

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User
        load_instance = True

class MessageSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Message
        load_instance = True
    
