# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 列表嵌套

l = [30,31] * 5
l.pop(0)
l[1] = 28
l.insert(7,31)
l.extend([30,31])




print(l)
print(len(l))

month = input("请输入一个正数，1～12：")

month = int(month)
# print(month)
# print(l[month]-1)
print(f"{month} 月份有 {l[month]-1} 天")