"""
题目：有四个数字：1，2，3，4，能组成多少个互不相同且无重复数字的三位数
"""

for i in range(1, 5):
    for j in range(1, 5):
        for z in range(1, 5):
            if i != j and i != z and j != z:
                print(i, j, z)



