'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/12字符串操作.py
Description: 
'''

import numpy


print(numpy.char.add(['hello'], [' world']))
print(numpy.char.multiply('hello ', 3))
print(numpy.char.center('python', 20, fillchar='*'))
print(numpy.char.capitalize('python'))
print(numpy.char.title('i love python'))
print(numpy.char.lower(['PYTHON', 'NUMPY']))
print(numpy.char.lower('PYTHON'))
print(numpy.char.upper(['python', 'numpy']))
print(numpy.char.upper('python'))
print(numpy.char.split('i like python'))
print(numpy.char.split('www.google.com', '.'))
print(numpy.char.splitlines('i\nlove\npython'))
print(numpy.char.strip(' py '))
print(numpy.char.join(':', 'python'))
print(numpy.char.replace('google', 'g', 'm'))
print(numpy.char.encode('python', 'cp037'))
print(numpy.char.decode(numpy.char.encode('python', 'cp037'), 'cp037'))
