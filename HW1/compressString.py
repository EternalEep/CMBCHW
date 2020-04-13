## Created by WeiwenYi on 2020/04/13

from HW1.util import Timer
from timeit import timeit

class Solution(object):


    def __init__(self):
        pass

    # while loop
    def compressString_while(self, S):
        """
        :type S: str
        :rtype: str
        : Time complexity: O(n)
        : Space complexity: O(1)
        """
        if not S:
            return ""
        i = 0
        res = ""
        while i < len(S):
            cnt = 1
            res += S[i]
            while i < len(S)-1 and S[i+1]==S[i]:
                i += 1
                cnt += 1
            res += str(cnt)
            if len(res) >= len(S):
                break
            i+=1

        #压缩原理
        if len(res) < len(S):
            return res
        else:
            return S

    # for loop
    def compressString_for(self, S):
        """
        :type S: str
        :rtype: str
        : Time complexity: O(n)
        : Space complexity: O(1)
        """
        if not S:
            return ""
        prev_ch = S[0]
        cnt = 0
        res = prev_ch
        for ch in S:
            if ch==prev_ch:
                cnt += 1
                continue
            else:
                res += str(cnt)
                res += ch
                prev_ch = ch
                cnt = 1
        res += str(cnt)

        return res if len(res)<len(S) else S

    def modify_compressString(self, temp):
        ressult = []
        i = 0
        while i < len(temp):
            j = i  # 记住当前的index
            while j < len(temp)-1 and temp[j] == temp[j + 1]: # 添加约束条件以防越界
                j += 1  # 刷新相同char的 index
            ressult.append(temp[i] + str(j-i+1))
            i = j+1 # 更新到最新的index索引

        return ''.join(ressult)


if __name__ == "__main__":

    t = Solution()
    timer = Timer()

    funcs = [t.compressString_while, t.compressString_for, t.modify_compressString]
    funcs_dict = {t.compressString_while: "while循环实现字符串压缩",
                  t.compressString_for: "for循环实现字符串压缩",
                  t.modify_compressString: "课堂双指针法修正"}

    # 结果&速度测试(1w iters)
    for func in funcs:

        print(funcs_dict[func])

        print(func(""))
        print(func("aabccccca"))
        print(func("aabcccccaaa"))

        # 1w次迭代速度统计
        num_str = "1w time cnt"
        print(num_str+' | '+timer.time_str_ms(timeit(lambda: func("aabcccccaaa"), number=10000))+'\n\n')
