# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 函数的作用域

i = 2


def f():
    # 如果需要在函数内修改全局变量的值，需要使用global关键字
    global i
    i = 0
    # print(i)


f()
print(i)
