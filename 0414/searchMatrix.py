matrix = [
    [1, 2, 4, 5],
    [10, 14, 18, 19],
    [21, 22, 24, 25],
]
target = 18


def matrixSearch(matrix, target):
    if not matrix:
        return 0
    row = 0
    col = len(matrix[0]) - 1
    count = 0
    while row < len(matrix) and col >= 0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            col += 1   # 临界条件控制 debug验证
        else:
            count += 1
            col -= 1
            row += 1
    return count
