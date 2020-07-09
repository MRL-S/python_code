# -*- coding: utf-8 -*-
import scrapy
from sinanew.items import SinanewItem
import os
class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['news.sina.com']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        content_list = response.xpath('//div[@id="XX_conts"]/div[@class="section"]')
        for content in content_list:
            item = SinanewItem()
            item['parentTitle'] = ''.join(content.xpath('./h2[@class="tit01"]//text()').extract())
            parentFilename = "./Data/"+item['parentTitle']
            if (not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)
            div_list = content.xpath('./div')
            for div in div_list:
                
                item['subTitle'] = div.xpath('./h3/a/text()').extract_first()
                if item['subTitle'] is None:
                    item['subTitle'] = div.xpath('./h3/span/text()').extract_first()
                subFilename = parentFilename+'/'+item['subTitle']
                item['subFilename'] = subFilename
                if (not os.path.exists(subFilename)):
                    os.makedirs(subFilename)
                
                li_list = div.xpath('./ul/li')
                for li in li_list:
                    item['sonTitle'] = li.xpath('./a/text()').extract_first()
                    item['sonUrl'] = li.xpath('./a/@href').extract_first()
                    yield item