# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from urllib import request

import pymysql
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from xinpianchang import settings


class XinpianchangPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='xpcItem',
            charset='utf8'
        )
        self.curcor=self.db.cursor()

    def __del__(self):
        self.db.close()


    def process_item(self, item, spider):

        self.curcor.execute('select * from xpc where name=%s',args=(item['video_name'],))
        if self.curcor.rowcount >=1:
            return
        try:
            self.curcor.execute('insert xpc(name,author,image_url,release_date,video_url) values(%s,%s,%s,%s,%s)',
                            args=(item['video_name'],item['video_author'],item['image_url'],item['release_date'],item['video_url']))
        except:
            self.db.rollback()
        else:
            self.db.commit()



        # url_name=item['video_name']+'.'+item['image_url'].split('.')[-1]
        # print(url_name)
        # request.urlretrieve(url=item['video_url'],filename=str(url_name))

        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('路径:',item['image_url'])
        yield scrapy.Request(url=item['image_url'],meta={'name':item['video_name']})

    def file_path(self, request, response=None, info=None):
        return request.meta['name']+'.'+request.url.split('.')[-1]
