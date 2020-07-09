# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    ranking = scrapy.Field()
    book_name = scrapy.Field()
    pic_url = scrapy.Field()
    comment_num = scrapy.Field()
    publisher_name = scrapy.Field()
    author_name = scrapy.Field()
    price = scrapy.Field()
    publisher_time = scrapy.Field()
    
