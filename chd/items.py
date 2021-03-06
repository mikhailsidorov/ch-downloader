# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader


class ChDownloaderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Course(scrapy.Item):
    name = scrapy.Field()
    original_name = scrapy.Field()
    description = scrapy.Field()
    materials = scrapy.Field()
    duration = scrapy.Field()
    lessons_info = scrapy.Field()


class Lesson(scrapy.Item):
    name = scrapy.Field()
    filename = scrapy.Field()
    file_urls = scrapy.Field()
    duration = scrapy.Field()
