from sqlalchemy import Column, String, PickleType, Float, Text, Date, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from sport_bot.settings import *

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    engine = SQLALCHEMYPIPELINE_ENGINE

    engine = create_engine(engine)
    return engine


def create_teamspropability_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)

class Teams(DeclarativeBase):
    """Sqlalchemy TeamsPropability model"""
    __tablename__ = "teams"

    team_id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String, nullable=False)

class Sites(DeclarativeBase):
    """Sqlalchemy TeamsPropability model"""
    __tablename__ = "sites"

    team_id = Column(Integer, nullable=False, primary_key=True)
    propability = Column(String, nullable=True)
    site = Column(String, nullable=True)
