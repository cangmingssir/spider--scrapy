# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline  #可以通过mian入口运行程序
from scrapy.linkextractors import LinkExtractor
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule

#1.可以使用命令的方式生成Spider类
# scrapy genspider -t crawl dushu www.dushu.com
#2.修改spider类
#   将集成的CrawlSpider类改为RedisCrawlSpider
#   声明开始请求的入口网址存在redis的key：
#       redis_key='数据库的key的名字'
class DushuSpider(RedisCrawlSpider):
    name = 'dushu'
    allowed_domains = ['www.dushu.com']

    redis_key = 'dushu:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+_?\d*?.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {} #字典类型
        print('-----获取图书概要信息----')
        # print(response.url)
        # print(response.xpath('//title/text()'))

        #从当前的网页中获取图书的信息
        books = response.xpath('//div[@class="book-info"]')
        for book in books:
            i['name'] = book.xpath('./h3/a/text()').extract_first()  #提取第一个结果
            i['book_url'] =book.xpath('./h3/a/@href').extract_first()    #提取书的详情路径
            #print(type(book.xpath('./h3/a/@href').extract_first()))
            author = book.xpath('./p/a/text()').extract()  #提取作者
            i['author'] = ','.join(author)
            i['summary'] = book.xpath('./p[last()-1]/text()').extract_first()    #提起简介
            i['img'] = book.xpath('.//a/img/@data-original').extract_first()   #提取图片路径

            yield i


if __name__ == '__main__':
    # cmdline.execute('scr')
    pass