# -*- coding: utf-8 -*-
import re

import scrapy

from Tencent.items import TencentItem
from urllib.parse import urlencode
import json

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query']

    def start_requests(self):
        data =  {
                'timestamp': '1592372256127',
                'countryId': '',
                'cityId': '',
                'bgIds': '',
                'productId': '',
                'categoryId': '',
                'parentCategoryId': '',
                'attrId': '',
                'keyword': '',
                'pageIndex': '',
                'pageSize': 10,
                'language': 'zh-cn',
                'area': 'cn'
            }
        base_url = "https://careers.tencent.com/tencentcareer/api/post/Query?"
        for page in range(1,3):
            data['pageIndex'] = page
            url = base_url+urlencode(data)
            yield scrapy.Request(url,self.parse)

    def parse(self,response):
        result = json.loads(response.text)
        # print(result.get('Posts'))
        for info in result.get('Data')['Posts']:
            item = TencentItem()
            item['RecruitPostName'] = info['RecruitPostName']#获取事业名
            item['Responsibility'] = info['Responsibility']#获取工作内容
            item['workLocation'] = info['CountryName']+'|'+info['LocationName']#获取工作地点
            item['LastUpdateTime'] = info['LastUpdateTime']#获取发布时间
            item['BGName'] = info['BGName']#获取事业名
            match = re.search(r'\d+',info['PostURL'])
            # print(item['PostURL'])
            # print(match.group(0))
            if len(match.group(0)) < 2:
                #判断url是否正确：’http://careers.tencent.com/jobdesc.html?postId=‘+PostId
                PostId = info['PostId']
                item['PostURL'] = info['PostURL'].replace(match.group(0),PostId)
            else:
                item['PostURL'] = info['PostURL']#获取发布url
            yield item
