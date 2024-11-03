"""
题目：打印出所有的"水仙花数"
"""
# digits = []
# for i in range(100, 1000):
#     # 转换为字符串
#     num_str = str(i)
#
#     temp_digits = []
#     for digit_char in num_str:
#         digit = int(digit_char)
#         digits.append(digit)
#
#     digits.extend(temp_digits)
#
# print(digits)

arr = []
for i in range(100, 1000):
    a = int(i / 100) % 10
    b = int(i / 10) % 10
    c = int(i / 1) % 10

    if a**3 + b**3 + c**3 == i:
        arr.append(i)

print(f"水仙花数是：{arr}")













