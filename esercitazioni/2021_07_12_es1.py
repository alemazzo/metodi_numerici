#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:38:14 2021

@author: alessandro
"""

import math
import numpy as np
import scipy.linalg as spl
import matplotlib.pyplot as plt


def usolve(U, b):
    n, m = U.shape
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i+1:], x[i+1:])
        x[i] = (b[i] - s) / U[i, i]
    return x

x = np.array([0, 4, 0, 5], dtype=float)
y = np.array([0, 0, 4, 6], dtype=float)

A = np.zeros((4, 3))
b = np.zeros((4, 1))
for i in range(4):
    A[i] = np.array([x[i], y[i], 1])
    b[i] = - (x[i] ** 2 + y[i] ** 2)


grado = 2
Q, R = spl.qr(A)
Y = np.dot(Q.T, b)
sol = usolve(R[:grado + 1], Y[:grado + 1])
print(sol)

temp = np.dot(A, sol) - b
norma = spl.norm(temp, 2) ** 2
print(f"il quadrato vale {norma}")


a0 = sol[0][0]
a1 = sol[1][0]
a2 = sol[2][0]

c = (-a0/2, -a1/2)
r = math.sqrt((a0 ** 2) / 4 + (a1 ** 2) / 4 - a2)
print(f"Centro = {c}")
print(f"Raggio = {r}")

def fx(t): return -a0/2 + r * np.cos(t)
def fy(t): return -a1/2 + r * np.sin(t)

t = np.linspace(0, 2 * math.pi, 100)
xs = fx(t)
ys = fy(t)
plt.plot(x, y, 'o')
plt.plot(xs, ys)