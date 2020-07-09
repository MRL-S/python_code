# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re 

class TiantiSpider(CrawlSpider):
    name = 'tianti'
    allowed_domains = ['itianti.sinaapp.com']
    start_urls = ['http://itianti.sinaapp.com']
    
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//ul[@class='list']/li/a"),callback='parse_item',follow=True),
        # Rule(LinkExtractor(allow=r'/index\.php/\w+'), callback='parse_item', follow=True)
    )
    
    def parse_item(self, response):
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        datas = []
        item = {}
        title = response.xpath('//h1[@class="title"]/text()').extract_first()
        heads = response.xpath('//thead/tr/th/text()').extract()
        if title == None:
            tit = '产品排行'
            num = re.findall(r'; array\((.*?)\)',response.text,re.S)[0]
            indexs = re.findall(r'\[.*?;(.*?)&.*?\]',response.text)
            contents = re.findall(r'string\(.*?\) .*?;(.*?)&.*?;',response.text,re.S)
            param = {}
            for index,content in zip(indexs,contents):
                
                if len(param) < int(num):
                    param[index] = content
                else:
                    
                    datas.append(param)
                    param = {}
                    param[index] = content
            else:
                datas.append(param)
            item[tit] = datas
        else:
            results = response.xpath('//tbody/tr')
            for result in results:
                cont = result.xpath('./td/text()').extract()
                data = {}
                for i,v in zip(heads,cont):
                    data[i] = v
                datas.append(data)
            item[title] = datas
        yield item
