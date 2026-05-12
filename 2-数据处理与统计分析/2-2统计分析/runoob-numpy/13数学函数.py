'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/13数学函数.py
Description: 
'''

import numpy

a = numpy.array([0, 30, 45, 60, 90])
print('不同角度的正弦值: ')
# 通过乘 pi/180 转化为弧度  
print(numpy.sin(a*numpy.pi/180))
print('余弦值: ')
print(numpy.cos(a*numpy.pi/180))
print('正切值: ')
print(numpy.tan(a*numpy.pi/180))
print('\n')


a = numpy.array([1.0,5.55,  123,  0.567,  25.532])
print(a)
print(numpy.around(a))
print(numpy.around(a, decimals=1))
print(numpy.around(a, decimals=-1))
print('\n')

a = numpy.array([-1.7, 1.5, -0.2, 0.6, 10])
print(a)
print('修改后的数组: ')
print(numpy.floor(a))
print('\n')

print(numpy.ceil(a))

