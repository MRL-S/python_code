# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy import Item,Field


class YouyuanscrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    header_url = Field()#个人头像链接
    username = Field()#用户名
    monologue = Field()#内心独白
    # pic_urls = Field()#相册图片链接
    age = Field()#年龄
    source = Field()
    source_url = Field()#个人主页源url
