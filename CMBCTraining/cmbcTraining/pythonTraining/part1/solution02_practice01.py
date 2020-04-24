# !/usr/bin/env python
# -*- coding:utf-8 -*-

# if练习
# 判断闰年（能被400整除或能被4整除但不能被100整除）


year = input("请输入一个有效年份：")
year = int(year)

#判断
if (year%400==0) or (year%4==0 and year%100 !=0):
    # print("{}是闰年".format(year))
    print(f"{year}是闰年")
else:
    # print("{}不是闰年".format(year))
    print(f"{year}不是闰年")
