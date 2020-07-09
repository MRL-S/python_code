# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import json
from juzi.items import JuziItem
from copy import deepcopy
class JzSpider(RedisSpider):
    name = 'jz'
    allowed_domains = ['www.itjuzi.com']
    redis_key = 'post_data'

    def make_request_from_data(self, data):
        data = json.loads(data)
        url = data['url']
        formdata = data['form_data']
        return scrapy.FormRequest(
            url=url,
            formdata=formdata,
            callback=self.parse
        )

    def parse(self, response):
        # print(response.text)

        data_list = json.loads(response.text)
        data_list = data_list['data']['data']
        for data in data_list:
            item = JuziItem()
            item['info_id'] = data['id']
            item['company_name'] = data['name']
            item['company_intro'] = data['des']
            item['found_time'] = data['agg_born_time']
            item['slogan'] = data['slogan']
            item['scope'] = data['scope']
            item['sub_scope'] = data['sub_scope']
            item['city'] = data['city']
            item['area'] = data['prov']
            item['home_page'] = 'https://www.itjuzi.com/company/'+str(data['id'])
            item['tags'] = data['tag']
            item['company_status'] = data['status']
            
            yield scrapy.Request(
                url='https://www.itjuzi.com/api/companies/{}?type=basic'.format(item['info_id']),
                callback=self.parse_company,
                meta={'item':deepcopy(item)}
            )
    def parse_company(self,response):
        item = response.meta['item']
        data_list = json.loads(response.text)
        data = data_list['data']['basic']
        item['company_size'] = data['company_scale']['com_scale_name']
        item['pdt_info'] = []
        product_list = data['com_organization']
        if len(product_list)>0:
            for product in product_list:
                pd = {}
                pd['com_name'] = product['com_name']
                pd['com_registered_name'] = product['com_registered_name']
                item['pdt_info'].append(pd)
        yield item
           


