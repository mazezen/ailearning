'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/09广播.py
Description: 
'''

import numpy

a = numpy.array([1, 2, 3, 4])
b = numpy.array([10, 20, 30, 40])
print(a*b)
print('\n')

a = numpy.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = numpy.array([0,1,2])
print(a + b)
print('\n')
 
a = numpy.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20],
           [30,30,30]])
b = numpy.array([1,2,3])
bb = numpy.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)
