def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


num = int(input("输入一个数字："))
print(fib(num))
