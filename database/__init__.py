""" Database module

This module is used for database initialization of Flask
SQL Alchemy
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from conf import Config

__session_options = {}
__engine_options = {
    'isolation_level': 'READ COMMITTED',
    'pool_pre_ping': True
}

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, **__engine_options)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def get_session():
    return Session()

def remove_session():
    Session.remove()