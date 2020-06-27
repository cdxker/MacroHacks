from flask import Blueprint, render_template, request, jsonify, abort
import random
from src.ext import bcrypt, db
from slugify import slugify
from flask_jwt_extended import jwt_required

user_bp = Blueprint('user', __name__)

