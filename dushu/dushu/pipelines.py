# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib
import pymysql
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


class DushuPipeline(object):
    def process_item(self, item, spider):
        print('----item写入数据库的Pipeline----')
        #向数据库写入
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='dushuMsg',
            charset='utf8'
        )
        self.cursor = self.db.cursor()
        print(item['name'],item['author'],item['summary'],item['book_url'],item['img'])
        sql='select id from dushu where name=%s'
        self.cursor.execute(sql,args=(item['name'],))
        if self.cursor.rowcount >=1:
            return
        try:
            self.cursor.execute('insert dushu(name,author,summary,book_url,img) values(%s,%s,%s,%s,%s)',
                            args=(item['name'],item['author'],item['summary'],item['book_url'],item['img']))
        except:
            self.db.rollback()
        else:

            self.db.commit()
            print('数据写入成功')

        return item




# class ImagePipeline(object):
#     def process_item(self, item, spider):
#         #下载图片
#         print('----item保存图片的Pipeline----')
#         print(item['name'],item['img'])
#
#         # fileName = './images/'+item['name']+'.'+item['img'].split('.')[-1]
#         # urllib.request.urlretrieve(item['img'],fileName=fileName)
#
#         return item