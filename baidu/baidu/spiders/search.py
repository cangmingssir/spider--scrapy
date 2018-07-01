# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy import cmdline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.linkextractors import LinkExtractor


class SearchSpider(scrapy.Spider):
    name = 'search'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def __init__(self):
        super(SearchSpider, self).__init__()

        #创建selenium的chrom浏览器对象
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('disable-gpu')

        self.brower = webdriver.Chrome(chrome_options=chrome_options)

    def parse(self, response):
        print('---parse---')
        print(response.url)
        #通过brower打开response.url
        #发起python关键的检索
        self.brower.get(response.url)
        self.brower.find_element_by_id('kw').send_keys('python')
        self.brower.find_element_by_id('su').click()
        time.sleep(5)
        self.brower.save_screenshot('baidu01.jpg')

        #获取搜索结果，再发起请求
        #基于链接提取器，获取查询结构链接
        extractor = LinkExtractor(r'http://www.baidu.com/link\?.*')
        #开始提取
        links = extractor.extract_links(self.brower.page_source)
        for link in links:
            print('title:',link.text)
            print('url:',link.url)
            yield {
                'title':link.text,
                'url':link.url
            }

    def __del__(self):
        #关闭brower浏览器
        self.brower.quit()


if __name__ == '__main__':
    cmdline.execute('scrapy crawl search'.split())
