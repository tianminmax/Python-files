# coding: utf-8
import requests
from lxml import etree
import re

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

f = open('newtext.txt','r')
for url in f:
    result = requests.get(url).content
    dom = etree.HTML(result)
    wz_wz = dom.xpath('//div/text()')
    for wz in wz_wz:
        wz.split('\xa0\xa0\xa0\xa0')
        print(wz)
        f = open('xs.txt', 'a',encoding='UTF-8')
        f.write(wz)