# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 创建二维列表
l = []
for i in range(3):
    item = []
    # 生成列表item
    for j in range(4):
        # print(f"i = {i},j = {j}")
        item.append(j)
    l.append(item)
print(l)

# 列表推导式
l1 = [[j for j in range(4)] for i in range(3)]
print(l1)

# 遍历列表
# for i in l:
#     # print(i)
#     for j in i:
#         print(j)

# 列表推导式遍历

[[print(j) for j in i] for i in l1]
