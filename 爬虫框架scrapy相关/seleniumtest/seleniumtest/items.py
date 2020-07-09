# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field
import scrapy

class ProductItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    p_url = Field()
    img_url = Field()
    price = Field()
    dealnumber = Field()
    location = Field()
    shop = Field()    
