'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/04创建数组.py
Description: 
'''

import numpy

'''
[[9218868437227405311   -4503599627370497]
 [4611686018427387904 4372995238176751616]
 [   4503599627370496                   1]]
'''
x = numpy.empty([3, 2], dtype=int)
print(x)

# 默认浮点数
x = numpy.zeros(5)
print(x)

y = numpy.zeros((5,), dtype=int)
print(y)

z = numpy.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])
print(z)

x = numpy.ones(5)
print(x)

x = numpy.ones([2, 2], dtype=int)
print(x)


# 创建一个 3*3 的二维数组
arr = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

# 创建一个与 arr 形状形同的数组, 所有元素用 0 填充
zeros_arr = numpy.zeros_like(arr)
print(zeros_arr)

# 创建一个与 arr 形状相同的数组, 所有元素用 1 填充
ones_arr = numpy.ones_like(arr)
print(ones_arr)
