# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImageItem(scrapy.Item):
    # define the fields for your item here like:
    collection = table = 'image'
    img_id = scrapy.Field()
    title = scrapy.Field()
    img_url = scrapy.Field()
    pic_desc = scrapy.Field()
    thumb_url = scrapy.Field()
    
