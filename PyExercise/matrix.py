# matrix multiplication


def matrix_multiply(matrix1, matrix2):
    # 初始化一个于结果相同维度的矩阵
    res = [[0 for x in range(3)] for y in range(3)]

    # explicit for loops
    for i in range(len(matrix1)): # 遍历matrix1的每一行
        for j in range(len(matrix2[0])): # 遍历matrix2的每一列
            for k in range(len(matrix2)):
                # resulted matrix
                res[i][j] += matrix1[i][k] * matrix2[k][j]

    return res


matrix1 = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[5, 8, 1],
           [6, 7, 3],
           [4, 5, 9]]

result = matrix_multiply(matrix1, matrix2)
print(result)
