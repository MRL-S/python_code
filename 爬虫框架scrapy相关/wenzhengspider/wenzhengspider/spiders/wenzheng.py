# -*- coding: utf-8 -*-
import scrapy
from wenzhengspider.items import WenzhengspiderItem
import urllib
import re
from scrapy.mail import MailSender

class WenzhengSpider(scrapy.Spider):
    name = 'wenzheng'
    allowed_domains = ['wz.sun0769.com']
    url = "http://wz.sun0769.com/political/index/politicsNewest?id=1&page="
    page = 1
    start_urls = [url+str(page)]

    def parse(self, response):
        li_list = response.xpath('//ul[@class="title-state-ul"]/li/span[@class="state3"]')
        for li in li_list:
            url = urllib.parse.urljoin(response.url,li.xpath('./a/@href').extract_first())
            yield scrapy.Request(url,self.parse_content)
        if self.page<=self.settings.get('MAX_PAGE'):
            self.page+=1
            yield scrapy.Request(self.url+str(self.page),self.parse)
    
    def parse_content(self,response):
        item = WenzhengspiderItem()
        item['number'] = response.xpath('//div[@class="mr-three"]/div[contains(@class,"focus-date")]/span[4]/text()').extract_first()
        item['title'] = response.xpath('//div[@class="mr-three"]/p[@class="focus-details"]/text()').extract_first()
        item['url'] = response.url
        item['state'] = response.xpath('//div[@class="mr-three"]/div[contains(@class,"focus-date")]/span[3]/text()').extract()
        item['state'] = ''.join([i.strip() for i in item['state'] if len(i.strip())>0])
        item['state'] = re.sub('\s','',item['state'])
        item['response_time'] = response.xpath('//div[@class="mr-three"]//div[@class="skillbar-title"]/span/text()').extract_first()
        item['ask_time'] = response.xpath('//div[@class="mr-three"]/div[contains(@class,"focus-date")]/span[2]/text()').extract_first()
        item['content'] = response.xpath('//div[@class="mr-three"]/div[@class="details-box"]/pre/text()').extract()
        item['content'] = ''.join(i.strip() for i in item['content'] if len(i.strip())>0)
        item['content'] = re.sub('\s','',item['content'])
        yield item
    def closed(self,reason):
        mailer = MailSender(
            smtphost='smtp.qq.com',
            mailfrom='243043853@qq.com',
            smtpuser='243043853@qq.com',
            smtppass='qxmthaxymygycaeh',
            smtpport=25
        )
        body = """
        这是爬取结果
        """
        subject = '爬虫'
        file = open('wenzheng.csv','rb')
        mailer.send(to=['243043853@qq.com','3611046@qq.com'],subject=subject,body=body,attachs=[('爬取数据','text/csv',file)],charset='utf-8')




