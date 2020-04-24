map = dict()
map[1] = 1
map[2] = 2
map[3] = 3

print(map)  # {1: 1, 2: 2, 3: 3} k:V

nums = [2, 3, 8, 10]
target = 5

list=[]  #  题目 twoSum  threeSum
hashTemp = {}
for i in range(len(nums)):
    if (target - nums[i]) in hashTemp:
        [hashTemp[target-nums[i]],i]
    else:
        hashTemp[nums[i]] = i
