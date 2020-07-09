# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy
import requests
from fake_useragent import UserAgent
ua = UserAgent(use_cache_server=False)
# 随机的User-Agent

class RandomUserAgent(object):
    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", ua.random)
        cookies = "_ga=GA1.2.918698155.1593670259; _gid=GA1.2.944243611.1593670259; Hm_lvt_1c587ad486cdb6b962e94fc2002edf89=1593670258,1593670712; juzi_user=857733; juzi_token=bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1OTM3MDA4MDQsImV4cCI6MTU5MzcwNDQwNCwibmJmIjoxNTkzNzAwODA0LCJqdGkiOiJNQjlTcGswMk1Qbk04QnZIIiwic3ViIjo4NTc3MzMsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiVXRQOVNwIn0.KUQjmVRYzrBOKqtklOMUJwbFk0_l7AdES_SXjFH8qCU; Hm_lpvt_1c587ad486cdb6b962e94fc2002edf89=1593700752; _gat_gtag_UA_59006131_1=1"
        cookies = {i.split('=')[0]:i.split('=')[1] for i in cookies.split('; ')}
        request.cookies = cookies
        authorization = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczpcL1wvd3d3Lml0anV6aS5jb21cL2FwaVwvYXV0aG9yaXphdGlvbnMiLCJpYXQiOjE1OTM3MDA4MDQsImV4cCI6MTU5MzcwNDQwNCwibmJmIjoxNTkzNzAwODA0LCJqdGkiOiJNQjlTcGswMk1Qbk04QnZIIiwic3ViIjo4NTc3MzMsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1dWlkIjoiVXRQOVNwIn0.KUQjmVRYzrBOKqtklOMUJwbFk0_l7AdES_SXjFH8qCU"
        request.headers['authorization'] = authorization

class ProxyMiddleWare(object):
    def process_request(self,request,spider):
        response = requests.get('http://127.0.0.1:5555/random')
        if response.text is not None:
            proxy = "https://"+response.text
            request.meta['proxy'] = proxy
