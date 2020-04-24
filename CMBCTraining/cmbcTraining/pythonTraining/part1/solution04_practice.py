# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 提示用户输入5个数，组成一个列表

l = []
for i in range(5):
    num = input(f"请输入第{i + 1}个数: ")
    num = int(num)
    l.append(num)
print(f"输入的5个数是：{l}")

# 2、将该列表各个元素乘以2

for i in range(len(l)):
    l[i] *= 2
print(l)

# 3、计算新列表中所有元素和
sum = 0
for i in l:
    sum += i
print(sum)

# 4、找出100以内所有7的倍数以及包含7的数，放入一个列表中

list1 = []
for i in range(100):
    a = i % 10
    b = i // 10 % 10
    if i % 7 == 0 or (a==7 or b==7):
        list1.append(i)
print(f"满足条件的值有:{list1}")
