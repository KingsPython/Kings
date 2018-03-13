from flask import Flask

from app.views.views import init_blue
from ext import init_ext
from settings import env


def create_app(mode):


    app = Flask(__name__)

    app.config.from_object(env[mode])


    init_blue(app)
    init_ext(app)


    return app