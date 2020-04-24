# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 继承
class Person():
    def talk(self):
        print("person is listening...")

class Chinese(Person):
    def walk(self):
        print("child is walking...")

obj = Chinese()
obj.talk()
obj.walk()