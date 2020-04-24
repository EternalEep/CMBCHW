def factorial(n):
    if n == 1:
        return 1  # 递归结束  递归到201万  怎么检查 DEBUG 思考题
    return n * factorial(n - 1)  # 问题规模减1，递归调用


if __name__ == '__main__':
    print(factorial(10))

    i = 10
    sum = 1
    while i > 0:
        sum = sum * i
        i = i - 1

    print(sum)
