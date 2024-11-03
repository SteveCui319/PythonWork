"""
题目：输入某年某月某日（yyyy-MM-dd），判断这一天是这一年的第几天？
"""
def calc_days(calc):

    date = calc.split('-')

    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0

    if year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        arr[1] = 29

    for i in range(len(arr)):
        if month > i:
            days += arr[i]
        else:
            days += day
            break

    return days


calc = input("日期：")
num = calc_days(calc)
print(f"天数是：{num}")
