# -*- coding: utf-8 -*-
import scrapy
import re
from urllib.parse import urlencode
from copy import deepcopy
class SnbookSpider(scrapy.Spider):
    name = 'snbook'
    allowed_domains = ['suning.com']
    start_urls = ['https://list.suning.com/0-502297-0.html']
    

    def parse(self, response):
        """
        获取每个分类书籍的url
        """
        results = response.xpath('//dd/a/@href').extract()
        for url_base in results:
            url = 'https:'+url_base
            yield scrapy.Request(url,self.parse_book)
        yield scrapy.Request(response.url,self.parse_book)

    def parse_book(self,response):
        """
        解析静态网页的书籍信息
        """
        results = response.xpath('//li[contains(@class,"item-wrap")]')
        categroyid =  re.findall(r'"categoryId": "(.*?)",',response.text)[0]

        items = {}
        data_list = []
        for data in results:
            item = {}
            item['title'] = data.xpath('normalize-space(.//div[@class="title-selling-point"]/a/text())').extract_first()
            item['img_url'] = 'https:'+data.xpath('.//a[@class="sellPoint"]/img/@src').extract_first()
            item['evaluate_num'] = data.xpath('.//div[@class="info-evaluate"]/a/i/text()').extract_first()
            item['evaluate_url'] = 'https:'+data.xpath('.//div[@class="info-evaluate"]/a/@href').extract_first()
            item['store-stock'] = data.xpath('.//a[@class="store-name"]/text()').extract_first()
            item['store_url'] = 'https:'+data.xpath('.//a[@class="store-name"]/@href').extract_first()
            item['author'] = data.xpath('.//em[@class="book-author"]/text()').extract_first()
            item['publisher'] = data.xpath('.//em[@class="book-press"]/text()').extract_first()
            item['book-time'] = data.xpath('.//em[@class="book-time"]/text()').extract_first()
            data_list.append(item)
        classify = data.xpath('//dl/dt/a/text()').extract_first()
        items[classify] = data_list
        
        params = {
            'ci': categroyid,
            'pg': '03',
            'cp': '0',
            'il': '0',
            'iy': '0',
            'isNoResult': '0',
            'n': '1',
            'sesab': '', 
            'id': 'IDENTIFYING',
            'cc': '023',
            'paging': '',
            'sub': '0',
            'jzq': '100314'
        }
        url_base = 'https://list.suning.com/emall/searchV1Product.do?'
        for i in range(1,4):
            params['paging'] = i
            url = url_base+urlencode(params)
            yield scrapy.Request(url,callback=self.parse_ajaxbook,meta={"classify": classify,"items":deepcopy(items)})
    
    def parse_ajaxbook(self,response):
        classify = response.meta["classify"]
        items = response.meta["items"]
        results = response.xpath('//li[contains(@class,"item-wrap")]')
        data_list = items[classify]
        for data in results:
            item = {}
            item['title'] = data.xpath('normalize-space(.//div[@class="title-selling-point"]/a/text())').extract_first()
            item['img_url'] = 'https:'+data.xpath('.//a[@class="sellPoint"]/img/@src').extract_first()
            item['evaluate_num'] = data.xpath('.//div[@class="info-evaluate"]/a/i/text()').extract_first()
            item['evaluate_url'] = 'https:'+data.xpath('.//div[@class="info-evaluate"]/a/@href').extract_first()
            item['store-stock'] = data.xpath('.//a[@class="store-name"]/text()').extract_first()
            item['store_url'] = 'https:'+data.xpath('.//a[@class="store-name"]/@href').extract_first()
            item['author'] = data.xpath('.//em[@class="book-author"]/text()').extract_first()
            item['publisher'] = data.xpath('.//em[@class="book-press"]/text()').extract_first()
            item['book-time'] = data.xpath('.//em[@class="book-time"]/text()').extract_first()
            data_list.append(item)
        yield items
        