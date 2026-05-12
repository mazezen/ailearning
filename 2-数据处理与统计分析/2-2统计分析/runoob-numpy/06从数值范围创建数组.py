'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/06从数值范围创建数组.py
Description: 
'''

import numpy

# 生成 0 - 4 长度为 5 的数组
x = numpy.arange(5)
print(x)
 
# 设置元素的类型
x2 = numpy.arange(5, dtype=float)
print(x2)

x3 = numpy.arange(10, 20, 2, dtype=int)
print(x3)

a = numpy.linspace(1, 10, 10)
print(a)

# 设置元素全部为1的等差数列
print(numpy.linspace(1, 1, 10))

# 将 endpoint 设为 false，不包含终止值, 设置 为 true , 包含终止值
print(numpy.linspace(10, 20, 5, endpoint = False))
print(numpy.linspace(10, 20, 5, endpoint = True))

print(numpy.linspace(1, 10, 10, retstep=True))
print(numpy.linspace(1, 10, 10).reshape([10, 1]))

print(numpy.logspace(1.0, 2.0, num=10))

