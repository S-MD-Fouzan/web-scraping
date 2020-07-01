# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ContextlinkItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url= scrapy.Field()
    text=scrapy.Field()
    pages=scrapy.Field()
    entities_nltk=scrapy.Field()
    nouns_from_site=scrapy.Field()
    precision_s=scrapy.Field()
    recall=scrapy.Field()
