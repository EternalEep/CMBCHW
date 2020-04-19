# created by WeiwenYi on 2020/04/19

# 迭代器遍历 实现删除  作业1
nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]  # 主元素问题  3   k:V

# 倒序删除
for i in range(len(nums)-1,-1,-1):
    nums.remove(nums[i])
print(nums) # []

#浅拷贝
from copy import copy
nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
for i in copy(nums):
    nums.remove(i)
print(nums) # []






