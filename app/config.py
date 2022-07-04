import os


class BaseConfig(object):
    TESTING = False
    SECRET_KEY = os.environ['SECRET_KEY']
    MONGODB_URI = os.environ['MONGODB_URI']
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    TESTING = True
    MONGODB_URI = 'mongomock://localhost'
    SERVER_NAME = 'testing.server.fake'

configs = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}