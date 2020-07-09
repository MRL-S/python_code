# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import openpyxl
from scrapy.exceptions import DropItem
class DangdangPipeline:
    def __init__(self):
        self.wb = openpyxl.Workbook()
        self.sheet = self.wb.active
        self.sheet.title = "dangdangbook"
        self.sheet.append(['排名','书名','图片url','评论数','出版时间','出版社名','打折后的价格'])

    def process_item(self, item, spider):
        if item:
            self.sheet.append(list(dict(item).values()))
            return item
        else:
            return DropItem("missiong data")
    
    def close_spider(self,spider):
        self.wb.save("当当网2020年5月书籍排名.xlsx")
        self.wb.close()
