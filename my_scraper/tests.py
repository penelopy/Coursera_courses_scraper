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
import os
import unittest
from models import Courses #or import from item? 
import coursera_spider


class Tests_for_Coursera_project(unittest.TestCase):
    # Validates that the content of a dummy html file is correctly captured by Beautiful Soup.
    def test_scrape_data_from_coursera(self): 
        relative_test_file_path = 'test_data/test_course_blocks.html'
        absolute_file_path = os.path.abspath(relative_test_file_path)
        url = 'file:///' + absolute_file_path

        course_block = coursera_spider.scrape_data_from_coursera(url)
        result = unicode(course_block[0].find("div", "c-courseList-entry-university").find('a').get_text())
        expected_result = "University of Maryland, College Park"
        self.assertEqual(expected_result, result)

    # Validates that the scraped data is formatted correctly before being written to file
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

        output_filename = 'test_course_listing.txt'
        result = coursera_spider.save_output_to_txt_file(course_objects_list, output_filename)
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()