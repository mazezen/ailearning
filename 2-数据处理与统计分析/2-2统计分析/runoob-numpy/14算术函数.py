'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/14算术函数.py
Description: 
'''

import numpy

a = numpy.arange(9, dtype=numpy.float64).reshape(3,3)
print('第一个数组: ')
print(a)
b = numpy.array([10, 10, 10])
print('第二个数组: ')
print(b)
print('\n')

print('相加结果: ')
print(numpy.add(a, b))
print('相乘结果: ')
print(numpy.multiply(a, b))
print('相减结果: ')
print(numpy.subtract(a, b))
print('相除结果: ')
print(numpy.divide(a, b))

a = numpy.array([0.25, 1.33, 1, 100])
print('我们的数组是: ')
print(a)
print('\n')
print('调用 reciprocal 函数: ')
print(numpy.reciprocal(a))

a = numpy.array([1, 10, 100])
print(numpy.power(a, 2))
print(numpy.power(a, numpy.array([1, 2, 3])))


a = numpy.array([1, 10, 100])
print(numpy.mod(a, 2))
