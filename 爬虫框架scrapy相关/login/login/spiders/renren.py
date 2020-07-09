# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/SysHome.do']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={
                'email':'15298195937',
                'password':'10253uxtvop'
            },
            callback=self.parse_login
        )

    def parse_login(self,response):
        print(re.findall('刘思灏',response.body.decode()))