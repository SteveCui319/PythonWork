"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

解题思路：对象的构造方法和使用
"""


class Code:
    content = ''
    letter = 0
    num = 0
    space = 0
    other = 0

    # 构造函数
    def __init__(self):
        self.content = content

    # 分析函数
    def analysis(self):
        for i in self.content:
            if i.isalpha():
                self.letter += 1
            elif i.isdigit():
                self.num += 1
            elif i.isspace():
                self.space += 1
            else:
                self.other += 1

    # 显示函数
    def showData(self):
        form = '字母（%d） 空格（%d） 数字（%d） 其他字符（%d）'
        data = (self.letter, self.space, self.num, self.other)
        print(form % data)


content = input('输入一段内容（英文）：\n')
code = Code()
code.analysis()
code.showData()
