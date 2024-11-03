"""
题目：判断101-200之间有多少个素数，并输出所有素数。
"""
min_num = 101
max_num = 200
count = 0

for i in range(min_num, max_num + 1):
    if i > 1:
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            count += 1
            print(i)

print(f"总共有{count}个质数")

