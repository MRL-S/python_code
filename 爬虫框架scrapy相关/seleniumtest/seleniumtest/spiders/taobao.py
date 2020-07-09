# -*- coding: utf-8 -*-
import scrapy
import urllib
from seleniumtest.items import ProductItem

class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    base_urls = 'http://s.taobao.com/search?q='

    # login_state = False
    def start_requests(self):
        """ 构建request请求 """
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1,self.settings.get('MAX_PAGE')+1):
                url = self.base_urls+urllib.parse.quote(keyword)
                yield scrapy.Request(url,self.parse,meta={'page':page},dont_filter=True)
        
    def parse(self,response):
        # print(response.url)
        div_list = response.xpath('//div[@id="mainsrp-itemlist"]/div/div/div[1]/div')
  
        for div in div_list:
            item = ProductItem()
            item['title'] = div.xpath('.//div[contains(@class,"ctx-box")]//div[@class="title"]/a//text()').extract()
            item['title'] = ''.join([i.strip() for i in item['title'] if len(i.strip())>0])
            item['p_url'] = div.xpath('.//div[@class="pic-box-inner"]/div[@class="pic"]/a/@href').extract_first()
            item['img_url'] = "https:"+div.xpath('.//div[@class="pic-box-inner"]/div[@class="pic"]//img/@src').extract_first()
            item['price'] = ''.join(div.xpath('.//div[contains(@class,"ctx-box")]//div[@class="price"]//text()').extract())
            item['dealnumber'] = div.xpath('.//div[contains(@class,"ctx-box")]//div[@class="deal-cnt"]//text()').extract_first()
            item['location'] = div.xpath('.//div[@class="location"]/text()').extract_first()
            item['shop'] = div.xpath('.//div[@class="shop"]/a[contains(@class,"shopname")]/p[2]/text()').extract_first()
            print(item)