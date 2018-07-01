# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule


class XhSpider(RedisCrawlSpider):
    name = 'xh'
    allowed_domains = ['www.meinv.hk']
#http://www.meinv.hk/?cat=2

    #设置redis存储爬虫起始的入口地址url的key
    redis_key = 'xh:start_urls'

    rules = (
        #restrict_xpaths='//div[@class="content-box"]'   r'http://www.meimv.hk/.p=\d{4}'
        Rule(LinkExtractor(restrict_xpaths='//div[@class="content-box"]/div[@class="posts-default-img"]'), callback='parse_item', follow=False),
    )

    def parse_item(self, response:HtmlResponse):
        #name_xpath='//h1[@class="title"]/text()'
        #img_xpath='//div[@class="post-image"]/img/@src'
        i = {'title':response.css('h1[class="title"]::text').extract_first(),
             'images':response.css('div[class="post-image"] img::attr(src)').extract(),
             'url':response.url}
        print('---获取的响应数据---')
        print(response.url)
        print(i)
        #print(response.body)
        yield i


if __name__ == '__main__':
    cmdline.execute('scrapy runspider xh.py -o aa.json'.split())