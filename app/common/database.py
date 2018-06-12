from ..models import db
from sqlalchemy_utils import drop_database


def init_db(app):
    """
    Create database if doesn't exist and
    create all tables.
    :param app:
    :return:
    """
    db.init_app(app)


def drop_db(app):
    """
    Drop all of the record from tables and the tables
    themselves.
    Drop the database as well.
    :param app:
    :return:
    """
    db.drop_all(app=app)
    drop_database(db.engine.url)
