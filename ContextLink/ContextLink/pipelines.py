# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class ContextlinkPipeline:
	def __init__(self):
		self.con=pymongo.MongoClient('localhost',27017);
		db=self.con['scrap'];
		self.collection=db['scrap_tb'];
	def process_item(self, item, spider):
		self.collection.insert(dict(item))
		return item