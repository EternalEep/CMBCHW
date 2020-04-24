# !/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests


# 2、章节名
if __name__ == '__main__':
    target = 'https://www.biqukan.com/1_1094/'
    req = requests.get(url = target)
    req.encoding = 'GBK'
    html = req.text
    div_bf = BeautifulSoup(html, 'html5lib')
    div = div_bf.find_all('div', class_ = 'listmain')
    print(div[0])

    """
    接下来再匹配每一个<a>标签，并提取章节名和章节文章
    使用Beautiful Soup匹配到了下面这个<a>标签，
    如何提取它的href属性和<a>标签里存放的章节名
    使用a.get('href')方法就能获取href的属性值，
    使用a.string就能获取章节名
    """
