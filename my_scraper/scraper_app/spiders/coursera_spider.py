# import lxml.html as lh
from selenium import webdriver
from bs4 import BeautifulSoup
import time
# import io
from items import Course

browser = webdriver.Firefox()
# browser.get('file:///Users/penelopehill/Desktop/test.html')
browser.get('https://www.coursera.org/courses?languages=en')

time.sleep(10)

elem = browser.find_element_by_xpath("//*")
content = elem.get_attribute("innerHTML")

# source_code = lh.fromstring(content)
soup = BeautifulSoup(content)

# print content
# print "test"

# content = browser.page_source
browser.quit()

course_blocks = soup.find_all("div", "c-courseList-entry")
# print course_blocks

new_titles = []

for course in course_blocks: 
    organization = course.find("div", "c-courseList-entry-university").find('a').get_text()
    title = course.find("div", "c-courseList-entry-title").find('a').get_text()
    authors = course.find("div", "c-courseList-entry-instructor").find_all('a')
    # print author
    author_list = []
    for author in authors: 
        author = author.get_text()
        author_list.append(author)
    print organization, "+", title, "+", author_list
    new_course = Course(organization, title, author)

    new_titles.append(new_course)  #FIXME save to DB
