# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 练习
# 接收一个整数，1～99999，返回这个数的个十百千万位的数字
"""
例如： 输入12345
返回： 个位： 5
      十位： 4
      百位： 3
      千位： 2
      万位： 1
"""

num = input("请输入一个整数：")
num = int(num)

# 个位
a1 = num %10

# 十位 例如：123——》12——》2
b1 = num//10%10
# 百位 1234//100——》12 %10——》2

c1 = num//100%10

# 千位：
d1 =num//1000%10

# 万位12345
e1 = num//10000

print(f"{num}每位上的数分别是:个位：{a1},十位：{b1},百位：{c1},千位：{d1},万位:{e1}")