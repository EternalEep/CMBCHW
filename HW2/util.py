testMap = {1:2,3:2}

#check if the value in the dict
print(testMap.__contains__(1))

# get(value, default_value)
print(testMap.get(1,0)+1)