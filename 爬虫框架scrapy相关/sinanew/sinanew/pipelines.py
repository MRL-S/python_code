# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class SinanewPipeline:

    def process_item(self, item, spider):
        filename = item['sonTitle']+'.json'
        files = json.dumps(dict(item),ensure_ascii=False)
        with open(item['subFilename']+'/'+filename,'w',encoding='utf-8') as f:
            f.write(files)
        return item
