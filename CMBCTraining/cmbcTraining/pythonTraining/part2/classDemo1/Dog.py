# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 类
#1、创建和使用类
"""python中首字母大些的名称指的是类"""

class Dog():
    """
    类中的函数称为方法
    __init__()作用是：初始化属性，使得每一个实例都有对应的基本属性
    包含三个形参：self必不可少，而且必须位于其他形参前面。
    python调用这个__init__（）方法来创建Dog实例时，将自动传入实参self，
    每个与类相关联的方法调用都自动传递实参self，他是一个指向实例本身的引用，
    让实例能够访问类中的属性和方法。
    """
    def __init__(self, name, age):
        """
        以self为前缀的变量都可供类中的所有方法使用，
        """
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " roll over!")


"""根据类创建实例"""
"""类：首字母大写；实例采用小写"""
my_dog = Dog('kitty', 3)
print("my dog's name is  " + my_dog.name.title() + ".")
print("my dog is  " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

