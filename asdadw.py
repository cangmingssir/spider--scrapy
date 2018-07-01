# coding:utf-8
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


url = 'https://music.163.com/discover/toplist?id=19723756'

resp = request.urlopen(url)
if resp.status ==200:
    with open('yinyue.html','wb') as f:
        f.write(resp.read())
        print('ok')

