"""
题目：编程找出1000以内的所有完数。

背景：完数是指一个数恰好等于它的因子（不包括它本身）之和，例如6的因子有1、2、3，而1+2+3=6，所以6是一个完数。

解题思路：
    1.对于每个数n，找出它的所有因子（除了n本身）。
    2.计算这些因子的和，如果和等于n，则n是一个完数。
    3.遍历所有小于1000的数，找出所有的完数。
"""

RAN = 1000

for i in range(2, RAN + 1):
    l = []
    for j in range(1, i):
        if i % j == 0:
            l.append(j)

    if sum(l) == i:
        print(i, ':', l)


