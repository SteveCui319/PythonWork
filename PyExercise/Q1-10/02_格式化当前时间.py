"""
题目：格式化当前输出的时间
"""
import time

# 获取自1970年1月1日到现在的时间
num = 1
while num <= 3:
    ticks = time.time()
    # print(f"当前时间戳为：{ticks}")
    num += 1
    # time.sleep(10)

# 获取当前时间
localtime = time.localtime()
print(localtime)

# 格式化当前时间
localtime2 = time.asctime()
print(localtime2)

# 或者也可以使用strftime()实现格式化
print(time.strftime("%Y-%m-%d %H:%M:%S", localtime))
