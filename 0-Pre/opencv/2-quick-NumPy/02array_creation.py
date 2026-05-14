'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /2-quick-NumPy/02array_creation.py
Description: 
'''

import numpy as np
from numpy import pi
import sys

# create an array from a regular Python List or Tuple using the `array`
a = np.array([1, 2, 3])
b = np.array([1.2, 2.1,3.5])
print(a)
print(type(a))
print(a.dtype)
print(b)
print(type(b))
print(b.dtype)

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)

c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

print(np.zeros((3, 4)))

print(np.ones((2, 3, 4), dtype=np.int16))

print(np.empty((2, 3)))

print(np.arange(10, 30, 5))

print(np.linspace(0, 2, 9))

print(np.arange(6))

print(np.arange(6).reshape(2, 3))

print(np.arange(24).reshape(2, 3, 4))

print(np.arange(10000))

print(np.arange(10000).reshape(100, 100))

print(np.set_printoptions(threshold=sys.maxsize))

