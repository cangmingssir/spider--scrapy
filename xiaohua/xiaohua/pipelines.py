# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import scrapy
from scrapy.pipelines.images import ImagesPipeline

from xiaohua import settings


class DBPipeline(object):
    def process_item(self, item, spider):
        print('hhhhhhhhhhhh',item)
        #item['images']='qqqqqqqqqqqqqqqqq'
        return item


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        #下载图片
        print('uuuuuuuuuuuuuuuuuuuuuu',item)
        for image_url in item['images']:
            yield scrapy.Request(url=image_url,meta={'name':item['title']})

    def item_completed(self, results, item, info):
        item['images'] = 'llllllllllllllllllll'
        return item


    def file_path(self, request, response=None, info=None):
        #获取存储的文件名
        dirpath = os.path.join(settings.IMAGES_STORE,request.meta['name'])
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)

        #相对与IMAGES_STORE的路径
        return request.meta['name']+"/"+request.url.split('/')[-1]

class moviesPipeline(object):
    def process_item(self,item,spider):
        print('papapapapapapapapapaapapapapapapapapap',item)
        item['images']='dddddddddddddddd'
        return item