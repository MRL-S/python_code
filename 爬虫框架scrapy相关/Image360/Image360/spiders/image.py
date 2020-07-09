# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
import json
from Image360.items import ImageItem
class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']
    start_urls = ['http://image.so.com/']

    def start_requests(self):
        base_url = 'https://image.so.com/zjl?'
        params = {
            'ch': 'photography',
            't1': 222,
            'sn': '',
            'listtype': 'new',
            'temp': 1
        }
        for page in range(1,self.settings.get('MAXPAGE')+1):
            params['sn'] = page*30
            url = base_url + urlencode(params)
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        result = json.loads(response.text)
        for data in result['list']:
            item = ImageItem()
            item['img_id'] = data['id']
            item['title'] = data['title']
            item['img_url'] = data['qhimg_url']
            item['pic_desc'] = data['pic_desc']
            item['thumb_url'] = data['qhimg_thumb']
            yield item
