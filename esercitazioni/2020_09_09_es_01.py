#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 08:04:05 2021

@author: alessandro
"""

import numpy as np
import sympy as sym
from sympy.utilities.lambdify import lambdify
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

x = sym.symbols('x')
fx = x - 2 * sym.sqrt(x - 1)
dfx = sym.diff(fx, x, 1)

f = lambdify(x, fx, np)
df = lambdify(x, dfx, np)

a = 1
b = 3
zero = 2

xx = np.linspace(a, b, 100)
y = f(xx)
d = df(xx)
plt.ylim((-1, 1))
plt.plot(xx, y)
plt.plot(xx, d)
plt.plot([zero, ], f(np.array([zero])), 'o')
plt.plot([zero, ], df(np.array([zero])), 'o')
plt.plot(xx, 0*xx)
plt.show()

# Serve newton di grado due poichè la derivata prima vale zero in alpha
# mentre la derivata seconda non si annulla

def newton(f, df, m, x0, tolx, tolf, nmax=2048):
    def delta(x): return f(x) / df(x) if abs(df(x)) > np.spacing(1) else print("Derivata nulla")
    def prossimax(x): return x - m * delta(x)
    
    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) > tolf and abs(delta(x)) > tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1
    
    return x, it, xk

alpha, it, xk = newton(f, df, 2, 3, 1e-12, 1e-12)
print(alpha)

# devo stabilire l'ordine di convergenza

def stimaordine(xk):
    k = len(xk) - 4
    n = np.log(np.abs(xk[k + 3] - xk[k + 2]) / np.abs(xk[k + 2] - xk[k + 1]))
    d = np.log(np.abs(xk[k + 2] - xk[k + 1]) / np.abs(xk[k + 1] - xk[k]))
    return n / d

ordine = stimaordine(xk)
print(f"L'ordine è {ordine}")

# stampo le iterate
plt.title("Iterazioni")
plt.semilogy(range(1, it + 1), xk, 'o')
plt.semilogy(range(1, it + 1), xk)

# provo a partire da x0 = 1
a = newton(f, df, 2, 1, 1e-12, 1e-12)
print(a)














