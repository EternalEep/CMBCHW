# !/usr/bin/env python
# -*- coding:utf-8 -*-

# JSON

import json

"""
是一种轻量级的数据交换格式。JSON的数据格式其实就是python里面的字典格式
 Json   模块提供了四个方法： dumps、dump、loads、load 
 
 序列化 (Serialization)是将对象的状态信息转换为可以存储或传输的形式的过程
 通过从存储区中读取或反序列化对象的状态，重新创建该对象
    
 1. json序列化方法：

          dumps：无文件操作            dump：序列化+写入文件

  2. json反序列化方法：

          loads：无文件操作              load： 读文件+反序列化
"""

# print(json.dumps(1))

with open("/Users/sudo/Documents/test_data/test.json", "r", encoding='utf-8') as f:
    aa = json.loads(f.read())
    f.seek(0) #seek() 方法用于移动文件读取指针到指定位置,0代表从文件开头开始算起
    bb = json.load(f)    # 与 json.loads(f.read())
print(aa)
print(bb)

