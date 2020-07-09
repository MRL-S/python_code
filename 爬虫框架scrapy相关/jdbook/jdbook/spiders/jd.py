# -*- coding: utf-8 -*-
import scrapy
from copy import deepcopy
import json
import re


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['book.jd.com','list.jd.com','p.3.cn']
    start_urls = ['http://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath('//div[@class="mc"]/dl/dt')#大分类列表
        for dt in dt_list:
            item = {}
            item['b_cate'] = dt.xpath('./a/text()').extract_first()
            em_list = dt.xpath('./following-sibling::dd[1]/em')#小分类列表
            for em in em_list:
                item['s_cate'] = em.xpath('./a/text()').extract_first()
                item['s_href'] = em.xpath('./a/@href').extract_first()
               
                if item['s_href'] is not None:
                    item['s_href'] = 'https:'+item['s_href']
                    return scrapy.Request(
                        item['s_href'],
                        self.parse_book,
                        meta={'item':deepcopy(item)}
                    )
        
    def parse_book(self,response):
        item = response.meta['item']
        booklist = response.xpath('//div[@id="J_goodsList"]/ul/li')
        for book in booklist:
            item['img_url'] = book.xpath('.//div[@class="p-img"]/a/img/@src').extract_first()
            item['book_name'] = book.xpath('.//div[@class="p-name"]/a/em/text()').extract_first().strip()
            item['book_url'] = book.xpath('.//div[@class="p-name"]/a/@href').extract_first()
            if 'https:' not in item['book_url']:
                item['book_url'] = 'https:'+item['book_url']
            item['book_auth'] = book.xpath('.//span[@class="p-bi-name"]/a/text()').extract() if len(book.xpath('.//span[@class="p-bi-name"]/a/text()').extract())>0 else None
            item['book_pub'] = book.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first() if book.xpath('.//span[@class="p-bi-store"]/a/text()').extract_first() is not None else None
            item['book_time'] = book.xpath('.//span[@class="p-bi-date"]/a/text()').extract_first() if book.xpath('.//span[@class="p-bi-date"]/a/text()').extract_first() is not None else None
            item['skuid'] = book.xpath('.//div[@class="p-price"]/strong/@class').extract_first()
            yield scrapy.Request(
                "https://p.3.cn/prices/mgets?&skuIds={}".format(item['skuid']),
                self.parse_bookprice,
                meta={'item':deepcopy(item)}
            )
        current_page = int(re.findall(r"page: '(.*?)'",response.text)[0])
        print(current_page)
        all_page = 100
        if current_page <= (all_page-1*2+1):
            yield scrapy.Request(
                response.url+'&page={}&s={}&click=0'.format(current_page+2,(current_page-1)*26+1),
                self.parse_book,
                meta={'item':item}
            )
    def parse_bookprice(self,response):
        item = response.meta['item']
        item['book_price'] = json.loads(response.text)[0]['op']
        print(item)