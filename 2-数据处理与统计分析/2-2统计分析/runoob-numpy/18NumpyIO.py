'''
Author: mazezen
Date: 2026-05-12
LastEditors: mazezen
LastEditTime: 2026-05-12
FilePath: /ailearning/2-数据处理与统计分析/2-2统计分析/runoob-numpy/18NumpyIO.py
Description: 
'''

import numpy

a = numpy.array([1, 2, 3, 4, 5])
numpy.save("outfile.npy", a)
numpy.save("outfile1", a)
