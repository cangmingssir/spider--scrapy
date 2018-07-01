# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy as scrapy
from scrapy.http import HtmlResponse
from gushiwen import ydm_http

class GushiwenSpider(scrapy.Spider):
    name = 'gsw'
    allowed_domain=['www.gushiwen.org','so.gushiwen.org','www.baidu.com']

    def start_requests(self):
        #开始发布请求任务
        print('---Gushiwen 开始发起请求---')

        yield scrapy.Request(url='https://so.gushiwen.org/RandCode.ashx',callback=self.parse)


    def parse(self, response:HtmlResponse):
        with open('yanzhengma.gif','wb') as f:
            f.write(response.body)
        print('验证码下载成功')

        #获取图片内容
        yzmTxt = ydm_http.ydm('yanzhengma.gif')
        print(yzmTxt)

        login_url = 'https://so.gushiwen.org/user/login.aspx?'
        data={
            'email': '610039018@qq.com',
            'pwd': 'disen8888',
            'code': yzmTxt      # 验证码数据
        }
        #post提交数据
        yield scrapy.FormRequest(url=login_url,formdata=data,callback=self.parse_zw)


    def parse_zw(self,response:HtmlResponse):
        print(response.xpath('//title/text()').extract_first())

