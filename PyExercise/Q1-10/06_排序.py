"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""

arr_str = input("输入三个整数: ")
arr = arr_str.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

arr.sort(reverse=False)
print(str(arr))

