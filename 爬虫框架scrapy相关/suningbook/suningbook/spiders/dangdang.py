# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
import scrapy
from copy import deepcopy
import urllib


class DangdangSpider(RedisSpider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com']
    # start_urls = ['http://book.dangdang.com/']
    redis_key = "dangdang"

    def parse(self, response):
        div_list = response.xpath('//div[@class="con flq_body"]/div')
        for div in div_list:
            item = {}
            item['b_cate'] = div.xpath('./dl/dt//text()').extract()#大分类
            item['b_cate'] = [i.strip() for i in item['b_cate'] if len(i.strip())>0]
            dl_list = div.xpath('./div//dl[@class="inner_dl"]')
            for dl in dl_list:
                item['m_cate'] = dl.xpath('./dt//text()').extract()#中分类
                item['m_cate'] = [i.strip() for i in item['m_cate'] if len(i.strip())>0][0]
                a_list = dl.xpath('./dd/a')
                for a in a_list:
                    item['s_cate'] = a.xpath('./text()').extract_first()#小分类
                    item['s_href'] = a.xpath('./@href').extract_first()
                    if item['s_href'] is not None:
                        yield scrapy.Request(item['s_href'],self.parse_book,meta={'item':deepcopy(item)})

    def parse_book(self,response):
        item = response.meta['item']
        li_list = response.xpath('//ul[@class="bigimg"]/li')
        for li in li_list:
            item['bimg_url'] = li.xpath('./a/img/@src').extract_first()
            if item['bimg_url'] == 'images/model/guan/url_none.png':
                item['bimg_url'] = li.xpath('./a/img/@data-original').extract_first()
            item['book_title'] = li.xpath('./p[@class="name"]/a/text()').extract_first().strip()
            item['book_url'] = li.xpath('./p[@class="name"]/a/@href').extract_first()
            item['book_detail'] = li.xpath('./p[@class="detail"]/text()').extract_first()
            item['book_price'] = li.xpath('./p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            item['book_author'] = li.xpath('./p[@class="search_book_author"]/span[1]/a/text()').extract_first()
            item['book_time'] = li.xpath('./p[@class="search_book_author"]/span[2]/text()').extract_first()
            item['book_publisher'] = li.xpath('./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            yield item
        next_page = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page:
            yield scrapy.Request(urllib.parse.urljoin(response.url,next_page),self.parse_book,meta={'item':item})
