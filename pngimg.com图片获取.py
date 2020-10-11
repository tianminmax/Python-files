# coding: utf-8
#//li[@class="catalog"]//div[@class="category"]/a[@one-link-mark="yes"]
#//li[@class="catalog"]//div[@class="category"]/a[@one-link-mark="yes"]/@href
#//div[@class="png_png"]/a/@href
#//li//img/@src
import requests
from lxml import etree
import urllib.request
import os

url = 'http://pngimg.com'
ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
x = 0

result = requests.get('http://pngimg.com').text
dom = etree.HTML(result)
minzis = dom.xpath('//li[@class="catalog"]//div[@class="category"]/a[@one-link-mark="yes"]')
huoq_urls = dom.xpath('//li[@class="catalog"]//div[@class="category"]/a[@one-link-mark="yes"]/@href')
print(huoq_urls)
print(minzis)
for huoq_url,minzi in zip(huoq_urls,minzis):
	print(huoq_url)
	print(minzi)
	os.mkdir('E:\\图片\\'+minzi)
	nb2 = requests.get(huoq_url).text
	nb_2 = etree.HTML(nb2)
	nb2_urls = nb_2.xpath('//div[@class="png_png"]/a/@href')
	nb2_minzis = nb_2.xpath('//div[@class="png_png"]/a/@title')
	for nb2_url,nb2_minzi in zip(nb2_urls,nb2_minzis):
		x = 0
		nb3 = requests.get(nb2_url).text
		nb_3 = etree.HTML(nb3)
		os.mkdir('E:\\图片\\'+minzi+'\\'+nb2_minzi)
		nb3_tps = nb_3.xpath('//li//img/@src')
		for nb3_tp in nb3_tps:
			lj = requests.get(nb3_tp)
			with open('E:\\图片\\'+minzi+'\\'+nb2_minzi + '\\' + str(x) + '.jpg', 'wb') as file:
			    file.write(lj.content)
			print(nb3_tp)
			x = x+1




'''
lj = requests.get(huoqu)
with open('E:\\图片\\'+ t + '\\' + str(x) + '.jpg', 'wb') as file:
    file.write(lj.content)
'''