from flask import Flask
from .routes import home_bp
from . import models


def init_app(app: Flask):

    app.register_blueprint(home_bp)
