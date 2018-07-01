# -*- coding: utf-8 -*-
import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class XpcSpider(CrawlSpider):
    name = 'xpc'
    allowed_domains = ['www.xinpianchang.com']
    start_urls = ['http://www.xinpianchang.com/channel/index/id-0/sort-addtime/type-0']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.xinpianchang.com/channel/index/type-0/sort-addtime/duration_type-0/resolution_type-/page-.*?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response:HtmlResponse):
        i = {}
        #print(response.text)
        # with open('xpc.html','wb') as f:
        #     f.write(response.body)

        links = response.xpath('//ul[@class="video-list"]/li')
        for link in links:
            i['image_url']=link.xpath('./a/img/@_src').extract_first()
            i['video_name']=link.xpath('./div//a/p/text()').extract_first()
            i['video_author']=link.xpath('./div/div[@class="user-info"]/a/span[last()]/text()').extract_first().strip()
            i['release_date']=link.xpath('./a/div[@class="video-hover-con"]/p/text()').extract_first()
            i['url_next']='http://www.xinpianchang.com/a'+link.xpath('./@data-articleid').extract_first()+'?from='+link.xpath('./@data-videourl').extract_first()

            print(i['url_next'])

            yield scrapy.Request(url=i['url_next'],
                                 callback=self.parse_video,
                                 meta={
                                     'name':i['video_name'],
                                     'author':i['video_author'],
                                     'image_url':i['image_url'],
                                     'release_date':i['release_date']
                                 })
            print(i)
            #yield i
    def parse_video(self,response):
        i={}
        video_url='http:'+response.xpath('//a[@id="player"]/@href').extract_first()
        print('视频下载路径',video_url)
        i['video_name']=response.meta['name']
        i['video_author']=response.meta['author']
        i['image_url']=response.meta['image_url']
        i['release_date']=response.meta['release_date']
        i['video_url']=video_url

        yield i


if __name__ == '__main__':
    cmdline.execute('scrapy crawl xpc'.split())
