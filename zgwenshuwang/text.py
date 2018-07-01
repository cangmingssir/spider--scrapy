# coding:utf-8
from lxml import etree

import requests
from scrapy import cmdline
from selenium import webdriver
url='http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6'

headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}

brower=webdriver.Chrome()
def run():
    brower.get(url)
    n=1
    while True:
        #print(brower.page_source)
        xpath_html(brower.page_source)
        with open('zgwsw'+str(n)+'.html','w') as f:
            f.write(brower.page_source)
        n+=1

        brower.find_element_by_class_name('next').click()
        if n==200:
            break
# r = requests.get(url,headers=headers)
# print(r.text)

def xpath_html(html):
    req = etree.HTML(html)
    texts=req.xpath('//div[@id="resultList"]/div[@class="dataItem"]')
    print(texts)
    for text in texts:
        a = text.xpath('./table/tbody/tr[1]//a[last()]/text()')
        print(a)

if __name__ == '__main__':
    run()