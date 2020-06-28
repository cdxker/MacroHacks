from flask import Blueprint, render_template, request, url_for, abort, redirect, flash, jsonify
import random
from src.ext import bcrypt, db
from .schemas import UserSchema, LoginSchema, MessageSchema
from .models import User, Message, Conversation
from slugify import slugify
from flask_login import login_user, current_user, logout_user, login_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=["GET", "POST"])
def register():

    user = UserSchema.load(request.form)
    user.password = bcrypt.generate_password_hash(user.password).decode('utf-8')
    user.slug = slugify(user.username)
    
    if User.query.filter_by(slug=user.slug).first():
        return jsonify({"status" : "Error", "msg" : "Username already exists"})

    if User.query.filter_by(email=user.email).first():
        return jsonify({"status" : "Error", "msg" : "Email already exists"})

    db.session.add(user)
    db.session.commit()
    
    return jsonify({ "status" : "Success" })

@user_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        schema = LoginSchema()
        body = schema.load(request.form)
        
        user = User.query.filter_by(username=body["username"]).first()
        if user and bcrypt.check_password_hash(user.password, body["password"]):
            login_user(user, remember=form.remember.data)
            flash("You are now logged in", "success")
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for("home.home"))
        return jsonify({ "status": "Error", "msg": "Wrong username or password" })

    return render_template('login.html')


@user_bp.route("/home")
@login_required
def home():

    return render_template("home.html")

@user_bp.route("/all_chats")
@login_required
def messages():
    return render_template("all_chats.html")

@user_bp.route("/chat")
@login_required
def chat():
    return render_template("chat.html")

############### JSON API STUFF ###############

@user_bp.route("/send_message", methods=["POST"])
@login_required
def send_message():

    message = MessageSchema().load(request.json)
    message.user_id = current_user.id
    db.session.add(message)
    db.session.commit()

@user_bp.route("/messages/<convo_id>")
def get_messages(convo_id):

    convo = Conversation.query.get_or_404(convo_id)

    return jsonify(MessageSchema(many=True).dump(convo.messages))

