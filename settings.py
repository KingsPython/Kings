

def getURL(DATEBASE):
    user = DATEBASE['USER']
    pwd = DATEBASE['PASSWORD']
    host = DATEBASE['HOST']
    port = DATEBASE['PORT']
    name = DATEBASE['NAME']

    # return 'mysql+pymysql://{}:{}@{}:{}/{}'.format(user, pwd, host, port, name)
    return 'sqlite:///sqlite3.db'  # 共享的数据只能用sqlite


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Develop(Config):
    DEBUG = True
    TESTING = True
    DATEBASE = {
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': "3306",
        'NAME': 'FlaskDay05'
    }
    SQLALCHEMY_DATABASE_URI = getURL(DATEBASE)
    SESSION_TYPE = 'redis'
    UPLOAD_FOLDER = 'app/static/media'
    SECRET_KEY = 'Yixiang'
    DEBUG = True


class Test(Config):
    TESTING = True
    DATEBASE = {
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': "3306",
        'NAME': 'FlaskDay05'
    }
    SQLALCHEMY_DATABASE_URI = getURL(DATEBASE)
    SESSION_TYPE = 'redis'
    UPLOAD_FOLDER = 'app/static/media'



class Stage(Config):
    DATEBASE = {
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': "3306",
        'NAME': 'FlaskDay05'
    }
    SQLALCHEMY_DATABASE_URI = getURL(DATEBASE)
    SESSION_TYPE = 'redis'
    UPLOAD_FOLDER = 'app/static/media'



class Product(Config):
    DATEBASE = {
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': "3306",
        'NAME': 'FlaskDay05'
    }
    SQLALCHEMY_DATABASE_URI = getURL(DATEBASE)
    SESSION_TYPE = 'redis'
    UPLOAD_FOLDER = 'app/static/media'



env = {
    'devlop': Develop,
    'test':Test,
    'stage': Stage,
    'product':Product,
}