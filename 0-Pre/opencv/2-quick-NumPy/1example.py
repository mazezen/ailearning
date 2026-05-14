'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /2-quick-NumPy/1example.py
Description: 
'''

import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape)
print(a.ndim)
print(a.dtype.name)
print(a.itemsize)
print(a.size)
print(type(a))

b = np.ndarray([6, 7, 8])
print(type(b))
