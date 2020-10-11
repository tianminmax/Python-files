# coding: utf-8
import requests
from lxml import etree
import re
url = 'http://www.xbiquge.la/9/9419/'

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


result = requests.get(url).content

dom = etree.HTML(result)
#wz_names = dom.xpath('//dd/a/text()')
wz_urls = dom.xpath('//dd/a/@href')
#wz_wz = dom.xpath('//div/text()')

for wz_url in wz_urls:
    f = open('newtext.txt','a')
    wz_url = 'http://www.xbiquge.la' + wz_url
    f.write(wz_url+'\n')
    print(wz_url)