"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""

height = 100
times = 10

drop_distance = []

for i in range(times):
    drop_distance.append(height)
    height /= 2

print(drop_distance)
print('总高度：', 2 * sum(drop_distance) - drop_distance[0])
print('第十次反弹高度：', drop_distance[-1] / 2)





