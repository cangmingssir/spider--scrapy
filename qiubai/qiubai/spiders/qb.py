# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse


class QbSpider(scrapy.Spider):
    #Spider名字，在命令行中，使用crawl命令，并指定qb的name名，开始爬取入口站点数据
    name = 'qb'

    #在请求站点资源时，资源只能是指定的域名下的资源
    allowed_domains = ['www.qiushibaike.com','www.baidu.com']   #这是一个集合，可添加多个

    #爬虫开始爬取资源的入口
    start_urls = ['https://www.qiushibaike.com']

    #当请求的资源成功时，回调parse函数，进行数据解析
    #parse如果有返回数据，则返回的是可迭代对象
    def parse(self, response:HtmlResponse):
        #response是响应对象，常用属性
        # print(response.encoding)    #不能修改
        # #字节码数据，返回的是字典类型，value为列表类型。例：{b'Server': [b'openresty'], b'Date': [b'Wed, 20 Jun 2018 01:59:00 GMT']}
        # print(response.headers)
        # print(response.status)
        # print(response.url)     #返回响应网址，与response.request.url相同
        # print(response.request.url)
        # print(response.body)    #字节码数据
        # print(response.text)    #文本数据
        # 可以直接发起xpath，查询网页中的title节点，xpath()返回的是Selector对象的列表集合
        # print(response.xpath('//div[@class="content"]/span/text()').extract_first())   #extract()提取selector对象的内容
        # t = response.xpath('//div[@class="content"]/span/text()').extract_first()
        # print(type(t))
        # p = response.xpath('//div[@class="content"]/span/text()').extract()
        # print(type(p))
        #print(response.css('div[class="author clearfix"] a'))

        articles = response.xpath('//div[starts-with(@class,"article")]')


        for article in articles:
            try:
                # article 是Selector对象类型
                name = article.xpath('./div[1]//img/@alt').extract()[0]
                img = article.xpath('./div[1]//img/@src').extract()[0]
                content = article.xpath('.//div[@class="content"]/span[1]/text()').extract()
            except:
                pass
            else:
                print(name, img)
                print(''.join(content).replace('\n', ''))



                #将item数据交给item管道处理
                yield {
                    "name":name,
                    "img":'http:'+img,
                    "content":''.join(content).replace('\n','')
                }
        #读取下一页数据
        next_url = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').extract()[0]
        next_page_url = response.urljoin(next_url)  #与start_url做拼接，https://www.qiushibaike.com/8hr/page/2/

        #发起下一页的请求,callback是回调函数
        yield scrapy.Request(next_page_url,callback=self.parse)
        print(next_url)

        #return QbSpider.start_urls[0]=r'https://www.qiushibaike.com'+next_url

