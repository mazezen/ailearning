'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/02数据类型.py
Description: 
'''

import numpy

# 标量数据类型
dt = numpy.dtype(numpy.int32)
print(dt)

# int8, int16, int32, int64 四种数据类型可以使用 'i1', 'i2', 'i4', 'i8'表示
dt1 = numpy.dtype('i1')
dt2 = numpy.dtype('i2')
dt4 = numpy.dtype('i4')
dt8 = numpy.dtype('i8')
print(dt1, dt2, dt4, dt8)

# 字节顺序标注
dt = numpy.dtype('<i4')
print(dt)

dt = numpy.dtype([('age', numpy.int8)])
print(dt)

a = numpy.array([(10, ), (20, ), (30, )], dtype=dt)
print(a)
print(a['age'])

student = numpy.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

a = numpy.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)
