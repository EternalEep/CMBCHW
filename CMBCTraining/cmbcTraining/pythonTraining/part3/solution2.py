# !/usr/bin/env python
# -*- coding:utf-8 -*-

def func(index, obj):
    print('{%d}, %s' % (index, obj))


"""
    1、先打开文件，才能访问它
    函数open()接收一个参数，要打开的文件的名称，返回一个表示文件的对象
    python将这个对象存储在后面将使用的变量中
    使用方法read()读取文件的全部内容，并将其作为一个长长的字符串存储在
    变量contents中。
    相比于原始文件，输出唯一不同时末尾多了一个空行，原因是：read()到达文件
    末尾时返回一个空字符串，显示出来就是一个空行
    要删除多出来的空行，可以print语句中使用rstrip():
"""
# 1、读取整个文件
file_path = '/Users/sudo/Documents/test_data/file.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    func(1, contents)
    func(2, contents.rstrip())

# 2、逐行读取
with open(file_path) as file_object:
    for line in file_object:
        func(3, line.rstrip())

"""
    注意：python读取文本文件时，将其中的所有文本都解读为字符串
    所以，如果读取为数字，需要使用int()转换为整数，float（）同理
"""
