from sqlalchemy import create_engine, Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()
ENGINE = None
Session = None

class Courses(DeclarativeBase):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    organization = Column('organization', String)
    course_title = Column('course_title', String)
    authors = Column('author', String) 
    start_date = Column('start_date', Date)
    duration = Column('duration', String)
    course_notes = Column('course_notes', String)

class Authors(DeclarativeBase):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    author_name = Column('author_name', String)
    course_title = Column('course_title', String)

authors_courses = Table('authors_courses', DeclarativeBase.metadata, 
    Column('author_course_id', Integer, primary_key=True, nullable=False), 
    Column('authors_id', Integer, ForeignKey('authors.id'), nullable=False),
    Column('courses_id', Integer, ForeignKey('courses.id'), nullable=False)
     )

def connect(): 
    global ENGINE
    global Session
    ENGINE = create_engine('postgresql://penelopehill: @localhost:5432/db_coursera')
    Session = sessionmaker(bind=ENGINE)
    return Session()

db_session = connect()

def main():
    connect()
    DeclarativeBase.metadata.create_all(ENGINE)

if __name__ == "__main__":
    main()

