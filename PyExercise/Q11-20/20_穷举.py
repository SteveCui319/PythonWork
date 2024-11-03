"""
题目：两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
# 方式一（答案不完美）
# T1 = ['a', 'b', 'c']
# T2 = ['x', 'y', 'z']
# arr = []
#
# def comb(i, j):
#     c = T1[i] + '-' + T2[j]
#     return c
#
# for i in range(len(T1)):
#     for j in range(len(T2)):
#         arr.append(comb(i, j))
# print(arr)
# for k in arr:
#     k = str(k)
#     if ('a-x' in k) or ('c-x' in k) or ('c-z' in k):
#         continue
#     print(k)


# 方法二（完美答案）
T1 = ('a', 'b', 'c')
T2 = ('x', 'y', 'z')

arr = []  # 可能的组合


def comb(i, j, k):
    c1 = T1[0] + '-' + T2[i]
    c2 = T1[1] + '-' + T2[j]
    c3 = T1[2] + '-' + T2[k]

    return tuple([c1, c2, c3])


# x, y, z的所有组合
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i == j) or (i == k) or (j == k):
                continue
            arr.append(comb(i, j, k))
print(arr)

for g in arr:
    if ('a-x' in g) or ('c-x' in g) or ('c-z' in g):
        continue
    print(g)





