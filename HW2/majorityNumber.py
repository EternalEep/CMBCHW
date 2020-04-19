# created by WeiwenYi on 2020/04/19
import math

# 作业2  出现次数大于nums.length/4次的值返回为list 可以用字典解决
def majorityNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return []
    n = math.floor(len(nums)/4)

    num_dict = {}

    res = []
    for num in nums:
        if num in res:
            continue
        if num in num_dict.keys():
            num_dict[num] += 1
        else:
            num_dict[num] = 1
        if num_dict[num] >= n:
            res.append(num)
    return res

if __name__=='__main__':
    nums = [1, 1, 2, 2, 3, 3, 4, 4]
    print(majorityNumber(nums))

