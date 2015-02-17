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



    # item_fields = {
    #     'title': './/span[@itemscope]/meta[@itemprop="name"]/@content',
    #     'link': './/a/@href',
    #     'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
    #     'original_price': './/a/div[@class="deal-prices"]/div[@class="deal-strikethrough-price"]/div[@class="strikethrough-wrapper"]/text()',
    #     'price': './/a/div[@class="deal-prices"]/div[@class="deal-price"]/text()',
    #     'end_date': './/span[@itemscope]/meta[@itemprop="availabilityEnds"]/@content'
    # }