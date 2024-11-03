"""
题目：利用递归方法求5!
"""
def factorial(n):
    if not isinstance(n, int):
        raise TypeError
    if n < 1:
        raise Exception('value should greater zero')
    if n == 1:
        return 1
    return factorial(n - 1) * n


n = int(input('input a number: '))
result = factorial(n)
print(result)
