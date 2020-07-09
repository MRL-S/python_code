# -*- coding: utf-8 -*-
import scrapy
from myspider1.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # with open("teacher.html","w") as f:
        #     f.write(response.text)
        # items = []

        for each in response.xpath("//div[@class='li_txt']"):
            #将我们得到的数据封装到一个ItcastItem对象中
            item = ItcastItem()
            #extract（）方法返回的都是字符串
            name = each.xpath('./h3/text()').extract_first()
            title = each.xpath("./h4/text()").extract_first()
            info = each.xpath("./p/text()").extract_first()

            #xpath返回的是包含的个元素的列表
            item['name'] = name
            item['title'] = title
            item['info'] = info

            # items.append(item)
            yield item
        # return items

