"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

解题思路：典型的斐波那契数列问题
"""

# 初始时有一对兔子
adult_rabbits = 1
baby_rabbits = 0

# 模拟12个月的情况
for month in range(1, 13):
    if month == 2:
        print("第%d个月的兔子总数为：%d对" % (month, 1))
        continue
    total_rabbits = adult_rabbits + baby_rabbits
    print("第%d个月的兔子总数为：%d对" % (month, total_rabbits))

    # 下个月新生的兔子数量等于本月成年兔子的数量
    baby_rabbits = adult_rabbits
    # 本月成年兔子的数量等于本月兔子总数
    adult_rabbits = total_rabbits
