from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotVisibleException
import time
from items import Course
import string
from datetime import datetime, date
import csv
import models
import codecs
from sqlalchemy.orm import sessionmaker


import unittest
from models import Courses #or import from item? 
import coursera_spider
 
 
class Tests_for_Coursera_project(unittest.TestCase):
 
    # def setUp(self):
    #     self.course = Courses()
    #     block = '<div class=\"c-courseList-entry-university\"><a data-js=\"course-link hut-link\" href=\"/course/innovativeideas\">Developing Innovative Ideas for New Companies: The First Step in Entrepreneurship</a></div>'
    #     blocks = []


# organization = course.find("div", "c-courseList-entry-university").find('a').get_text()

    # def test_parsing(self): 

        # course_objects_list = []
        # course_objects_list.append(new_course)

        # def __init__(self, organization, title, all_authors, start_date, duration, course_notes):

        # coursera.spider.save_output_to_txt_file(course_objects_list)
        # coursera_spider.parse_data("test")
        # print coursera_spider.parse_data(block)
 
    def test_create_text_file_returns_correct_result(self):
        course_objects_list = []
        new_course = Course('University of Maryland', 'Developing Innovative Ideas for New Companies: The First Step in Entrepreneurship', 'Dr. James V. Green', 'Not Listed', 'Not Listed', 'Not Listed')

        course_objects_list.append(new_course)
        myResult = 'University of Maryland\tDeveloping Innovative Ideas for New Companies: The First Step in Entrepreneurship\tDr. James V. Green\tNot Listed\tNot Listed\tNot Listed\n'

        result = coursera_spider.save_output_to_txt_file(course_objects_list)
        self.assertEqual(myResult, result)
 
    # def test_calculator_returns_error_message_if_both_args_not_numbers(self):
    #     self.assertRaises(ValueError, self.calc.add, 'two', 'three')

    # def main():
    #     test_calculator_add_method_returns_correct_result():


if __name__ == '__main__':
    unittest.main()