# -*- coding: utf-8 -*-
import scrapy
from qianchengwuyou.items import QianchengwuyouItem


class Q51Spider(scrapy.Spider):
    name = 'q51'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html?']

    def parse(self, response):
        node_list = response.xpath('//div[@id="resultList"]/div[@class="el"]')

        for node in node_list:
            item = QianchengwuyouItem()
            item["work_name"] = node.xpath('./p/span/a/@title').extract_first()
            item["company"] = node.xpath('./span[@class="t2"]/a/text()').extract_first()
            item["work_place"] = node.xpath('./span[@class="t3"]/text()').extract_first()
            item["salary"] = node.xpath('./span[@class="t4"]/text()').extract_first()
            item["etc_time"] = node.xpath('./span[@class="t5"]/text()').extract_first()

            content_link = node.xpath('./p/span/a/@href').extract_first()

            yield scrapy.Request(url = content_link,callback = self.detail,meta = {"item":item})

    def detail(self,response):
        item = response.meta["item"]
        print(item)

        item["content"] = "".join(response.xpath('//div[@class="bmsg job_msg inbox"]/p/text()').extract()).strip()
        print(item["content"])
        yield item


