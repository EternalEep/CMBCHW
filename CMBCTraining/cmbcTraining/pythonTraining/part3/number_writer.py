# !/usr/bin/env python
# -*- coding:utf-8 -*-

#10、存储数据

"""
    需要通过程序把用户提供的信息存储在列表和字典等数据结构中
    使用模块json来存储数据

    模块json让你能够将简单的python数据结构转存到文件中，并在
    程序再次运行时加载该文件中的数据
    还可以使用json在python程序之间分享数据。更重要的是json数据格式
    通用性高，可以同使用其他语言的分享。
"""

"""
    存储一组数字：（数字列表），使用函数json.dump()
    接收两个实参：要存储的数据以及可用于存储数据的文件对象。
    
    再将这些数字读取到内存中。使用json.load()
"""
"""导入模块json"""
import json
"""创建数字列表"""
numbers = [2,3,4,65,7,12,55]
filename = '/Users/sudo/Documents/test_data/numbers.json'
"""以写入模式打开这个文件，让json能够将数据写入到其中"""
with open(filename,'w') as f_obj:
    """使用函数json.dump()将数字列表存储到文件numbers.json中"""
    json.dump(numbers,f_obj)