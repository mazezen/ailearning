'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/05从已有的数组创建数组.py
Description: 
'''

import numpy

x = [1, 2, 3]
a = numpy.asarray(x)
print(a)

a = numpy.asarray(a=x, dtype=float, order='C')
print(a)

# 将元组转为 ndarray
x = (1, 2, 3)
a = numpy.asarray(x)
print(a)

# 将元组列表转为 ndarray
x = [(1, 2, 3), (4, 5, 6)]
a = numpy.asarray(x)
print(a)

s = b'Hello world'
a = numpy.frombuffer(s, dtype='S1')
print(a)


# 从迭代对象中建立 ndarray 对象, 返回一维数组
list = range(5)
it = iter(list) # 创建迭代器对象
x =  numpy.fromiter(it, dtype=float)
print(x)
