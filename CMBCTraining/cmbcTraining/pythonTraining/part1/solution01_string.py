# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))
    # print('{0}, {1}'.format(index, obj))


# 一、字符串下标
# 1、下标访问字符
word = "hello"

func(1, word[0])
func(2, word[1])
func(3, word[2])
func(4, word[3])
func(5, word[4])
# func(6, word[5])

# 负数下标：从后往前数
func(7, word[-1])
func(8, word[-2])

# 下标截取字符串,默认步长为1
func(9, word[1:3])

str1 = "01234567"
func(10, str1[2:7])
func(11, str1[2:7:2])

# 倒序字符串
func(12, str1[::-1])
# 获取字符串后三位字符
func(13, str1[-3:])

func(14, str1[:])

# 二、字符串方法

# 长度
func(15, len(word))

# 查找字串,有，返回index，否则-1
func(16, word.find("e"))
func(16, word.find("q"))

# 字串出现次数
func(17, word.count("l"))

# 是否包含 in, not in
func(18, 'lo' in word)
func(18, 'lo' not in word)

# 字符串替换
func(19, word.replace("l", "k"))

# 字符串分割
num = "1,2,3,4,5,6"
num1 = "123456"
func(20, num.split(","))
func(20, num1.split("23"))

# 转义字符
"""
\"  "
\\  \
\t  tab
\n  newline

字符串中转义字符失效,加r
r"D:\data"      raw未经处理的
"""
str2 = r"\n 表示换行"
func(21, str2)

# 换行字符串
html = """
<html>
    <head>
    </head>
    <body>
    </body> 
</html>
"""
func(22, html)

# 格式化字符串

age = 20
name = "book"
# 拼接方式
result = "年龄是:" + str(age) + "岁"
func(23, result)

# 方式1、F-String(Python3.6以上)
result1 = f"年龄是:{age}岁"
func(24, result1)

# 方式2、format()，{}作为占位符，format传入参数
result2 = "你好{},年龄是:{}岁".format(name, age)
# result2 = "你好{0},年龄是:{0}岁".format(name, age)
# result2 = "你好{0},年龄是:{1}岁".format(name, age)
func(25, result2)

# 方式3、% 根据变量类型来写
result3 = "你好%s,年龄是:%d岁" % (name, age)
func(26, result3)

# 格式化数字

# 小数点保留几位
pi = 3.141592
# result4 = f"{pi:.2f}"
result4 = "{:.2f}".format(pi)
result5 = f"{pi:%}"
result6 = f"{pi:.0%}"
func(27, result4)
func(28, result5)
func(29, result6)

print(type(result6))

# 进制转换
num2 = 20
func(30, f"{num2:#b}")
func(31, f"{num2:b}")
func(31, f"{num2:#o}") #八进制
func(32, f"{num2:#x}") #十六进制
