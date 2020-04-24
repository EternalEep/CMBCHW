# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 可变参数
def f(a,*args):
    print(a)
    print(args)


f(1, 2, "you", 4, 5)
