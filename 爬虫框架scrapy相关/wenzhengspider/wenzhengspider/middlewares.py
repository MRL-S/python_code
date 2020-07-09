# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html


from logging import getLogger
import scrapy

class WenzhengspiderSpiderMiddleware:

    def __init__(self):
        self.logger = getLogger(__name__)
    def process_request(self,request,spider):
        request.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.56"
    
    def process_response(self,request,response,spider):
        
        if response.xpath('//div[@class="mr-three"]/div[contains(@class,"focus-date")]/span[4]/text()').extract_first() is None:
            self.logger.debug('No data save')
        return response