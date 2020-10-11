# coding: utf-8
import requests
from lxml import etree
import re
shuru = int(input('下载1~几页面的视频：'))
url = 'https://maoyan.com/news?showTab=3&offset='
url_1 = 0


ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

for i in range(0,shuru*16,16):
    url_1 = i
    url = url + str(url_1)
    result = requests.get(url, headers=ua).text

    dom = etree.HTML(result)
    movie_names = dom.xpath('//h4[@class="video-name one-line"]/a/text()')
    movie_strs = dom.xpath('//h4[@class="video-name one-line"]/a/@href')

    for movie_name,movie_url in zip(movie_names,movie_strs):
        movie_id_string = requests.get(movie_url, headers=ua).text
        mp4_url = re.search('source src="(.*)" type',movie_id_string).group(1)
        print(mp4_url)
        mp4 = requests.get(mp4_url, headers=ua).content

        with open('F:\视频\%s.mp4'%movie_name,'wb') as file:
            file.write(mp4)