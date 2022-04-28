class Config(object):
    TESTING = False
    DEFAULT_KEY = 'liuningjianshi'
    AUTH_TOKEN_ENCRYPT_KEY = 'liuningloveyou'
    SYNC_TOKEN_ENCRYPT_KEY = 'liuninglovyoueveryday'
    AUTH_TOKEN_EXPIRE_TIME = 1e6
    HOME_IMAGE_POEM_FETCH_TIME_GAP = 24 * 60 * 60
class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DATABASE_URI = "sqlite:////tmp/foo.db"

class TestingConfig(Config):
    MYSQL_LOCAL_HOST = '127.0.0.1'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123456'
    MYSQL_DB_NAME = 'jianshi'
    TESTING = True