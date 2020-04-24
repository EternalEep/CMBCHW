# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Rect():
    def getPeri(self, a, b):
        return (a + b) * 2
    def getArea(self, a, b):
        return a * b

obj  = Rect()
print(obj.getPeri(3, 4))
print(obj.getArea(3, 4))
print(obj.__dict__)

"""
类中没有定义init()方法，也能够得到结果
1、通过print(obj.__dict__)查看属性的实例，发现是空的，原因：未定义init方法
2、实例化对象时，obj  = Rect()参数为空，只有在调用函数才使用，
"""