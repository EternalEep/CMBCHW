# !/usr/bin/env python
# -*- coding:utf-8 -*-

import turtle
import time

import tracer as tracer

turtle.pensize(2)
turtle.bgcolor("black")
colors = ["red", "yellow", "purple", "blue"]
tracer.start(False)

for x in range(400):
    turtle.forward(2 * x)  # 每次画的长度是变量x的2倍
    turtle.color(colors[x % 4])  # 改变颜色
    turtle.left(91)  # 逆时针旋转91度形成交叉螺旋
tracer.stop(True)
