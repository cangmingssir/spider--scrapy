# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class ZgwswSpider(RedisCrawlSpider):
    name = 'zgwsw'
    allowed_domains = ['wenshu.court.gov.cn']
    #start_urls = ['http://wenshu.court.gov.cn/']

    redis_key = 'zgwsw:start_urls'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//div[@id="pageNumber"]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        i = {}
        with open('zgwsw.html','wb') as f:
            f.write(response.body)

        print('下载成功')
        #return i



if __name__ == '__main__':
    cmdline.execute('scrapy runspider zgwsw.py'.strip())
