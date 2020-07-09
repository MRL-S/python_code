# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from scrapy.exceptions import DropItem

class MysqlPipeline():
    def __init__(self,host,database,name,password,port):
        self.host = host
        self.database = database
        self.name = name
        self.password = password
        self.port = port
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            host = crawler.settings.get('MYSQL_HOST'),
            database = crawler.settings.get('MYSQL_DATABASE'),
            name = crawler.settings.get('MYSQL_NAME'),
            password = crawler.settings.get('MYSQL_PASSWORD'),
            port = crawler.settings.get('MYSQL_PORT')
        )
        
    def open_spider(self,spider):
        self.db = pymysql.connect(self.host,self.name,self.password,self.database,port=self.port,charset='utf8')
        self.cursor = self.db.cursor()

    def close_spider(self,spider):
        self.db.close()

    def process_item(self, item, spider):
        data = dict(item)
        keys = ','.join(data.keys())
        values = ','.join(['%s']*len(data))
        sql = 'insert into %s (%s) values (%s)'%(item.table,keys,values)
        try:
            self.cursor.execute(sql,tuple(data.values()))
            self.db.commit()
        except:
            self.db.rollback()
            print("erro")
        return item

class MongoPipeline():
    def __init__(self,mongo_uri,mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri = crawler.settings.get('MONGO_URI'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self,spider):
        self.client = pymongo.MongoClient(self.mongo_uri,port=27017)
        self.db = self.client[self.mongo_db]
    
    def close_spider(self,spider):
        self.client.close()
    
    def process_item(self,item,spider):
        data = dict(item)
        self.db[item.collection].insert_one(data)
        return item

class ImagePipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        url = request.url
        file_name = url.split('/')[-1]
        return file_name
    
    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok,x in results if ok]
        if not image_paths:
            raise DropItem("url can not download")
        return item
    
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['img_url'])