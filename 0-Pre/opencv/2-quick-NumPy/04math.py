'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /2-quick-NumPy/04math.py
Description: 
'''

import numpy as np

B = np.arange(3)
print(B)

print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(np.add(B, C))


a = np.arange(10)**3
print(a)
print(a[2])
print(a[2:5])

print(a[:6:2])
for i in a:
    print(i**(1/3.))
