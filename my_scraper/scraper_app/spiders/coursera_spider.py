from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

from scraper_app.items import Course

class CourseraSpider(BaseSpider):
    name = "coursera"
    allowed_domains = ["coursera.com"]
    start_urls = ["https://www.coursera.org/courses?languages=en"]

    course_list_xpath = ''

    item_fields = { 
        'organization':  '//div[@class="c-courseList-entry-university"/a/text()'
        'title': ''
        'author': ''
        'start_date': ''
        'duration': ''
    }


    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for course in selector.xpath(self.course_list_xpath):
            loader = XPathItemLoader(Course(), selector=course)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()
