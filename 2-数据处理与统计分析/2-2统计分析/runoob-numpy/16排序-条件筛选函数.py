'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/16排序-条件筛选函数.py
Description: 
'''

import numpy

a = numpy.array([[3, 7], [9, 1]])
print(a)
print('\n')
print(numpy.sort(a=a))
print(numpy.sort(a=a, axis=0))

dt = numpy.dtype([('name', 'S10'), ('age', int)])
a = numpy.array([('raju', 21), ('anil', 25), ('ravi', 17)], dtype=dt)
print(numpy.sort(a, order='name'))
print('\n')

x = numpy.array([3, 1, 2])
print(x)
print('\n')
print(numpy.argsort(x))


nm =  ('raju','anil','ravi','amar') 
dv =  ('f.y.',  's.y.',  's.y.',  'f.y.') 
ind = numpy.lexsort((dv,nm))  
print ('调用 lexsort() 函数：') 
print (ind) 
print ('\n') 
print ('使用这个索引来获取排序后的数据：') 
print ([nm[i]  +  ", "  + dv[i]  for i in ind])
