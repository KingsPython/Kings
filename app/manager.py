from flask import Flask
from flask_script import Manager

from flask_migrate import MigrateCommand

from App import init_blue, init_ext


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite3.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    init_blue(app=app)
    init_ext(app=app)
    return app







app = create_app()
print(app)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


