# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class QiubaiPipeline(object):
    #开始打开spider时，回调的函数
    def open_spider(self,spider):
        print('___open_spider___')
        #链接数据库
        self.db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='root',
            db='qiubaiscrapy',
            charset='utf8'
        )
        #创建游标对象
        self.cursor=self.db.cursor()
        print('--数据库连接成功--')

    #完成打开spider时，回调的函数
    def close_spider(self,spider):
        print('___close_spider___')
        #关闭数据库链接
        self.db.close()

    #item 管道在接收spider的parse返回的list时
    #由当前的item管道process_item处理
    def process_item(self, item, spider):
        print('--process item--')
        #print(item['name'],item['img'])
        #将数据写入到数据库中
        self.cursor.execute('insert content(name,img,content) values(%s,%s,%s)',args=(item['name'],item['img'],item['content']))
        self.db.commit()
        if self.cursor.rowcount >=1:
            print(item['name'],'数据写入成功')


