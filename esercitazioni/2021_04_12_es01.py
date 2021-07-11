#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 17:22:40 2021

@author: alessandro
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def trapezio(f, a, b, n):
    h = (b - a) / n
    nodi = np.arange(a, b + h, h)
    fnodi = f(nodi)
    return (h / 2) * (fnodi[0] + 2 * np.sum(fnodi[1:n]) + fnodi[n])

def integrale(f, a, b, tol, nmax = 2048):
    err, n = 1, 1
    i1 = trapezio(f, a, b, n)
    while n < nmax and err > tol:
        n *= 2
        i2 = trapezio(f, a, b, n)
        err = abs(i2 - i1) / 3
        i1 = i2
    return i2, n

def f(n): return lambda x: (x ** n) / (x + 10)

y = [math.log(11) - math.log(10)]

for i in range(2, 31):
    y.append((1 / (i - 1)) - 10 * y[i - 2])
    
z = np.zeros((31,))
for i in range(30, 0, -1):
    z[i - 1] = ((1 / 10) * ((1 / (i)) - z[i]) )

xk = np.arange(1, 31)
yk = []
zk = []
for n in range(0, 30):
    i, it = integrale(f(n + 1), 0, 1, 1e-6)
    print(str(i) + " -- " + str(it))
    
    erry = np.abs(y[n] - i) / np.abs(i)
    yk.append(erry)
    
    errz = np.abs(z[n] - i) / np.abs(i)
    zk.append(errz)
    
plt.semilogy(xk, yk, label="Errore y")
plt.semilogy(xk, zk, label="Errore z")
plt.legend()
    