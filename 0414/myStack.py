class myStack(object):
    """模拟栈"""

    def __init__(this):
        this.items = []

    def is_empty(this):
        """判断是否为空"""
        return this.items == []

    def size(this):
        """返回栈的大小"""
        return len(this.items)

    def push(this, item):
        """压栈(加入元素)"""
        this.items.append(item)

    def pop(this):
        """弹栈(弹出元素)"""
        if len(this.items) > 0:
            return this.items.pop()  # 删除
        else:
            print("栈已经为空")
            return None

    def top(this):
        """返回栈顶元素"""
        if not this.is_empty():
            return this.items[len(this.items) - 1]
        else:
            return None


s = myStack()  # List<Integer> list = new ArrayList<Integer>()
print(s.is_empty())
print(s.size())
s.push(1)
s.push(2)
s.push(3)
print(s.size())
print("栈顶元素为：" + str(s.top()))
print("栈大小为：" + str(s.size()))
s.pop()
print("弹栈成功")
s.pop()
"""
栈顶元素为：4
栈大小为：1
弹栈成功
栈已经为空
"""
