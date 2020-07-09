# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ZhihuuserItem(scrapy.Item):
    # define the fields for your item here like:
    id = Field()
    avatar_url = Field()
    head_line = Field()
    badge_v2 = Field()
    employments = Field()
    follower_count = Field()
    gender = Field()
    name = Field()
    types = Field()
    url = Field()
    url_token = Field()
    answer_count = Field()
    articles_count = Field()
    
    
