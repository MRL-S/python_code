# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field
import scrapy

class WenzhengspiderItem(scrapy.Item):
    # define the fields for your item here like:
    number = Field()
    state = Field()
    title = Field()
    response_time = Field()
    ask_time = Field()
    content = Field()
    url = Field()