#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:23:06 2021

@author: alessandro
"""
import numpy as np
import scipy.linalg as spl
import matplotlib.pyplot as plt

def usolve(U, b):
    m, n = U.shape
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i+1:], x[i+1:])
        x[i] = (b[i] - s) / U[i, i]
    return x

def qr(x, y, n):
    H = np.vander(x, n + 1)
    Q, R = spl.qr(H)
    X = np.dot(Q.T, y)
    pol = usolve(R[:n+1, :], X[:n+1])
    return pol

dati = np.array([1900, 76, 1910, 92, 1920, 106, 1930, 123, 1940, 132, 1950, 151, 1960, 179, 1970, 203, 1980, 226, 1990, 249, 2000, 281, 2010, 305], dtype=float)

x = dati[0::2]
y = dati[1::2]

p1 = qr(x, y, 1)
p2 = qr(x, y, 2)
p3 = qr(x, y, 3)
p4 = qr(x, y, 4)

xx = np.linspace(1900, 2010, 100)
y1 = np.polyval(p1, xx)
y2 = np.polyval(p2, xx)
y3 = np.polyval(p3, xx)

plt.plot(x, y, 'o')
plt.plot(xx, y1, label="p1(x)")
plt.plot(xx, y2, label="p2(x)")
plt.plot(xx, y3, label="p3(x)")
plt.legend()
plt.show()

y1 = np.polyval(p1, x)
y2 = np.polyval(p2, x)
y3 = np.polyval(p3, x)
e1, e2, e3 = 0, 0, 0

for i in range(12):
    e1 += (y1[i] - y[i]) ** 2
    e2 += (y2[i] - y[i]) ** 2
    e3 += (y3[i] - y[i]) ** 2

print(f"e1 = {e1}")
print(f"e2 = {e2}")
print(f"e3 = {e3}")
    
