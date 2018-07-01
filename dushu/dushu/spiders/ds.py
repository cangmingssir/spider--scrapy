# -*- coding: utf-8 -*-
import urllib

import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dushu.items import DushuItem

class DsSpider(CrawlSpider):
    name = 'ds'
    allowed_domains = ['www.dushu.com','img.dushu.com']
    start_urls = ['http://www.dushu.com/']

    #通过链接提取器，engine自动将所有的链接加入到队列中
    #follow为True时，当下载器下载的链接时，会自动提取本页的所有符合规则的链接，并加入下载队列中
    #当链接请求成功后，由callback的解析函数来处理
    rules = (
        Rule(LinkExtractor(allow=r'/book/\d+_?\d*?.html'), callback='parse_item', follow=True),

    )

    def parse_item(self, response:HtmlResponse):
        i = DushuItem()  #字典类型
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
            # iml = img.encode('gbk')
            # meta 可以实现在spider之间的数据传送
            # 主要实现request和response之间的数据共享
            # meta传参时，不要使用对象的引用，需要使用常量值
            yield scrapy.Request(url=str(i['img']),meta={'name':i['name']},callback=self.parse_img)
            #print(iml,name,book_url,author,summary)

            yield i

    def parse_img(self,response):
        print('____saveImg_____')
        # response.meta是读取request中的meta数据
        name = response.meta['name']
        print(name)
        print(response.url)


        #
        fileName = 'images/'+name+'.'+response.url.split(".")[-1]
        with open(fileName,'wb') as f:
            f.write(response.body)