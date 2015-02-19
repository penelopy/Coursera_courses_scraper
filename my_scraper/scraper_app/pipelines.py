#! -*- coding: utf-8 -*-

from sqlalchemy.orm import sessionmaker
from models import Courses, db_connect, create_courses_table


class CourseraPipeline(object):
    def __init__(self):
        """Initializes database connection and sessionmaker.

        Creates courses table.

        """
        engine = db_connect()
        create_courses_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """Save courses in the database.

        This method is called for every item pipeline component.

        """
        session = self.Session()
        course = Courses(**item)

        try:
            session.add(deal)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
