'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/10迭代数组.py
Description: 
'''

import numpy

a = numpy.arange(6).reshape(2, 3)
print("原始数组: ")
print(a)
print('\n')

for x in numpy.nditer(a):
    print(x, end=", ")
print('\n')

a = numpy.arange(6).reshape(2, 3)
for x in numpy.nditer(a.T):
    print(x, end=", ")
print('\n')

for x in numpy.nditer(a.T.copy(order='C')):
    print(x, end=", ")
print('\n')

a = numpy.arange(0,60,5) 
a = a.reshape(3,4)  
print ('原始数组是：') 
print (a) 
print ('\n') 
print ('原始数组的转置是：') 
b = a.T 
print (b) 
print ('\n') 
print ('以 C 风格顺序排序：') 
c = b.copy(order='C')  
print (c)
for x in numpy.nditer(c):  
    print (x, end=", " )
print  ('\n') 
print  ('以 F 风格顺序排序：')
c = b.copy(order='F')  
print (c)
for x in numpy.nditer(c):  
    print (x, end=", " )

print('\n')

a = numpy.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是: ')
print(a)
print('\n')
for x in numpy.nditer(a, op_flags=['readwrite']):
    x[...] = 2*x
print('修改后的数组是: ')
print(a)
