# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 列表嵌套

stu1 = ["周瑜", 12]
stu2 = ["黄盖", 60]
stu3 = ["孙权", 9]

student = [stu1, stu2, stu3]

# print(student[0])
# print(student[0][0])
# print(student[0][1])
#
# print(f"{student[0][0]} 的分数：{student[0][1]}")
# print(f"{student[1][0]} 的分数：{student[1][1]}")

# index = 0
# index = 1
index = 2
print(f"{student[index][0]} 的分数：{student[index][1]}")
