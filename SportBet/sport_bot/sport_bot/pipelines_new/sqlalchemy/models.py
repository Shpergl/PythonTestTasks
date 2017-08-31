from sqlalchemy import Column, String, PickleType, Float, Text, Date, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from sport_bot import settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    engine = settings.get('SQLALCHEMYPIPELINE_ENGINE')
    engine_echo = settings.get('SQLALCHEMYPIPELINE_ENGINE_ECHO')
    drop_all_tables = settings.get('SQLALCHEMYPIPELINE_DROP_ALL_TABLES')

    engine = create_engine(engine, echo=engine_echo)
    return engine


def create_teamspropability_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)



class TeamsPropability(DeclarativeBase):
    """Sqlalchemy TeamsPropability model"""
    __tablename__ = "TeamsPropability"

    id = Column(Integer, primary_key=True)
    team_name = Column('team_name', String)
    propability = Column('propability', String, nullable=True)
    link = Column('link', String, nullable=True)
    site_name = Column('site_name', String, nullable=True)
    date = Column('date', DateTime, nullable=True)