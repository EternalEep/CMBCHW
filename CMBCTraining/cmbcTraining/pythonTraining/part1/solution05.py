# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 格式化输出
def func(index, obj):
    print('{%d}, %s' % (index, obj))


# 字典 key唯一，不可变类型（列表、字典不能作为key）
def demoDiction():
    # 增删改查
    # 1、字典 (是一系列键值对),存储的是一个对象信息,使用key来查找
    dict0 = {'name': '民生', 'price': 5, "count": 2}
    func(0, type(dict0))
    # 查找 确保key存在dict中
    func(1, dict0['name'])
    func(2, dict0['price'])

    # get方法不改变字典本身
    name = dict0.get("name", -1)
    func(3, name)

    # setdefault方法，如果字典中不存在这个key，则首先将这个key和value加入字典
    name1 = dict0.setdefault("name", -1)
    func(4, name1)

    # 3、修改：字典是一种动态结构，可随时添加键值
    dict0['price'] = 0
    func(5, dict0)

    # 添加元素
    dict0['home'] = "中国"
    func(6, dict0)

    # 一次增加多个元素
    dict0.update({"addr": "北京", "tel": 123})
    func(7, dict0)

    # 删除元素，先判断后删除,避免出错
    if "count" in dict0:
        v = dict0.pop("count")
        func(8, v)

    # 也可以采用-1
    # v1 = dict0.pop("count", -1)
    v1 = dict0.pop("dd", -1)
    func(9, v1)
    func(10, dict0)

    del dict0['addr']
    func(11, dict0)

    # 清空字典
    dict0.clear()
    func(12, dict0)

    # 获取元素个数
    func(13, len(dict0))

    # in, not in 判断key是否在字典中
    func(14, "name" in dict0)

    # 判断一个值是否在字典中
    if 3 in dict0.values():
        print("3包含在字典dict0的值中")
    else:
        print("3不包含在字典dict0的值中")

    # ５、遍历字典,key,value 以及key-value
    """
    dict.keys()
    dict.values()
    dict.items()
    """

    # 6、打印字典
    dict1 = dict(a=1, b=2, c=3)
    func(15, dict1)

    # 遍历字典中键
    for i in dict1:
        func(16, (f"key={i}, value= {dict1[i]}"))

    for i in dict1.keys():
        func(17, (f"key={i}, value= {dict1[i]}"))
    # 遍历字典中值
    for i in dict1.values():
        func(18, i)

    # 遍历字典中所有的键值对
    for k, v in dict1.items():
        print(19, (f"key={k}, value={v}"))

    # 字典嵌套
    dict2 = dict(a=[1, 2, 3], b={"name": "老王", "age": 20})
    func(20, dict2)

    # 打印老王
    func(21, dict2["b"]["name"])

    # 打印2
    func(22, dict2["a"][1])

    # 8、集合 无序、互异
    # python中集合是通过函数set()来获取
    list1 = [1, 2, 1, 2, 3, 5, 9]
    set1 = set(list1)
    func(23, set1)


demoDiction()
