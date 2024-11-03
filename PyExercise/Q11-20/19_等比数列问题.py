"""
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
以后每天早上都吃了前一天剩下的一半零一个。
到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

解题思路：等比数列的逆向推导过程
第10天剩下：1个桃子 第9天剩下：(第10天剩下的桃子数 + 1) * 2 = 4个桃子
第8天剩下：(第9天剩下的桃子数 + 1) * 2 = 10个桃子 ... 第1天剩下：(第2天剩下的桃子数 + 1) * 2
"""

arr = []
arr.insert(0, 1)

for i in range(9, 0, -1):
    n = (arr[0] + 1) * 2
    arr.insert(0, n)

print(arr)
print(f'第一天摘了{arr[0]}个桃子')





