for i in range(1, 10):
    for j in range(1, i+1):
        exp = '%d x %d = %d' % (j, i, i*j)
        print(exp, end='\t') # 制表符分隔。这种方式可以实现将多个内容输出在同一行上的效果。
    print() # 换行

