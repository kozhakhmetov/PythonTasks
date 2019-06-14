import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:@localhost/'
database_name = 'redditclone'


class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class ProductionConfig(Config):
    DEBUG = False
    # TODO: DONT forget


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
