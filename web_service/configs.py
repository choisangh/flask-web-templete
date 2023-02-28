import os
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

class Config:
    """Flask config"""
    SECRET_KEY = 'test'
    SESSION_COOKIE_NAME = 'tomproject'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SWAGGER_UI_DOC_EXPANSION = 'list'


class DevelopmentConfig(Config):
    """Flask Config for dev"""
    DEBUG =True
    SEND_FILE_MAX_AGE_DEFAULT = 1
    WTF_CSRF_ENABLED = False


class TestingConfig(DevelopmentConfig):
    __test__ = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(BASE_PATH, "sqlite_test.db")}'


class ProductionConfig(DevelopmentConfig):
    pass
