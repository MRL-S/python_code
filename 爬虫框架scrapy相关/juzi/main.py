import redis
import json
from scrapy import cmdline
rd = redis.StrictRedis('127.0.0.1',port=6379,db=0)

def push_data_to_redis(data):
    """ 将post请求所需的data lpush到redis中 """
    rd.lpush('post_data',data)

if __name__ == "__main__":
    url = "https://www.itjuzi.com/api/companys"
    form_data = {
        'city': '',
        'com_fund_needs': "",
        'hot_city': "",
        'keyword': "",
        'location': "",
        'page': '0',
        'pagetotal': '171824',
        'per_page': '20',
        'prov': "",
        'round': '',
        'scope': "",
        'selected': "",
        'sort': "",
        'status': "",
        'sub_scope': "",
        'total': '0',
        'year': ''
    }
    data = {
        'url':url,
        'form_data':form_data
    }
    for i in range(1,10):
        form_data['page'] = str(i)
        push_data_to_redis(json.dumps(data))
    cmdline.execute('scrapy crawl jz'.split())