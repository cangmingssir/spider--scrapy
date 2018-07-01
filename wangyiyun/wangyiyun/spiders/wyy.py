# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from scrapy_redis.spiders import RedisCrawlSpider


class WyySpider(RedisCrawlSpider):
    name = 'wyy'
    allowed_domains = ['music.163.com']
    # start_urls = ['http://https://music.163.com/']

    redis_key = 'wyy:start_urls'

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//ul[@class="f-cb"]/li//div[@class="left"]'), callback='parse_item', follow=True),
    )


    def parse_item(self, response):
        i = {}
        print(response.url)
        print(response.xpath('//tbody/tr/td[2]//span[@class="txt"]/a/@href').extract())
        alinks = response.xpath('//tbody/tr/td[2]//span[@class="txt"]/a/@href').extract()
        # for alink in alinks:
        #     i['name']=alink.xpath('./')
        #return i

if __name__ == '__main__':
    cmdline.execute('scrapy runspider wyy.py'.split())
