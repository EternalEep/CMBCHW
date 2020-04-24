# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 常用标准库

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 0、引入模块

import sys
import pprint
import os




#sys模块

# 1、sys.argv 获取执行代码时，命令行中所包含的参数
# 该属性是一个列表，保存了当前命令的所有参数
# func(1, sys.argv)


# 2、获取当前程序中引入的所有模块，返回的是一个字典
# 字典key是模块名，值是模块对象
# func(2, sys.modules)

# 3、 print本身数据原样输出，如果需要格式化
# pprint模块提供了方法pprint()可对需打印的数据进行格式化
# pprint.pprint(sys.modules)

# 4、 sys.path 是一个列表，列表中保存的是模块的搜索路径（从前往后依次去找模块路径）

# pprint.pprint(sys.path)


# 5、 sys.platform 表示当前python运行的平台
# https://docs.python.org/3/library/sys.html#module-sys

func(3, sys.platform)

# 6、 sys.exit()函数用于退出程序
# sys.exit('程序异常，退出')
func(4, 'hello world !')



# os模块

#os.environ获取系统环境变量

# pprint.pprint(os.environ)
# pprint.pprint(os.environ["HOME"])

#getcwd() 获取当前工作目录
func(5, os.getcwd())

func(6, "获取指定文件夹中所有内容的名称列表")

#listdir() 获取指定文件夹中所有内容的名称列表
result = os.listdir('/')
pprint.pprint(result)




