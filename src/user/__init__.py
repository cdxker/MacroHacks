from flask import Flask
from .routes import user_bp
from . import models


def init_app(app: Flask):

    app.register_blueprint(user_bp)
