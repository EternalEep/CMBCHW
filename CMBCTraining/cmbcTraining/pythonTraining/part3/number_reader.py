# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""程序之间共享数据的一种方式"""

"""使用json.load()将列表读取到内存中"""

import json

"""读取的是前面写入的文件"""
filename = '/Users/sudo/Documents/test_data/numbers.json'
"""以读取方式打开这个文件"""
with open(filename, 'r') as f_obj:
    """加载存储在numbers.json中的信息，并存储到变量numbers中"""
    numbers = json.load(f_obj)

"""打印，看是否同number_writer.py中创建的数字列表相同"""
print(numbers)
