# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from qianchengwuyou.settings import USER_AGENTS as ua
import random
import redis
import hashlib
from scrapy.exceptions import IgnoreRequest

#给 每个请求随机分配一个 User-Agent
class QianchengwuyouSpiderMiddleware(object):
    def process_request(self,request,spider):
        uesr_agent = random.choice(ua)
        request.headers["User-Agent"] = uesr_agent

class QianchengqcMiddleware(object):

    def __init__(self):
        self.rs = redis.StrictRedis(host="localhost",port=6379,db=0)

    def process_request(self,request,spider):
        if request.url != "https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,1.html":
            url_md5 = hashlib.md5(request.url.encode()).hexdigest()
            result = self.rs.sadd("qc_url",url_md5)

            #如果redis 添加失败 返回False，则 忽略该 请求
            if result == False:
                raise IgnoreRequest

