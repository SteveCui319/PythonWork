"""
题目：一个整数，它加上100和加上268后都是一个完全平方数，请问该数是多少？

解题思路：
1. 设 x+100 = m^2，x+268 = n^2，其中 m 和 n 都是整数。
2. 根据以上两个等式，可以得到：n^2 - m^2 = (n+m)(n-m) = 168。
3. 找出两个数的因子，使得它们的乘积等于168，并且 n 和 m 都是整数。
4. 找到符合条件的 n 和 m 后，解出 x 的值，即可得到答案。
"""
# import math
#
# for i in range(10000):
#     m = math.sqrt(i + 100)
#     n = math.sqrt(i + 268)
#
#     if m % 1 == 0 and n % 1 == 0:
#         print(i)  # output: 21 261 1581

for i in range(1, 169):
    for j in range(1, 169):
        if i * j == 168 and (i + j) % 2 == 0:
            #print(i, j)
            n = (i + j) / 2
            m = (j - i) / 2
            if n and m > 0:
                #print(n, m)
                x1 = m**2 - 100
                x2 = n**2 - 268
                if x1 == x2 and x1 > 0:
                    print(int(x1))

