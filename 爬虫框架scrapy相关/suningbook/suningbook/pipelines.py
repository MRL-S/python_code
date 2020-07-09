# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SuningbookPipeline:
    def __init__(self):
        self.file = open('bookdangdang.json','a',encoding='utf-8')

    def process_item(self, item, spider):
        data = json.dumps(item,ensure_ascii=False,indent=2)
        self.file.write(data)
        return item

    def close_spider(self,spider):
        self.file.close()