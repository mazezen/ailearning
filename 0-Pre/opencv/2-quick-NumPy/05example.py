'''
Author: mazezen
Date: 2026-05-14
LastEditors: mazezen
LastEditTime: 2026-05-14
FilePath: /2-quick-NumPy/05example.py
Description: 
'''

import numpy as np
import matplotlib.pyplot as plt

def mandlebrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)"""
    x = np.linspace(-2.5, 1.5, 4*h+1)
    y = np.linspace(-1.5, 1.5, 3*w+1)
    A, B = np.meshgrid(x, y)
    C = A + B*1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r
        div_now = diverge & (divtime == maxit)
        divtime[div_now] = i
        z[diverge] = r
    return divtime
plt.clf()
plt.imshow(mandlebrot(400, 400))

