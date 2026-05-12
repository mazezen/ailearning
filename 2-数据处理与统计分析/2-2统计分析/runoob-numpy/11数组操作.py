'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/11数组操作.py
Description: 
'''

import numpy

a = numpy.arange(8)
print(a)
print('\n')

b = a.reshape(4, 2)
print(b)
print('\b')

for row in a:
    print(row)

for row in a.flat:
    print(row)

print(a.flatten())
print(a.flatten(order='F'))

print(a.ravel())
print('\n')

a = numpy.arange(12).reshape(3, 4)
print(a)
print('\n')

print(numpy.transpose(a))

print('\n')
a = numpy.arange(12).reshape(3,4)
print("原数组: ")
print(a)
print("转置数组: ")
print(a.T)
print('\n')


a = numpy.arange(8).reshape(2,2,2)
print ('原数组：')
print (a)
print ('获取数组中一个值：')
print(numpy.where(a==6))   
print(a[1,1,0])  # 为 6
print ('\n')


# 将轴 2 滚动到轴 0（宽度到深度）
print ('调用 rollaxis 函数：')
b = numpy.rollaxis(a, 2, 0)
print(b)
print(numpy.where(b==6))
print('\n')

# 将轴 2 滚动到轴 1：（宽度到高度）
print ('调用 rollaxis 函数：')
c = numpy.rollaxis(a, 2, 1)
print(c)
print(numpy.where(c==6))
print('\n')


# 创建了三维的 ndarray
a = numpy.arange(8).reshape(2,2,2)
 
print ('原数组：')
print (a)
print ('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
 
print ('调用 swapaxes 函数后的数组：')
print (numpy.swapaxes(a, 2, 0))


a = numpy.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = numpy.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
# 两个数组的维度相同
 
print ('沿轴 0 连接两个数组：')
print (numpy.concatenate((a,b)))
print ('\n')
 
print ('沿轴 1 连接两个数组：')
print (numpy.concatenate((a,b),axis = 1))


a = numpy.arange(9)
 
print ('第一个数组：')
print (a)
print ('\n')
 
print ('将数组分为三个大小相等的子数组：')
b = numpy.split(a,3)
print (b)
print ('\n')
 
print ('将数组在一维数组中表明的位置分割：')
b = numpy.split(a,[4,7])
print (b)
