## CMBC HomeWork1
### [列表逆序](listreverse.py)
1. 函数反转: 采用list.reverse() 
1. 切片反转: 利用[::-1]切片反转
1. 迭代器反转: reversed()函数生成迭代器，类型转换为list
1. 列表生成式反转
```
[arrays[i] for i in range(len(arrays)-1,-1,-1)]
or
[arrays[~i] for i in range(0,len(arrays))]
```
##### 速度对比
```
函数反转:
10w time cnt | 17.312978 ms

切片反转:
10w time cnt | 22.041344 ms

迭代反转:
10w time cnt | 43.448182 ms

列表生成式反转:
10w time cnt | 77.202305 ms

while循环反转:
10w time cnt | 74.988291 ms
```
速度排名: 函数反转>切片反转>迭代反转>while循环反转>列表生成式反转
### [字符串压缩](compressString.py)
#### 错误案例分析(双指针法)
##### 错误案例1
```
ressult = []
for i in range(len(temp) - 1):
    j = i

    while (temp[j] == temp[j + 1]):
        j += 1

    i = i + j
    ressult.append(temp[i] + str(j))
```
1. $i$ 和 $j$ 的取值范围不匹配，$j + 1$存在越界问题
1. $i=i+j$ 溢出
1. for循环内部伴随$i = i + j$中$i$的修改，不符合规范，并且容易出现越界问题
##### 错误案例2
```
i = 0
while (i < len(temp) - 1):
    j = i  # 记住当前的index
    while (temp[j] == temp[j + 1]):
        j += 1  # 刷新相同char的 index
    ressult.append(temp[i] + str(j+1))
    i = i+j  # 更新到最新的index索引
```
1. while外循环需遍历所有char，而内循环需增加条件防止越界
1. 统计个数$j+1$逻辑错误
#### 错误案例修正(双指针法)
##### 修正双指针法
```
ressult = []
i = 0
while i < len(temp):
    j = i  # 记住当前的index
    while j < len(temp)-1 and temp[j] == temp[j + 1]: # 添加约束条件以防越界
        j += 1  # 刷新相同char的 index
    ressult.append(temp[i] + str(j-i+1))
    i = j+1 # 更新到最新的index索引
```
#### [字符串压缩实现](compressString.py)
1. While循环实现
1. For循环实现
1. 错误案例修正
##### 速度对比
```
while循环实现字符串压缩
1w time cnt | 45.090118 ms

for循环实现字符串压缩
1w time cnt | 21.305166 ms

课堂双指针法修正
1w time cnt | 44.473928 ms
```
while循环整体慢于for循环实现

### [字符串解压缩](uncompressString.py)
#### 异常声明
需要保证输入数据的合法性
1. 输入字符串为一个字母+一个数字的顺序组合
1. 输入字符串长度必须>2
#### [字符串解压缩实现](uncompressString.py)
1. While循环实现
1. For循环实现
##### 速度对比
```
while循环实现字符串解压缩
1w time cnt | 35.547416 ms

for循环实现字符串解压缩
1w time cnt | 25.564299 ms
```
while循环整体慢于for循环实现

### [python魔法方法](util.py)
1. \__str__ : 重写print()方法
1. \__len__ : 重写len()方法
1. \__setitem__ : 是设置array[key]=value时调用的方法，可自定义
1. \__getitem__: 是取array[key]时调用的方法，可自定义

