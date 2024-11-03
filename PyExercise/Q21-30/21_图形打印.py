"""
题目：打印三角形

解题思路：
    - 空格数 = 总行数 - 当前行
    - 星号数 = 2 * 行数 - 1  （1，3，5，7，... factor = 2）
"""
h = int(input('输入三角形高度: '))
show = '*'
hide = ' '

for i in range(1, h + 1):
    print(hide * (h - i), end='')
    print(show * (2 * i - 1))


"""
题目：利用循环打印菱形

解题思路：
    1. 先打印上半部分三角形
        - 上半部分高度 = 总高度 // 2 + 1 
        - 空格数 = 上半部分高度 - 当前行
        - 星号数 = 2 * 当前行数 - 1
        
    2. 再打印下半部分三角形
        - 下半部分高度 = 总高度 // 2
        - 空格数 = 当前行数
        - 星号数 = 总高度 - factor 2
"""

h = int(input('输入菱形高度（奇数）: '))
show = '*'
hide = ' '

for i in range(1, h // 2 + 1 + 1):
    s1 = h // 2 + 1 - i  # 空格数
    s2 = 2 * i - 1  # 字符数
    print(hide * s1 + show * s2)

for i in range(1, h // 2 + 1):
    s1 = i
    s2 = h - i * 2
    print(hide * s1 + show * s2)


"""
题目：空心线条等腰三角形

解题思路：
    1. 左侧空格
    2. 左边的 ‘/’
    3. 中间的空格或者_
    4. 右边的 ‘\’
"""

h = int(input('请输入高度：'))

for i in range(1, h + 1):
    # 空格数 = 总行数 - 当前行
    print(' ' * (h - i), end='')
    print('/', end='')
    # 中间空格为双数： 2(x-1)
    # 如果不是最后一行，为空格
    # 如果是最后一行， 为’_‘
    interval = ' '
    if i == h:
        interval = '_'
    print((i - 1) * 2 * interval, end='')
    # 单独一个’\‘是打印不出来的
    print('\\')


"""
题目：空心线条菱形

解题思路：
    1. 左侧空格
    2. 左边的 ‘/’
    3. 中间的空格或者_
    4. 右边的 ‘\’
"""
h = int(input('请输入高度：'))
half = h // 2

left_symbol = '/'
right_symbol = '\\'
interval = ' '

# 上半部分
for i in range(1, half + 1):
    print(interval * (half - i), end='')
    print(left_symbol, end='')
    print((i - 1) * 2 * interval, end='')
    print(right_symbol)

# 下半部分
for i in range(1, half + 1):
    print((i - 1) * interval, end='')
    print(right_symbol, end='')
    print((half - i) * 2 * interval, end='')
    print(left_symbol)










