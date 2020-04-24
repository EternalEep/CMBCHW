# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 条件判断
def demoCondition():
    # 1、条件判断
    list1 = ['java', 'linux', 'ruby', 'c']
    for language in list1:
        if language == 'linux':
            func(1, language.upper())
        else:
            func(2, language.title())

    # 2、检查是否不相等
    request = 'add';
    if request != 'middle':
        func(3, "not equal !")

    # 3、检查多个条件 (and,or)
    # 4、检查特定值是否包含在列表中 (in, not in)
    cars = ['audi', 'bmw', 'sds', 'wed']
    if 'wed' not in cars:
        func(4, "false")
    else:
        func(5, "true")

    # 5、条件判断
    age = 10
    if age >= 20:
        func(6, "more")
    else:
        func(7, "no")

    # 6、省略else代码块
    age = 12
    if age < 4:
        func(8, "<4")
    elif age == 12:
        func(9, "=12")

    # 7、使用if语句处理列表
    mapps = ['one', 'two', 'three', 'four']
    for map in mapps:
        if map == "two":
            func(10, "this is two" + ".\n")
        else:
            func(11, "adding " + map + ".")


demoCondition()
