'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/03数组属性.py
Description: 
'''

import numpy

a = numpy.arange(24)
print(a.ndim)

b = a.reshape(2, 4, 3)
print(b.ndim)

a = numpy.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

a.shape = (3, 2)
print(a)

x = numpy.array([1, 2, 3, 4, 5, 6], dtype=numpy.int8)
print(x.itemsize)

y = numpy.array([1, 2, 3, 4, 5], dtype=numpy.float64)
print(y.itemsize)

print(x.flags)
