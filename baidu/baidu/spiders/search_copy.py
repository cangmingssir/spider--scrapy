# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy import cmdline
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.linkextractors import LinkExtractor


class SearchSpider(scrapy.Spider):
    name = 'search_1'
    allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/']

    def __init__(self):
        super(SearchSpider, self).__init__()

        #创建selenium的chrom浏览器对象
        chrome_options=Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')

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
        links=self.brower.find_elements_by_xpath('//div[starts-with(@class,"result c-container")]/h3/a[1]')
        # links = self.brower.find_elements_by_css_selector('div[class="result c-container "] h3 a')

        for link in links:
            yield scrapy.Request(link.get_attribute('href'),callback=self.parse_target)

            yield {'title':link.text,
                   'url':link.get_attribute('href')}

    def parse_target(self,response):
        print('目标网站')
        #self.brower.get(response.url)
        return {
            'title':response.css('title::text').extract_first(),
            'url':response.url
        }


    def __del__(self):
        #关闭brower浏览器
        self.brower.quit()


if __name__ == '__main__':
    cmdline.execute('scrapy crawl search_1'.split())
