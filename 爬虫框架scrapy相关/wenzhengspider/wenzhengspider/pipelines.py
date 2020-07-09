# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem
import scrapy
import csv
class WenzhengspiderPipeline:
    def __init__(self):
        self.file = open('wenzheng.csv','a',newline='',encoding='utf-8')
        head = ['number','title','url','state','response_time','ask_time','content']
        self.writer = csv.DictWriter(self.file,head)
        self.writer.writeheader()

    def process_item(self, item, spider):
        if item['number']:
            self.writer.writerow(item)
            return item
        else:
            return DropItem("Invalid data")
    def close_spider(self,spider):
        self.file.close()
