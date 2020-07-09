# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem

class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/']

    def start_requests(self):
        base_url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2020-5-1-1'
        for i in range(1,3):
            url = base_url.replace(base_url[-1],str(i))
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        data_list = response.xpath('//ul[contains(@class,"bang_list_mode")]/li')
        for data in data_list:
            item = DangdangItem()
            item['ranking'] = data.xpath('./div[contains(@class,"list_num")]/text()').extract_first()
            item["book_name"] = data.xpath('./div[@class="name"]/a/text()').extract_first()
            item["pic_url"] = data.xpath('./div[@class="pic"]/a/@href').extract_first()
            item["comment_num"] = data.xpath('./div[@class="star"]/a/text()').extract_first()
            item["publisher_time"] = data.xpath('./div[@class="publisher_info"][2]/span/text()').extract_first()
            item["publisher_name"] = data.xpath('./div[@class="publisher_info"][2]/a/text()').extract_first()
            item['price'] = data.xpath('./div[@class="price"]/p[1]/span[1]/text()').extract_first()
            yield item
