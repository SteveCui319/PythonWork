"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""


def factorize(num):
    arr = []
    i = 2
    while i <= num:
        if num % i == 0:
            arr.append(i)
            num = num // i
        else:
            i = i + 1

    return arr


n = int(input("请输入一个正整数: "))
result = factorize(n)
print(result)
