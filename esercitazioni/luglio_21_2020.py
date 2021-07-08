#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 15:58:48 2021

@author: alessandro
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy.utilities.lambdify import lambdify
from scipy.optimize import fsolve

def f(x): return 2 * math.cos(x) + x * (7 - x) - math.tan((3 / 2) * x)

zero1 = fsolve(f, -1)
zero2 = fsolve(f, 0)
zero3 = fsolve(f, 1)

zeri = np.array([zero1, zero2, zero3])

x = sym.symbols('x')
gx = sym.tan((3 / 2) * x) - 2 * sym.cos(x) - x * (6 - x)
dgx = sym.diff(gx, x, 1)

g = lambdify(x, gx, np)
dg = lambdify(x, dgx, np)

xx = np.linspace(-1, 1, 100)
y = g(xx)

plt.ylim((-3, 3))
plt.plot(zeri, g(zeri), 'o')
plt.plot(zeri, dg(zeri), 'o')
plt.plot(xx, xx, label="y = x")
plt.plot(xx, y, label="g(x)")
plt.plot(xx, dg(xx), label="g'(x)")
plt.legend()
plt.show()


# --------

gx = (sym.tan((3 / 2) * x) - 2 * sym.cos(x)) / (7 - x)
dgx = sym.diff(gx, x, 1)

g = lambdify(x, gx, np)
dg = lambdify(x, dgx, np)

xx = np.linspace(-1, 1, 100)
y = g(xx)

plt.ylim((-3, 3))
plt.plot(zeri, g(zeri), 'o')
plt.plot(zeri, dg(zeri), 'o')
plt.plot(xx, xx, label="y = x")
plt.plot(xx, y, label="g(x)")
plt.plot(xx, dg(xx), label="g'(x)")
plt.legend()
plt.show()

# c)
def puntofisso(g, x0, tol, nmax):
    x = g(x0)
    it, xk = 1, [x]
    while it < nmax and abs(x - x0) >= tol * abs(x):
        x0 = x
        x = g(x)
        xk.append(x)
        it += 1
    return x, it, xk

# d)
x, it, xk = puntofisso(g, 0, 1e-7, 500)
print(x)
plt.plot(np.arange(1, it + 1), xk)

# e)

def stima_ordine(xk):
    k = len(xk) - 4
    n = np.log(np.abs(xk[k + 3] - xk[k + 2]) / np.abs(xk[k + 2] - xk[k + 1]))
    d = np.log(np.abs(xk[k + 2] - xk[k + 1]) / np.abs(xk[k + 1] - xk[k]))
    return n / d

ordine = stima_ordine(xk)
print(ordine)
    
    
