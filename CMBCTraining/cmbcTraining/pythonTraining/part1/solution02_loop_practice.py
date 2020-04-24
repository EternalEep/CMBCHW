# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
循环：
1、找到0～1000内最小的水仙花数
水仙花数：水仙花数是指一个 3 位数，它的每个位上的数字的 3次幂之和等于它本身

    1^3 + 5^3+ 3^3 = 153


2、100以内的所有质数
    质数：大于1，并且只能被1和自身整除

3、打印九九乘法表

"""
# # 默认是换行
# print("hello", "world", 18, sep="*")
# print("hello", "world", 18)
# # 使得结尾不换行
# print("hello,world",end="")
# print("hello,world",end="")

# print("hello", "world", end="*")
# print("hello", "world", end="")
# print("hello", "world", end="")

# 1、水仙花数
# for i in range(0, 1000):
#     a = i % 10
#     b = i // 10 % 10
#     c = i // 100 % 10
#     if a ** 3 + b ** 3 + c ** 3 == i:
#         print(f"{i} 是水仙花数")

# 2、质数
# l = []
# for i in range(2, 100):
#     # 判断质数
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         l.append(i)
# print(l)

# 3、乘法表
#
for i in range(1,10):
    for j in range(1,i+1):
        # print(f"{i}*{j} = {i*j}",end="   ")
        # print(f"{i}*{j} = {i*j:2d}",end="   ")
        print(f"{j}*{i} = {i*j:2d}",end="   ")
    #当i==2时，换行，依次同理
    print("")
