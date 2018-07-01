# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MovieheavenPipeline(object):

    def open_spider(self,spider):
        print('___open-spider__')
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='movieHeave',
            charset='utf8'
        )
        #创建游标对象
        self.cursor = self.db.cursor()
        print('数据库链接成功')

    def close_spider(self,spider):
        print('___colse-spider___')
        #关闭数据库
        self.db.close()

    def process_item(self, item, spider):
        print('********************************')
        print(item['movie_name'])
        print(item['movie_url'])
        #return item
        self.cursor.execute('insert moviedl(name,url) values(%s,%s)',args=(item['movie_name'],item['movie_url']))
        self.db.commit()
        if self.cursor.rowcount >=1:
            print('数据保存成功')

