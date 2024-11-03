"""
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
"""

a = int(input('input a: '))
n = int(input('input n: '))

x = 0  # 各项值
l = []

for i in range(n):
    x += a * (10 ** i)
    l.append(x)

# map()：映射 -》 将集合里的元素一一转换成str类型
# join()：序列中的元素以指定的字符连接生成一个新的字符串。
exp = ' + '.join(map(str, l))
res = sum(l)

print('%s = %d' % (exp, res))