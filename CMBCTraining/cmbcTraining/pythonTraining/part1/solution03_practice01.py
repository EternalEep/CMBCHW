# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 列表推导式

l = [1, 2, 3, 4]
l1 = [i * 2 for i in l]
print(l1)

l2 = [i * 2 for i in range(10)]
print(l2)

l3 = [i for i in range(10) if i % 2 == 0]
print(l3)

l4 = [str(i) for i in range(10) if i % 2 == 0]
print(l4)

# 字符串遍历

l5 = [i for i in "hello"]
print(l5)

# 获取 ['boy','girl','people']中每个元素首字母，并组成一个新的字符串

l6 = ['boy', 'girl', 'you']
r1 = [i[0] for i in l6]
s = "".join(r1)
print(s)

# 找出两个列表中相同的元素
l7 = [2, 4, 6, 8, 10, 20]
l8 = [1, 2, 5, 6, 20, 100]

r2 = [i for i in l7 if i in l8]
print(r2)

#将列表中的元素打印到控制台
[print(i) for i in l8]