temp = "ssssssssssrrrrrrrrrrrrttttttttt"  # input
print(temp.startswith("s"))
tempRes = "s10r12t9"  # output


ressult = []

# ctrl+shift +enter   case1 错误案例
# for i in range(len(temp)-1):
#     j=i
#     while(temp[j]==temp[j+1]):
#         j+=1
#
#     i=i+j
#     ressult.append(temp[i]+str[j])

i = 0
while (i < len(temp) - 1):
    j = i  # 记住当前的index
    while (temp[j] == temp[j + 1]):
        j += 1  # 刷新相同char的 index
    ressult.append(temp[i] + str(j+1))
    i = i+j  # 更新到最新的index索引

# 索引临界区 tring index out of range
# len(temp) - 1

# ressult.index(0,"success")
# ressult.append("success2")
#    ressult.__setitem__("test")
#TypeError:  expected 2 arguments, got 1
#
print(ressult)
