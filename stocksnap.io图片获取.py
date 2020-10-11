# coding: utf-8
import requests
from lxml import etree
import urllib.request
import os

x = 0
url = 'https://stocksnap.io'

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

result = requests.get(url).text
dom = etree.HTML(result)
houqu_urls = dom.xpath('//a[@style]/@href')
ts = dom.xpath('//a[@style]/strong/text()')
for hq,t in zip(houqu_urls,ts):
    if hq == '#':
        pass
    try:
        os.mkdir('E:\\图片\\'+t)
    except:
        print('错误')
    hq_url = 'https://stocksnap.io'+hq
    print(hq_url)
    print(t)
    res = requests.get(hq_url).text
    dom1 = etree.HTML(res)
    houqus = dom1.xpath('//img/@src')#//a[@style]/@href
    for huoqu_url in houqus:
        huoqu = huoqu_url.replace('280h', '960w')
        try:
            if huoqu[1] == 's':
                pass
            else:
                lj = requests.get(huoqu)
                with open('E:\\图片\\'+ t + '\\' + str(x) + '.jpg', 'wb') as file:
                    file.write(lj.content)
                print(huoqu)
                x = x+1
        except:
            print('错误')
    x = 0
'''
lj = requests.get(huoqu)
with open('E:\\图片\\%s'%huoqu, 'wb') as file:
    file.write(lj.content)
    downPath = 'E:\\图片\\' + huoqu
    urllib.request.urlretrieve(huoqu, downPath)
'''