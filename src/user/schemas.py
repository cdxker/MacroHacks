from src.ext import ma
from .models import User
from marshmallow import fields, Schema

class UserSchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = User

