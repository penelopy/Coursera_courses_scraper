
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

import settings


DeclarativeBase = declarative_base()


def db_connect():
    """Performs database connection using database settings from settings.py.

    Returns sqlalchemy engine instance.

    """
    return create_engine(URL(**settings.DATABASE))


def create_deals_table(engine):
    """"""
    DeclarativeBase.metadata.create_all(engine)


class Courses(DeclarativeBase):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    organization = Column('organization', String)
    title = Column('title', String)
    author = Column('author', String)
    start_date = Column('start_date', String)
    duration = Column('duration', String)

#create authors table for many to one relationship with Courses