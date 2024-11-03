"""
题目：将一个列表的数据复制到另一个列表中。
"""
origin = ['javascript', 'php', 'python']
refer = origin
copy = origin[:]  # origin.copy()

print('变量(0x%x): %s' % (id(origin), str(origin)))
print('引用(0x%x): %s' % (id(refer), str(refer)))
print('复制(0x%x): %s' % (id(copy), str(copy)))

"""
赋值是将一个变量指向同一块内存地址，而复制是创建一个新的列表，其内容与原始列表相同，但在内存中占用不同的位置.

origin 和 refer 都指向同一块内存地址，因此它们指向的列表是同一个对象。
copy 是通过切片操作创建的一个新列表，它与原始列表内容相同，但在内存中占据不同的位置。
因此，对 origin 进行修改会影响 refer，因为它们指向同一个对象，而对 copy 的修改不会影响原始列表。这说明了赋值和复制的区别。
"""








