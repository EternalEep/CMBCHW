# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 导入urllib库的request模块
from urllib import request

# 请求URL
result = request.urlopen('http://www.baidu.com')
# 使用响应对象输出数据
print(result.read().decode("utf-8"))
