# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QianchengwuyouPipeline(object):

    def open_spider(self,spider):
        self.file = open("qiancheng.json","w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii=False) +"\n"
        self.file.write(content)
        return item

    def clsoe_spider(self,spider):
        self.file.close()
