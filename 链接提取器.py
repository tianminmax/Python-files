# coding: utf-8
import requests
from lxml import etree
url = input('请输入url:')
x = ''
#x = input('xpath语法:')
#/div/div/ul/li/div
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}


result = requests.get(url).content

dom = etree.HTML(result)
#wz_names = dom.xpath('//div/div/ul/li/div/a/text()')
wz_urls = dom.xpath('//a/@href')
#wz_wz = dom.xpath('//div/text()')
#print(wz_names)
for wz_url in wz_urls:
    if wz_url == 'javascript:;':
        pass
    elif wz_url == 'javascript:void(0);':
        pass
    elif wz_url == '#':
        pass
    else:
        print('"'+wz_url+'"')
'''
for wz_name,wz_url in zip(wz_names,wz_urls):
    print(wz_name,'   ',wz_url)'''