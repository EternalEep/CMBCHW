# !/usr/bin/env python
# -*- coding:utf-8 -*-


list1 = [1, 2, 3]


#
# def f(a):
#     a.append(4)  #a未重新赋值
#
#
# f(list1)  # a == list1
# print(list1)
#


def f(a):
    a = [6, 7, 8]  # 新列表
    a.append(4)


f(list1)
print(list1)
