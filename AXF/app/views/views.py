from flask import Blueprint, render_template, redirect, request, url_for, make_response, config, g, current_app



blue = Blueprint('blue', __name__)


def init_blue(app):
    app.register_blueprint(blueprint=blue)


@blue.route('/')
def hello_world():
    return 'Hello World'