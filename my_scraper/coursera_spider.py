from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import ElementNotVisibleException
import time
from items import Course
from datetime import datetime, date
import models
import codecs
import utilties

def scrape_data_from_coursera(url): 
    # Locates "Load more courses" links and scrapes complete list of courses once all courses are loaded
    more_content = True

    browser = webdriver.Firefox()
    browser.get(url)

    time.sleep(10)

    # while more_content:
    #     try:
    #         load_more = browser.find_element_by_xpath("//a[@href='#']")
    #         load_more.click()
    #         continue
    #     except ElementNotVisibleException:
            # more_content = False

    elem = browser.find_element_by_xpath("//*")
    content = elem.get_attribute("innerHTML")
    soup = BeautifulSoup(content)  

    browser.quit()

    course_blocks = soup.find_all("div", "c-courseList-entry")
    return course_blocks

def parse_data(course_blocks):
    # Extract data from BS4 instance and save to data structure
    # print "----------------"
    # print course_blocks
    # print "----------------"
    
    course_objects_list = []
    for course in course_blocks: 
        try:
            # print "----------------"
            # print course.find("div", "c-courseList-entry-university").find('a').get_text()
            # print "----------------"
            organization = unicode(course.find("div", "c-courseList-entry-university").find('a').get_text())
            # print organization
        except None:
            organization = "Not Listed"
        try: 
            title = unicode(course.find("div", "c-courseList-entry-title").find('a').get_text())
        except None: 
            title = "Not Listed"
        try: 
            start_dates = course.find("div", "bt3-col-xs-3 bt3-text-right").find_all('p')
        except:
            start_dates = None
        try: 
            authors = course.find("div", "c-courseList-entry-instructor").find_all('a')
        except AttributeError:
            author = None
         # Save each author to authors table in Postgres   
        all_authors = ""
        if len(authors) > 1: 
            for author in authors: 
                author = author.get_text()
                # Save each author individually to author database table
                new_author = models.Authors(author_name = author, course_title = title)
                models.db_session.add(new_author)
                models.db_session.commit()
                # Create text string of authors to include in text file
                all_authors += author + ", "
        elif len(authors) == 1:
            all_authors = authors[0].get_text()

        # Process and parse date, duration and course note information
        for start_date in start_dates:
            start_date = str(start_date)
            duration = None
            course_begins = None
            course_notes = None
            if "Go at your own pace." in start_date: 
                course_notes = "Go at your own pace."
            elif "There are no open sessions." in start_date:
                course_notes = "There are no open sessions."
            else: 
                matches = utilties.parse_date_fields(start_date)
                course_begins, duration = utilties.clean_date_data(matches) 
                duration = unicode(duration)
            try: 
                course_notes = unicode(course_notes)
            except: 
                course_notes = "Not listed"

            new_course = Course(organization, title, all_authors, course_begins, duration, course_notes)
            course_objects_list.append(new_course)
            print new_course.title
    return course_objects_list
 
def save_output_to_txt_file(course_objects_list):
    # Creates a tab separated file with data on all Coursera courses
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
    # Insert course data into Postgres
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
    url = 'https://www.coursera.org/courses?languages=en'
    course_data = scrape_data_from_coursera(url)
    course_objects_list = parse_data(course_data)
    # save_output_to_txt_file(course_objects_list)
    # upload_data_to_postgres(course_objects_list)

if __name__ == "__main__": 
    main()

