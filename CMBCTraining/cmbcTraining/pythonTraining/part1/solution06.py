# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 函数
def demoFunction():
    # 1、函数 无参
    def greet_user():
        """显示简单的问候语"""
        func(1, "hello!")

    greet_user()

    # 2、 字符串 返回值
    def get_name(string1, string2):
        """字符串拼接"""
        name = string1 + string2
        return name

    result = get_name('中国', '民生银行信用卡中心')
    func(2, result)




demoFunction()
