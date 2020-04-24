# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 控制流
def demoControlFlow():

    score = 66
    # score = 61

    # if/else
    if score % 2 == 0:
        func(0, "{0}这个数是偶数".format(score))
        if score % 3 == 0:
            func(0, "{0}这个数还能被3整除".format(score))
    else:
        func(0, "{0}这个数是奇数".format(score))

    # if/elif else 额外条件判断
    #特别注意：空字符串 ""、0、None、空对象，都当作False来处理
    if score > 80:
        func(1, "A")
    elif score > 60:
        func(2, "B")
    else:
        func(3, "C")

    # for循环,可遍历列表，字符串，元组、range
    for i in range(0, 4):
        func(4, i)

    # for循环
    messages = "hello"
    for message in messages:
        func(5, message)

    # continue 单次循环先结束掉
    for i in range(0, 4):
        if i == 2:
            continue
        func(6, i)

    # break 整个循环结束
    for i in range(0, 4):
        if i == 2:
            break
        func(7, i)

    # while 知道循环结束条件
    target = 6
    current = 1
    while current < target:
        current += 3
    func(8, current)


    #break while应用

    l = []
    i =''
    while True:
        i = input("请输入指令(q退出)：")
        if i =='q':
            break
        l.append(i)
    print(l)


    #pass 占位符

    for i in range(5):
        pass

demoControlFlow()
