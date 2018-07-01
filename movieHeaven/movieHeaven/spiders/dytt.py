# -*- coding: utf-8 -*-
import os

import scrapy
from scrapy.http import HtmlResponse


class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response:HtmlResponse):
        # print(response.text)
        with open('movie.html','w') as f:
            f.write(response.text)
        movies = response.xpath('//div[@class="co_area2"]/div[@class="co_content8"]/ul/td/table[@class="tbspan"]')
        #print(movies)
        for movie in movies:
            try:
                movie_url_q = movie.xpath('./tr[2]/td[2]//a/@href').extract()[0]
                movie_name = movie.xpath('./tr[2]/td[2]//a/text()').extract()[0]
                print(movie_name,movie_url_q)
                movie_url = 'http://www.dytt8.net'+movie_url_q
                # movie_url=response.urljoin(movie_url_q)
                print(movie_url)
            except:
                pass
            else:
                yield scrapy.Request(movie_url,self.parse_video)

        next_url_q = response.xpath('//div[@class="x"]//a[last()-1]/@href').extract()[0]
        print(next_url_q)
        next_url = 'http://www.dytt8.net/html/gndy/dyzz/'+next_url_q

        yield scrapy.Request(next_url,self.parse)


    #解析详情的电影页面
    def parse_video(self,response:HtmlResponse):
        print('下载路径')
        # with open('movie_dl.html','w') as f:
        #     f.write(response.text)
        movie_dl_url = response.xpath('//div[@class="co_area2"]/div[@class="co_content8"]/ul//table/tbody//a/text()').extract()[0]
        #print(movie_dl_url)
        movie_name = response.xpath('//div[starts-with(@class,"title_all")]/h1/font/text()').extract_first()

        #下载movie
        #os.system('')

        yield {
            'movie_name':movie_name,
            'movie_url':movie_dl_url
        }

        yield scrapy.Request(movie_dl_url,self.saveMoive)

    def saveMoive(self,response):
        #保存视频
        print('保存视频')

