# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json
from zhihuuser.items import ZhihuuserItem
class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://www.zhihu.com/']
    start_name = 'excited-vczh'
    user_url = 'https://www.zhihu.com/api/v4/members/{name}?include={include}'
    user_query = 'allow_message,is_followed,is_following,is_org,is_blocking,employments,answer_count,follower_count,articles_count,gender,badge[?(type=best_answerer)].topics'

    follows_url = 'https://www.zhihu.com/api/v4/members/{name}/followees?include={include}&offset={offset}&limit={limit}'
    follows_query = 'data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics'
    def start_requests(self):
        yield Request(self.user_url.format(name=self.start_name,include=self.user_query),self.parse_user)
        yield Request(self.follows_url.format(name=self.start_name,include=self.follows_query,offset=0,limit=20),self.parse_follows)

    def parse_user(self, response):
        results = json.loads(response.text)
        item = ZhihuuserItem()
        for field in item.fields:
            if field in results.keys():
                item[field] = results[field]
        yield item
        yield Request(self.follows_url.format(name=item['url_token'],include=self.follows_query,offset=0,limit=20),self.parse_follows)
    def parse_follows(self, response):
        results = json.loads(response.text)
        if 'data' in results.keys():
            for data in results['data']:
                yield Request(self.user_url.format(name=data['url_token'],include=self.user_query),self.parse_user)
        if 'paging' in results.keys() and results['paging']['is_end'] == False:
            yield Request(results['paing']['next'],self.parse_follows)
