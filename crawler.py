# -*- coding: UTF-8 -*-
import requests
from lxml import html
# url='https://www.hanjutv.com/top/tv/'
page=requests.Session().get(url)
tree=html.fromstring(page.text)
name=tree.xpath('//li[@class="item_list"]//span[1]//a/text()')
actor=tree.xpath('//li[@class="item_list"]//span[2]/text()')

file = open('korea.txt', 'w', encoding = 'utf8')
for i in range(len(name)):
    file.write(str(i+1) + '\n' + name[i] + actor[i] + "\n\n")

file.close()
