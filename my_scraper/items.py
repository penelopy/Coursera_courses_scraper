#! -*- coding: utf-8 -*-



class Course():
    def __init__(self, organization, title, all_authors, start_date, duration, course_notes):
        self.organization = organization
        self.title = title
        self.all_authors = all_authors
        self.start_date = start_date
        self.duration = duration
        self.course_notes = course_notes

