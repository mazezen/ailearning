'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/08高级索引.py
Description: 
'''

import numpy
x = numpy.array([[1, 2], [3, 4], [5, 6]])
print(x[[0, 1, 2], [0, 1, 0]]) # [1, 4, 5]
print(x[[0, 1, 2], [0, 1, 1]]) # [1, 4, 6]
print(x[[1, 1, 2], [0, 1, 1]]) # [3, 4, 6]
print('\n')

x = numpy.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print(x)
print('\n')

rows = numpy.array([[0,0], [3,3]])
cols = numpy.array([[0,2], [0,2]])
y = x[rows, cols]
print(y)
print('\n')

a = numpy.array([[1,2,3], [4,5,6],[7,8,9]])
print(a)
print(a[1:3, 1:3])
print(a[1:3, [1,2]])
print(a[...,1:])

print('\n')

x = numpy.array([[  0,  1,  2],[  3,  4,  5],[  6,  7,  8],[  9,  10,  11]])  
print('大于5 的元素: ')
print(x[x > 5])

a = numpy.array([numpy.nan, 1, 2, numpy.nan, 3,4,5])
print(a[~numpy.isnan(a)])

x = numpy.arange(9)
print(x)
print('\n')
print(x[[0, 6]])
print(x[[0, 6]][0])
print(x[[0, 6]][1])
# print(x[[0, 6]][2]) # index out of bouds for axis 0 with size 2

x = numpy.arange(32).reshape((8, 4))
print(x)
# 二维数组读取指定下标对应的行
print(x[[4,2,1,7]]) # 输出下表为 4, 2, 1, 7 对应的行
print('\n')

x = numpy.arange(32).reshape(4, 8)
print(x)
print(x[[-2, -1]])

