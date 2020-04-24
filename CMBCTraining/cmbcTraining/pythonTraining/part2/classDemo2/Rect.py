# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
在类中定义init()方法，方便创建实例的时候给实例绑上属性
即：定义完init方法后，创建的每个实例都有自己的属性，
也方便直接调用类中的函数
"""
class Rect():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        # 给属性指定默认值
        self.num = 10

    def getPeri(self):
        return (self.a + self.b) * 2
    def getArea(self):
        return self.a * self.b

    # 通过方法修改属性的值
    def update(self, count):
        self.num = count

    # 打印属性的值
    def read(self):
        print(self.num)

obj  = Rect(3, 4)

# 打印周长和面积
print(obj.getPeri())
print(obj.getArea())
print(obj.__dict__)

# 查看修改后的属性
obj.update(100)
obj.read()
print(obj.__dict__)