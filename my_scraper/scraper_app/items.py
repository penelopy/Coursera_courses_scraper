#! -*- coding: utf-8 -*-

from scrapy.item import Item, Field


class Course(Item):
    """Coursera course container (dictionary-like object) for scraped data"""
    organization = Field()   
    title = Field()
    author = Field()
    start_date = Field()
    duration = Field()

