## Created by WeiwenYi on 2020/04/13

from HW1.util import Timer
from timeit import timeit

class Solution(object):


    def __init__(self):
        pass

    # while loop
    def uncompressString_while(self, S):
        """
        :type S: str
        :rtype: str
        : Time complexity: O(n)
        : Space complexity: O(1)
        """

        if not S:
            return ""

        if len(S) < 2:
            raise  ValueError("S长度至少为2")

        i = 0
        res = ""

        while i < len(S):
            assert type(S[i]) == str # 异常检测，保证输入数据的合法性
            ch = S[i]
            i += 1
            assert S[i].isdigit() # 异常检测，保证输入数据的合法性
            tmp = ""
            while i < len(S) and S[i].isdigit():
                tmp += S[i]
                i += 1
            res += ch * int(tmp)

        return res

    # for loop
    def uncompressString_for(self, S):
        """
        :type S: str
        :rtype: str
        : Time complexity: O(n)
        : Space complexity: O(1)
        """

        if not S:
            return ""

        if len(S) < 2:
            raise  ValueError("S长度至少为2")

        res = ""
        tmp = ""
        prev_ch = S[0]

        int_flag = True # 异常检测，保证输入数据的合法性

        for ch in S[1:]:

            if int_flag:
                assert ch.isdigit()

            if not ch.isdigit():
                res += prev_ch * int(tmp)
                prev_ch = ch
                tmp = ""
                int_flag = True

            elif ch.isdigit():
                tmp += ch
                int_flag = False

        res += prev_ch * int(tmp)

        return res

if __name__ == "__main__":

    t = Solution()
    timer = Timer()

    funcs = [t.uncompressString_while, t.uncompressString_for]
    funcs_dict = {t.uncompressString_while: "while循环实现字符串解压缩",
                  t.uncompressString_for: "for循环实现字符串解压缩"}

    # 结果&速度测试(1w iters)
    for func in funcs:

        print(funcs_dict[func])

        print(func(""))
        print(func("s10r12t1"))
        print(func("s10r12t9"))

        # 1w次迭代速度统计
        num_str = "1w time cnt"
        print(num_str+' | '+timer.time_str_ms(timeit(lambda: func("s10r12t9"), number=10000))+'\n\n')

    # 异常检测
    # t.uncompressString_for('s')
    # t.uncompressString_for('s10r12ta')
