# created by WeiwenYi on 2020/04/19

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    res = []
    hashTemp = {}

    for i in range(len(nums)):
        if (target - nums[i]) in hashTemp.keys():
            res.extend([hashTemp[target - nums[i]], i])
        else:
            hashTemp[nums[i]] = i

    return res