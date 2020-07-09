# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class CrawltestPipeline:
    def __init__(self):
        self.files = open('tianti.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        results = json.dumps(item,ensure_ascii=False,indent=2)+'\n'
        self.files.write(results)
        return item
    
    def close_spider(self,spider):
        self.files.close()