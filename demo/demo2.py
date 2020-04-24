temp = "s10r12t9"  # input
tempDummy = "ssssssssssrrrrrrrrrrrrttttttttt"  # output
str = "p"
# str()

#充分利用好API
#变量的转换

numstr = "1"
int(numstr)
strNum = str * 9  # 1
print(str.isdigit() == False)  # 2
print(strNum)
# && ||  python and or
i = 0  # index
tempList = []
while (i < len(temp) - 1):
    tempnum = ""
    countnum = 0
    if temp[i].isdigit() == False:
        tempstr = temp[i]
        while ((i + 1) <= (len(temp) - 1) and temp[i + 1].isdigit()):  # 错误的逻辑 如何修复  F9
            tempnum += temp[i + 1]  # 错误逻辑
            i = i + 1
        i = i + 1  # 注意变量的变化

        tempList.append(tempstr * int(tempnum))

        """ Return the number of items in a container. """
    #   ValueError: invalid
    #   literal
    #  for int() with base 10: ''

    # tempList.append(tempstr * int(tempnum))

print(tempList)
