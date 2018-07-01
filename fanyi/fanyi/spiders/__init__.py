# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import json

import scrapy as scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fy'
    allowed_domain=['fanyi.baidu.com']

    # start_urls = ['http://fanyi.baidu.com/']
    #
    #
    def parse(self,response):
        print('-----ok----')
        print(response.url)
        #print(response.body)

        jsonObj = json.loads(response.text)
        print(jsonObj)

    #spider 开始发起请求的函数
    def start_requests(self):
        print('开始发起请求')
        #get请求
        #yield scrapy.Request(url='http://fanyi.baidu.com/',callback=self.parse)

        url='http://fanyi.baidu.com/sug'
        data={
            'kw':'李世民'
        }
        yield scrapy.FormRequest(url=url,formdata=data,callback=self.parse)


        pdata={
        "from": "zh",
        "to": "en",
        "query": "李世民",
        "transtype": "translang",
        "simple_means_flag": 3,
        "sign": 966824.664473,
        "token": "2ad40757cffe7b37af44436ad14c1388"
        }

        #在FormRequest函数中可以设置url，formdata(上传的参数)，headers（请求头），callback(请求成功的回调)
        yield scrapy.FormRequest(url='http://fanyi.baidu.com/v2transapi',formdata=pdata,callback=self.parse)