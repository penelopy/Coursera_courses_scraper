import lxml.html as lh
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://www.coursera.org/courses?languages=en')

time.sleep(10)

content = browser.page_source
browser.quit()

doc = lh.fromstring(content)


full_text = doc.xpath('//div[@class="c-courseList-listing"]/text()') #produces blank array
print "Full Text =", full_text

# course_block = doc.xpath('//div[@class="c-courseList-listing"]/div/div/h2/text()') #this worked
organization = doc.xpath('//div[@class="c-courseList-entry-university"]/a/text()') #this worked
title = doc.xpath('//div[@class="c-courseList-entry-title"]/a/text()') 
author = doc.xpath('//div[@class="c-courseList-entry-instructor"]/a/text()') 
# start_date = doc.xpath('//div[@class="bt3-col-xs-3 bt3-text-right"]/p/text()') 
# duration = doc.xpath('//div[@class="bt3-col-xs-3 bt3-text-right"]/p/br/text()') 


# print "********"
# for i in range(3): 
#     print organization[i]
#     print title[i]
#     print author[i]
#     # print start_date[i]
#     print "********"


print organization[0]
print title[0]
print author[0]
# print start_date[0]
# print duration[0]

