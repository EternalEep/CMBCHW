# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 异常

"""
    异常使用try-except代码块处理。让python执行指定的操作，同时告诉
    python发生异常时候怎么办
"""
# 1、处理ZeroDivisionError异常
"""
    使用try-except代码块处理可能引发的异常
    如果try代码块中的代码运行没有问题，则python跳过except代码块；
    如果try代码块中的代码导致了错误，则python将查找这样的except代码块
    并运行其中的代码
    如果try-except代码块后面还有其他代码，程序将接着运行。
"""
while True:
    num1 = input("num1: ")
    num2 = input("num2: ")
    try:
        answer = int(num1) / int(num2)
    except ZeroDivisionError:
        print("you can't divide by 0 !")
    else:
        print(answer)
    break
