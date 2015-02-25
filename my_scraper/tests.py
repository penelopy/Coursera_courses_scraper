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

    def test_create_text_file_returns_correct_result(self):
        course_objects_list = []
        new_course = Course(
            'University of Maryland',
            'Developing Innovative Ideas for New Companies: The First Step in Entrepreneurship',
            'Dr. James V. Green',
            'Not Listed',
            'Not Listed',
            'Not Listed')

        course_objects_list.append(new_course)
        expected_result = 'University of Maryland\tDeveloping Innovative Ideas for New Companies: The First Step in Entrepreneurship\tDr. James V. Green\tNot Listed\tNot Listed\tNot Listed\n'

        result = coursera_spider.save_output_to_txt_file(course_objects_list)
        self.assertEqual(expected_result, result)
##########################
    def test_parse_data(self):

    # browser.get('file:///Users/penelopehill/Desktop/test1.html')

        course_objects_list = []
        new_course_1 = Course(
            'University of Maryland, College Park',
            'Developing Innovative Ideas for New Companies: The First Step in Entrepreneurship',
            'Dr. James V. Green',
            'Feb 23rd, 2015',
            '4 weeks long',
            'Not Listed')
        new_course_2 = Course(
            'University of California, San Diego',
            'Learning How to Learn: Powerful mental tools to help you master tough subjects',
            'Dr. Barbara Oakley, Dr. Terrence Sejnowski',
            'Not Listed',
            'Not Listed',
            'Go at your own pace.')
        course_objects_list.append(new_course_1)
        # course_objects_list.append(new_course_2)
        expected_result = course_objects_list
        print expected_result

        # self.assertEqual(expected_result, result)

        course_blocks = [r'<div class="c-courseList-entry-university"><a data-id="32" data-js="partner-link" href="/umd">University of Maryland, College Park</a>']
        result = coursera_spider.parse_data(course_blocks)

        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()