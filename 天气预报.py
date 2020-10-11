# coding: utf-8
import requests

from lxml import etree
#于都:http://www.weather.com.cn/weather/101240710.shtml
#赣州:http://www.weather.com.cn/weather/101240701.shtml

url = 'http://www.weather.com.cn/weather/'+input('请输入地区url:')+'.shtml'

#x = input('xpath语法:')

#/div/div/ul/li/div

ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
try:
    result = requests.get(url).content

    dom = etree.HTML(result)

    shij = dom.xpath('//div/div/div/ul/li/h1/text()')

    tianqi = dom.xpath('//div/div/div/ul/li/p[@title]/text()')

    zuixiaowendu_fongx = dom.xpath('//div/div/div/ul/li/p/i/text()')

    zuidawendu = dom.xpath('//div/div/div/ul/li/p/span/text()')

    diq = dom.xpath('//body/div/div/div/div/div/a/text()')

    jutidiq = dom.xpath('//body/div/div/div/div/div/span/text()')

    zuixiaowendu = []

    for i in range(0,len(zuixiaowendu_fongx),2):
        zuixiaowendu.append(zuixiaowendu_fongx[i])


    for sj,tq,zxwd,zdwd in zip(shij,tianqi,zuixiaowendu,zuidawendu):
        print('地点:'+diq[4]+diq[5]+jutidiq[3]+'  '+'时间:'+sj+'  '+'天气:'+tq+'  '+'温度:'+zxwd+'~'+zdwd+'℃')

except:
    print('\n没有这个地点!!!')
'''
wz_urls = dom.xpath('//div[@id="coolsites_wrapper"]/div/ul/li/div/a/@href')
#wz_wz = dom.xpath('//div/text()')

for wz_name,wz_url in zip(wz_names,wz_urls):
    print(wz_name,'  ',wz_url)
'''