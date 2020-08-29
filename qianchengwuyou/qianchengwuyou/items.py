# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengwuyouItem(scrapy.Item):
    #职位名称
    work_name = scrapy.Field()
    #公司名称
    company = scrapy.Field()
    #工作地点
    work_place = scrapy.Field()
    #薪资
    salary = scrapy.Field()
    #发布时间
    etc_time = scrapy.Field()
    #工作详情
    content = scrapy.Field()