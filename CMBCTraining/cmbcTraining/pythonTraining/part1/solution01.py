# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 基础操作

# 1、运算符
def demoOperation():
    # 取余运算，对2取余，结果0或1，可判断奇偶
    func(0, 0 % 2)  # 求余
    func(0, 1 % 2)  # 求余
    func(0, 3 % 2)  # 求余
    func(0, 4 % 2)  # 求余
    func(0, 12 % 5)  # 求余
    func(1, 5 + 2)
    func(2, 5 - 2)
    func(3, 5 * 2)

    # 除法运算结果总是浮点数
    func(4, 5 / 2)
    func(4, 2 / 2)
    # 整数除法，自动舍去小数，保留整数
    func(4, 5 // 2)
    func(4, 5 // 2.0)
    # 整除应用：获取某一位上的数字
    print("54321的万位数是：" + str(54321 // 10000))
    # print((54321 // 10000))
    # print(54321%10) #个位
    # print((54321 // 1000)) #万位和千位
    func(5, 5 << 2)
    func(6, 5 >> 2)  # 右移两位，低位移除，高位补0
    func(7, 5 & 2)  # 相同为1，不同为0
    func(8, 5 | 2)  # 只要有一个为1，其值为1
    func(9, 5 ^ 2)  # 相同为0不同为1
    func(10, 5 == 2)
    func(10, 5 >= 2)
    func(10, 5 <= 2)
    func(10, 5 < 2)
    func(10, 5 != 2)

    # and or not
    """
    优先级：从上往下，优先级依次从高到低
    **
    * / % //
    + -
    > < >= <= == !=
    and or not
    =
    """
    # 关系运算 字符串比较
    # string 0 1 2 ... 9 < A B C ...Z <a b c ... z
    func(11, "Hello" > "Hi")

    # 指数运算
    """
        func(12, 5 ** 2)  # 两个乘号表示乘方运算

    """

    # 2、注释，单引号，双引号，#号 均可

    # 3、变量，就是存储数据的容器
    # 变量名只能为字母、数字，下划线，不能以数字开头
    # 可采用下划线，一般习惯上小写

    # 4、赋值 "="，变量使用前必须赋值，并且"=左边必须为变量"

    greet = "hello Python!"
    func(13, greet)

    a = 2
    a += 6  #a= a+6
    func(14, a)

    # 多个变量同时赋值（不建议）
    m, n, k = 1, 2, 3
    func(14, m + n + k)

    # 5、字符串（可以是单引号，双引号）
    name = "cmbc"
    func(15, name.title())  # 首字母大写
    func(16, name.upper())  # 转大写
    func(17, name.lower())  # 转小写

    # 字符串拼接
    part_one = "中国"
    part_two = "民生银行"
    part = part_one + part_two
    func(18, part)

    # 字符串只能拼接字符串类型
    func(19, ("你好" + str(1)))

    # 6、类型转换 字符串中使用整数时，需要将非字符串值转换为字符串
    age = 120
    message = "Happy " + str(age) + " Birthday!"
    func(20, message)

    """
    字符串使用 "+"和"*"运算符
    "+" 拼接
    "*" 重复字符串一定次数，产生新字符串
    """
    func(21, "hello" * 3)
    func(22, "hello" + "world")


demoOperation()
