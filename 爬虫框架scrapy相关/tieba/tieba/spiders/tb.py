# -*- coding: utf-8 -*-
import scrapy
import urllib


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ["https://tieba.baidu.com/f?kw=%E9%87%8D%E5%BA%86%E8%80%8D%E6%9C%8B%E5%8F%8B&fr=home"]

    def parse(self, response):
        li_list = response.xpath('//li[contains(@class,"j_thread_list")]//div[contains(@class,"threadlist_lz")]')
        for li in li_list:
            item = {}
            item['title'] = li.xpath('.//a[@class="j_th_tit "]/text()').extract_first()
            item['author'] = li.xpath('.//a[contains(@class,"frs-author-name")]/text()').extract_first()
            item['author_url'] = urllib.parse.urljoin(response.url,li.xpath('.//a[contains(@class,"frs-author-name")]/@href').extract_first())
            item['content_url'] = li.xpath('.//a[@class="j_th_tit"]/@href').extract_first()
            item['img_url'] = []
            if item['content_url'] is not None:
                item['content_url'] = urllib.parse.urljoin(response.url,item['content_url'])
                yield scrapy.Request(
                    item['content_url'],
                    self.parse_content,
                    meta={'item':item}
                )
    
    def parse_content(self,response):
        """
        获取发帖的人内容
        """
        item = response.meta['item']
        img_list = response.xpath('//div[@class="j_d_post_content"]/img[@class="BDE_Image"]/@src').extract()
        item['img_url'].extend(img_list)
        print(item)
        yield item