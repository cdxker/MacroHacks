from flask import Blueprint, render_template, request, url_for, abort, redirect, flash
import random
from src.ext import bcrypt, db
from .schemas import UserSchema
from .models import User
from slugify import slugify
from flask_login import login_user, current_user, logout_user, login_required

user_bp = Blueprint('user', __name__)


@user_bp.route('/register', methods=["GET", "POST"])
def register():
    # if current_user.is_authenticated:
    #     return redirect(url_for('forum.main'))
    # form = RegistrationForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     default_images = [f"default{i}.jpg" for i in range(1, 5)]
    #     user = User(username=form.username.data, email=form.email.data, password=hashed_password, image_file=random.choice(default_images))
    #     db.session.add(user)
    #     db.session.commit()
    #     flash('Your account has been created you are now able to login', 'success')
    #     redirect(url_for("forum.login"))
    return render_template('register.html')

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    # schema = UserSchema()
    # form = schema.load(request.form)

    # if current_user.is_authenticated:
    #     return redirect(url_for("user.home"))

    # if request.method == "POST":

    #     user = User.query.filter_by(username=form["username"]).first()
    #     if user and bcrypt.check_password_hash(user.password, form.password.data):
    #         login_user(user, remember=True)
    #         flash("You are now logged in", "success")
    #         next_page = request.args.get('next')
    #         return redirect(next_page) if next_page else redirect(url_for("home.home"))
    #     else: 
    #         flash("Wrong username or password", "warning")


    return render_template('login.html')


@user_bp.route("/home")
def home():

    return render_template("home.html")

@user_bp.route("/all_chats")
def messages():
    return render_template("all_chats.html")

@user_bp.route("/chat/")
def chat():
    return render_template("chat.html")

