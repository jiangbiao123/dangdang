# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings
class DangdangPipeline(object):

    def __init__(self):
        MONGO_DB = settings.get('MONGO_DB')
        MONGO_URL =settings.get('MONGO_URL')
        self.client = pymongo.MongoClient(MONGO_URL)
        db = self.client[MONGO_DB]
        self.post = db['dangdang3']

    def process_item(self, item, spider):
        self.post.insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()
