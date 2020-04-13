## Created by WeiwenYi on 2020/04/13

from HW1.util import Timer
from timeit import timeit

# 函数反转
def func_reverse(arrays: list):
    arrays.reverse()
    return arrays

# 切片反转
def slice_reverse(arrays: list):
    return arrays[::-1]

# 迭代器反转
def iter_reverse(arrays: list):
    return list(reversed(arrays))

# 列表生成式反转
def list_reverse(arrays: list):
    # return [arrays[i] for i in range(len(arrays)-1,-1,-1)]
    # bit-wise
    return [arrays[~i] for i in range(0,len(arrays))]

def list_reverse_while(arrays: list):
    i = len(arrays)-1
    res = []
    while i >= 0:
        res.append(arrays[i])
        i-=1
    return res

if __name__ =='__main__':

    timer = Timer()

    funcs = [func_reverse, slice_reverse, iter_reverse, list_reverse, list_reverse_while]
    funcs_dict = {func_reverse: '函数反转', slice_reverse: '切片反转',
                  iter_reverse:'迭代反转', list_reverse: '列表生成式反转',list_reverse_while:"while循环反转"}

    # 结果&速度测试(10w iters)
    for func in funcs:
        arrays = ["python", "java", "c", "c++"]

        print(funcs_dict[func]+':')
        print(func(arrays))

        # 10w次迭代速度统计
        num_str = "10w time cnt"
        print(num_str+' | '+timer.time_str_ms(timeit(lambda: func(arrays), number = 100000))+'\n')




