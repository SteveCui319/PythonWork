"""
题目：一个5位数，判断它是不是回文数。

解题思路：回文数是指一个数字从左往右读和从右往左读是一样的数
"""

num = input("input an integer: ")
arr = []

temp = int(num)

for i in range(len(num)):
    arr.insert(0, str(int(num) % 10))
    num = int(num) // 10

arr.reverse()
palin = ''.join(arr)

if str(temp) == palin:
    print(f'{temp}是回文数')
else:
    print(f'{temp}不是回文数')












