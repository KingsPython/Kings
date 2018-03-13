from flask_cache import Cache
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
model = SQLAlchemy()
migrate = Migrate()
my_session = Session()
toolbar = DebugToolbarExtension()
cache= Cache(config={
    "CACHE_TYPE":'redis'
})
def init_ext(app):
    model.init_app(app=app)
    migrate.init_app(app=app, db=model)
    my_session.init_app(app=app)
    toolbar.init_app(app=app)
    cache.init_app(app=app)



