'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/07切片和索引.py
Description: 
'''

import numpy

a = numpy.arange(10)
print(a)
s = slice(2, 7, 1)
print(a[s])
s1 = a[2:7:1]
print(s1)

print(a[5])
print(a[2:])
print(a[2:5])

a = numpy.array([[1,2,3],[3,4,5],[4,5,6]])
print(a)
print(a[1:])
