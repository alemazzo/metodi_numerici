#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 12:19:07 2021

@author: alessandro
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def lagrange(x, k):
    if k == 0:
        zeri = x[1:]
    else:
        zeri = np.append(x[:k], x[k+1:])
    n = np.poly(zeri)
    d = np.polyval(n, x[k])
    return n / d

def interpola(x, y, punti):
    n, m = x.size, punti.size
    L = np.zeros((n, m))
    for k in range(n):
        pol = lagrange(x, k)
        L[k, :] = np.polyval(pol, punti)
        
    return np.dot(y, L)

def f(x): return np.cos(math.pi * x) + np.sin(math.pi * x)
a = 0
b = 2

nodi = np.array([1, 1.5, 1.75])
fnodi = f(nodi)

x = np.linspace(a, b, 100)
y = interpola(nodi, fnodi, x)
plt.plot(nodi, fnodi, 'o')
plt.plot(x, f(x), label="f(x)")
plt.plot(x, y, label="p(x)")
plt.legend()
plt.show()


def p(x): return interpola(nodi, fnodi, np.array([x]))
def r(x): return abs(p(x) - f(x))

x0 = 0.75
rx0 = r(x0)
print(rx0)

nodi = np.array([0.75, 1, 1.5, 1.75])
fnodi = f(nodi)

x = np.linspace(a, b, 100)
y = interpola(nodi, fnodi, x)
plt.plot(nodi, fnodi, 'o')
plt.plot(x, f(x), label="f(x)")
plt.plot(x, y, label="p(x)")
plt.legend()
plt.show()
