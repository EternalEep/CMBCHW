# !/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import datetime

# time模块

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


#生成timestamp
print(time.time())

print(time.strftime("%Y-%m-%d %X"))

print(time.ctime(time.time()))


# datetime
print(datetime.today())