# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 变量的作用域（在程序的哪些地方可以使用变量）

i = 2


def f():
    i = 0  # 新变量
    # print(i)
    j = 0


f()
print(i)
