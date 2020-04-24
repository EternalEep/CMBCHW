list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]

for i in list:
    list.remove(i)

for i in range(len(list)):  # 错误的实现
    list.remove(list[i])

# 迭代器遍历 实现删除  作业1
nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]  # 主元素问题  3   k:V
nums1 = [1, 1, 2, 2, 3, 3, 4, 4] # 1 2 3 4  作业2

# testMap = dict()
# testMap.__contains__()
# testMap.get(1)+1



# 作业2  出现 nums.length/4次 的值返回为 list 可以用字典解决

def majorityNumber(nums):
    key, count = None, 0
    for num in nums:
        if key is None:
            key, count = num, 1
        else:
            if key == num:
                count += 1
            else:  # 最关键的
                count -= 1
        if count == 0:
            key = None
    return key
    # key == num
