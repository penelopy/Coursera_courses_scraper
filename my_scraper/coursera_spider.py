from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotVisibleException
import time
from items import Course
from datetime import datetime, date
import models
import codecs
# from sqlalchemy.orm import sessionmaker
import utilties


def scrape_data_from_coursera(): 
    # Locates "Load more courses" links and scrapes complete list of courses
    more_content = True

    browser = webdriver.Firefox()
    browser.get('https://www.coursera.org/courses?languages=en')

    time.sleep(10)

    while more_content:
        try:
            load_more = browser.find_element_by_xpath("//a[@href='#']")
            load_more.click()
            continue
        except ElementNotVisibleException:
            more_content = False

    elem = browser.find_element_by_xpath("//*")
    content = elem.get_attribute("innerHTML")
    soup = BeautifulSoup(content)  

    browser.quit()

    course_blocks = soup.find_all("div", "c-courseList-entry")
    return course_blocks

def parse_data(course_blocks):
    course_objects_list = []
    for course in course_blocks: 
        try:
            organization = course.find("div", "c-courseList-entry-university").find('a').get_text()
        except None:
            organization = None
        try: 
            title = course.find("div", "c-courseList-entry-title").find('a').get_text()
        except None: 
            title = None
        try: 
            start_dates = course.find("div", "bt3-col-xs-3 bt3-text-right").find_all('p')
        except:
            start_dates = None
        try: 
            authors = course.find("div", "c-courseList-entry-instructor").find_all('a')
        except AttributeError:
            author = None
        all_authors = ""
        if len(authors) > 1: 
            for author in authors: 
                author = author.get_text()
                #save each author individually to author database table
                new_author = models.Authors(author_name = author, course_title = title)
                models.db_session.add(new_author)
                models.db_session.commit()
                #save author to author string for text file
                all_authors += author + ", "
            all_authors = all_authors[:-2]

        elif len(authors) == 1:
            all_authors = authors[0].get_text()

        # process and parse date, duration and course note information
        for a_date in start_dates:
            a_date = str(a_date)
            duration = None
            course_begins = None
            course_notes = None
            if "Go at your own pace." in a_date: 
                course_notes = "Go at your own pace."
            elif "There are no open sessions." in a_date:
                course_notes = "There are no open sessions."
            else: 
                matches = utilties.parse_date_fields(a_date)
                course_begins, duration = utilties.clean_date_data(matches) #this will return course_begins and duration
            try: 
                organization = unicode(organization)
            except None: 
                organization = "Not listed"
            try: 
                title = unicode(title)
            except None: 
                title = "Not listed"
            try:
                duration = unicode(duration)
            except None: 
                duration = "Not listed"
            try: 
                course_notes = unicode(course_notes)
            except: 
                course_notes = "Not listed"
            try: 
                course_begins
            except None: 
                course_begins = None

            new_course = Course(organization, title, all_authors, course_begins, duration, course_notes)
            course_objects_list.append(new_course)

    return course_objects_list
 
def save_output_to_txt_file(course_objects_list):
    with codecs.open('complete_course_list.txt', 'w', encoding="utf-8") as f:

        for course in course_objects_list: 
            course_items = []
            course_items.append(course.organization)
            course_items.append(course.title)
            course_items.append(course.all_authors)
            start_date = str(course.start_date)
            course_items.append(start_date)
            course_items.append(course.duration)
            course_items.append(course.course_notes)
            f.write('%s' % ('\t'.join(course_items) + '\n'))
            #used in tests.py
            formatted_output = ('%s' % ('\t'.join(course_items) + '\n')) 
        return formatted_output

def upload_data_to_postgres(course_objects_list):
    for course in course_objects_list:

        newcourse = models.Courses(organization=course.organization, 
                        course_title=course.title,
                        authors=course.all_authors,
                        start_date=course.start_date,
                        duration=course.duration,
                        course_notes=course.course_notes)

        models.db_session.add(newcourse)
    models.db_session.commit()


def main():
    course_data = scrape_data_from_coursera()
    course_objects_list = parse_data(course_data)
    # save_output_to_txt_file(course_objects_list)
    # upload_data_to_postgres(course_objects_list)

if __name__ == "__main__": 
    main()

