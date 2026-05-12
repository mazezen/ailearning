'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/01ndarray.py
Description: 
'''

import numpy

# print(numpy.__version__)

a = numpy.array([1, 2, 3])
print(a)

a1 = numpy.array([[1, 2], [3, 4]])
print(a1)

a2 = numpy.array([1, 2, 3, 4, 5], dtype=complex)
print(a2)

a3 = numpy.array([1, 2, 3, 4, 5], ndmin=2)
print(a3)

