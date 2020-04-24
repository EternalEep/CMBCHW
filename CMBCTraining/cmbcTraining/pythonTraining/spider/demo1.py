# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1、使用requests获取整个网页的HTML信息
2、使用Beautiful Soup解析HTML信息，找到所有<img>
按照我们的设想，我们应该能找到很多<img>标签。
但是我们发现，除了一些<script>标签和一些看不懂的代码之外，
我们一无所获，一个<img>标签都没有！跟我们在网站审查元素的结果完全不一样，
这是为什么？
答案：这个网站的所有图片都是动态加载的！动态加载有一部分的目的就是为了反爬虫
动态网站使用动态加载常用的手段就是通过调用JavaScript来实现的
一个动态加载的网站可能使用很多JavaScript脚本，我们只要找到负责动态加载图片的JavaScript脚本
对于初学者，我们不必看懂JavaScript执行的内容是什么，做了哪些事情，因为我们有强大的抓包工具，
它自然会帮我们分析。这个强大的抓包工具就是Fiddler：
也可以使用浏览器自带的Networks，但是我更推荐这个软件，因为它操作起来更高效。
"""
import requests
if __name__ == '__main__':
    target = 'https://unsplash.com/'
    req  =requests.get(url=target)
    print(req.text)