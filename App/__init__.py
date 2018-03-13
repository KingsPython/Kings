from flask import Flask

from App.ext import init_ext
from App.views.views import init_blue


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_blue(app=app)
    init_ext(app=app)
    return app


