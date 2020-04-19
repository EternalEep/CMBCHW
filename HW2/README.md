## CMBC HomeWork2
### [迭代删除](deleteItems.py)
list.remove() 用于移除列表中的某个值的第一个匹配项
#### 错误案例1
```python
list = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
for i in list:
    list.remove(i)
```
1. IndexError: list index out of range
1. 逻辑错误：列表元素删除后，list发生变化, 而for i in list按原始列表进行遍历，出现越界
#### 错误案例2
```python
for i in range(len(list)):  # 错误的实现
    list.remove(list[i])
```
1. IndexError: list index out of range
1. 逻辑错误：列表元素删除后，list变短，循环长度却没有减少，按照原来list的长度进行遍历，造成IndexError

### [多数元素](majorityNumber.py)
出现次数大于nums.length/4次的值返回为list, 可以用字典解决
### [两数之和](twoSum.py)
### [矩阵搜索](matrixSearch.py)
### [dict方法](util.py)
1. \__contains__(item): 检测dict里是否包含key的值为item，返回值为boolean
1. get(key,default_value): 从dict里获得key对应的value，如果没有该key则返回default_value

