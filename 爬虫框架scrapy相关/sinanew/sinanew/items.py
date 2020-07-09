# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item,Field


class SinanewItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    parentTitle = Field()
    # parentUrls = Field()
    subTitle = Field()
    subFilename = Field()
    sonTitle = Field()
    sonUrl = Field()
    # title = Field()
    # content = Field()
