#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 09:22:35 2021

@author: alessandro
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from sympy.utilities.lambdify import lambdify
from scipy.optimize import fsolve

# Dati
x = sym.symbols('x')
fx = x - 2 * sym.sqrt(x - 1)
dfx = sym.diff(fx, x, 1)
f = lambdify(x, fx, np)
df = lambdify(x, dfx, np)
a = 1
b = 3
zero = 2

xx = np.linspace(a, b, 100)
yy = f(xx)
dyy = df(xx)
plt.ylim((-1, 1))
plt.plot(xx, 0*xx)
plt.plot(zero, f(zero), 'o')
plt.plot(zero, df(zero), 'o')
plt.plot(xx, yy)
plt.plot(xx, dyy)
plt.show()


# Serve newton di molteplicità 2 per ottenere una convergenza quadratica
def newton(f, df, m, x0, tolx, tolf, nmax=2048):
    def delta(x): return f(x) / df(x) if abs(df(x)) > np.spacing(1) else print("derivata nulla")
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

zero, it, xk = newton(f, df, 2, 3, 1e-12, 1e-12)
print(f"lo zero è in {zero}, con {it} iterate")

def stima(xk):
    k = len(xk) - 4
    n = np.log(np.abs(xk[k + 3] - xk[k + 2]) / np.abs(xk[k + 2] - xk[k + 1]))
    d = np.log(np.abs(xk[k + 2] - xk[k + 1]) / np.abs(xk[k + 1] - xk[k]))
    return n / d

ordine = stima(xk)
print(f"Ordine di convergenza stimato = {ordine}")

plt.title("Iterate metodo Newton")
plt.semilogy(range(1, it + 1), xk)


zero = newton(f, df, 2, 1, 1e-12, 1e-12)
print(f"ZERO = {zero}")