'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/15统计函数.py
Description: 
'''

import numpy
a = numpy.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
print("我们的数组是: ")
print(a)
print('\n')
print('调用amin()函数: ')
print(numpy.amin(a, 1))
print('再次调用amin()函数: ')
print(numpy.amin(a, 0))
print('调用amax()函数: ')
print(numpy.amax(a=a))
print(numpy.amax(a, axis=0))
print('\n')

print('调用ptp()函数: ')
print(numpy.ptp(a))
print(numpy.ptp(a, axis=1))
print(numpy.ptp(a, axis=0))

print('\n')
print(numpy.percentile(a, 50))
print(numpy.percentile(a, 50, axis=1))
print(numpy.percentile(a, 50, axis=0))

print('\n')
print(numpy.median(a))
print(numpy.median(a,axis=1))
print(numpy.median(a, axis=0))


print('\n')
print(numpy.mean(a))
print(numpy.mean(a,axis=1))
print(numpy.mean(a, axis=0))
