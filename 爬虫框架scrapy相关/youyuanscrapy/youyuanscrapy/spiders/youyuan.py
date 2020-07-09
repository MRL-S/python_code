# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from youyuanscrapy.items import YouyuanscrapyItem
import re

class YouyuanSpider(CrawlSpider):
    name = 'youyuan'
    allowed_domains = ['www.youyuan.com']
    start_urls = ['http://www.youyuan.com/find/chongqing/mm18-0/advance-0-0-0-0-0-0-0/p1/']

    #搜页面匹配规则
    list_page_lx = LinkExtractor(allow=(r"http://www.youyuan.com/find.+"))
    #重庆、18岁以上、女性的搜索页面匹配规则
    page_lx = LinkExtractor(allow=(r"http://www.youyuan.com/find/chongqing/mm18-25/advance-0-0-0-0-0-0-0/p\d+/"))
    #个人网页匹配规则
    profile_page_lx = LinkExtractor(allow=(r"http://www.youyuan.com/\d+-profile/"))
    rules = (
        Rule(list_page_lx,follow=True),
        Rule(page_lx,follow=True),
        Rule(profile_page_lx, callback='parse_profile_page', follow=False)
    )

    def parse_profile_page(self, response):
        item = YouyuanscrapyItem()
        item['header_url'] = self.get_header_url(response)
        item['username'] = self.get_username(response)
        item['monologue'] = self.get_monologue(response)
  
        item['age'] = self.get_age(response)
        item['source'] = 'youyuan'
        item['source_url'] = response.url
        yield item
        
    def get_header_url(self,response):
        """ 获取头像地址 """
        header_url = response.xpath('//dl[@class="personal_cen"]/dt/img/@src').extract()
        if len(header_url)>0:
            header_url = header_url[0].strip()
        else:
            header_url = ""
        return header_url
    def get_username(self,response):
        """ 获取用户名 """
        username = response.xpath('//dl[@class="personal_cen"]//div[@class="main"]/strong/text()').extract()
        if len(username) > 0:
            username = username[0]
        else:
            username = "该用户没有用户名"
        return username
    def get_age(self,response):
        """ 获取用户年龄 """
        age_url = response.xpath('//dl[@class="personal_cen"]/dd/p[@class="local"]').extract()
        if len(age_url)>0:
            age_word = age_url[0]
        else:
            age = 0
        age_key = re.findall('\s(\d*?)岁',age_word)
        if age_key:
            age = age_key[0]
        else:
            age = 0
        return age
    
    def get_monologue(self,response):
        """ 获取用户内心独白 """
        monologue_url = response.xpath('//div[@class="pre_data"]/ul[@class="requre"]/li[1]/p/text()').extract()
        if len(monologue_url)>0:
            monologue = monologue_url[0].strip()
        else:
            monologue = "给用户没有内心独白"
        return monologue
    
