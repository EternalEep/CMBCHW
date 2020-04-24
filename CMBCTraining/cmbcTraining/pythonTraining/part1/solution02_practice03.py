# !/usr/bin/env python
# -*- coding:utf-8 -*-

# random练习
"""
Python中随机数
    石头、剪刀、布猜拳游戏
    玩家输入1，2，3表示 剪刀、石头、布
    程序随机选择 石头、剪刀、布与玩家比较

Python随机数方法
import random
#随机生成1到3之间的整数
number = random.randint(1, 3)
其中：number可能位1，2，3
"""

import random

# 1 -剪刀
# 2 -石头
# 3 - 布
number = random.randint(1, 3)
user_number = input("请选择一个数：")
user_number = int(user_number)
print(f"电脑出的是：{number}")

if number == user_number:
    print("平局")
else:
    if user_number > number and not (user_number == 3 and number == 1):
        print("你获胜了！")
    elif user_number == 1 and number == 3:
        print("你获胜了！")
    else:
        print("你失败了！")
