'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /2-quick-NumPy/03basic_operations.py
Description: 
'''

import numpy as np
from numpy import pi

a = np.array([20, 30, 40, 50])
b = np.arange(4)
print(b)
print(a + b)

print(a - b)

print(b**2)

print(10 * np.sin(a))

print(a < 35)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
print(A*B)
print(A@B)
print(A.dot(B))

rg = np.random.default_rng(1)
print(rg)
a = np.ones((2, 3), dtype=int)
b = rg.random((2, 3))
a *= 3
print(a)
print(b+a)

a = np.ones(3, dtype=np.int32)
b = np.linspace(0, pi, 3)
print(b.dtype.name)
print(a+b)
print((a+b).dtype)
print(np.exp((a+b)*1j))

a = rg.random((2, 3))
print(a)
print(a.sum())
print(a.min())
print(a.max())

b = np.arange(12).reshape(3, 4)
print(b)
print(b.sum(axis=0))
print(b.sum(axis=1))
print(b.min(axis=0))
print(b.cumsum(axis=1))

