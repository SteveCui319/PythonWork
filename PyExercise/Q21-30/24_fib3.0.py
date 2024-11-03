"""
题目：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

解题思路： f(n)/g(n) = (f(n-1) + g(n-1))/f(n-1)
"""
arr = []

fn, gn = 1, 1

for i in range(20):
    fn, gn = fn + gn, fn
    arr.append('%d / %d' % (fn, gn))
print(arr)
# eval() 函数用来执行一个字符串表达式，并返回表达式的值
print(eval('+'.join(arr)))






















