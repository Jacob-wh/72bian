import os


class Config(object):
    """Base config class."""

    # Flask app config
    DEBUG = True
    TESTING = False
    LOG_LEVEL = "DEBUG"
    LOG_DIR = "logs"

    # SQLAlchemy config
    PG_USER = ""
    PG_PASS = ""
    PG_HOST = "127.0.0.1"
    PG_PORT = "5432"
    PG_DB = ""
    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (PG_USER, PG_PASS, PG_HOST, PG_PORT, PG_DB)
