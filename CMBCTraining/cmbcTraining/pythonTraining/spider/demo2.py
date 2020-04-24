# !/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests


# 1、章节内容
if __name__ == '__main__':
    # target = 'http://gitbook.cn/'
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    req.encoding = 'GBK'
    # print(req.text)

    html = req.text
    bf = BeautifulSoup(html, 'html5lib')
    texts = bf.find_all('div', class_ = 'showtxt')
    # print(texts)
    """
    find_all匹配的返回的结果是一个列表。提取匹配结果后，使用text属性，提取文本内容，
    滤除br标签。随后使用replace方法，剔除空格，替换为回车进行分段。&nbsp;在html中是用来表示空格的。
    replace('\xa0'*8,'\n\n')就是去掉下图的八个空格符号，并用回车代替
    """
    print(texts[0].text.replace('\xa0'*8,'\n\n'))

    """要想下载正本小说，我们就要获取每个章节的链接
        目录： https://www.biqukan.com/1_1094/
        小说每章的链接放在了class属性为listmain的<div>标签下的<a>标签中。
        先匹配class属性为listmain的<div>标签，再匹配<a>标签
    """

