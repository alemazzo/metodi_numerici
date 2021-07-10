#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:57:16 2021

@author: alessandro
"""

import math
import numpy as np
import matplotlib.pyplot as plt

u = []
for i in range(1, 36):
    u.append((15 * ((3/5) ** i + 1)) / (5 * (3/5) ** i + 3))

print(u)

u1 = [4]
for i in range(1, 35):
    u1.append(8 - (15 / (u1[i - 1])))
print(u1)

u2 = [4, 17/4]
for i in range(2, 35):
    u2.append(108 - (815 / u2[i - 1]) + (1500 / (u2[i - 1] * u2[i - 2])))
print(u2)

u = np.array(u)
u1 = np.array(u1)
u2 = np.array(u2)

eu1 = np.abs(u1 - u)
eu2 = np.abs(u2 - u)
x = np.arange(1, 36)
plt.semilogy(x, eu1, label="Errore u1")
plt.semilogy(x, eu2, label="Errore u2")
plt.legend()
plt.show()

# Punti fissi
def iterazione(g, x0, tolx, nmax=2048):
    x = g(x0)
    it, xk = 1, [x]
    while it < nmax and abs(x - x0) > tolx * abs(x):
        x0 = x
        x = g(x0)
        xk.append(x)
        it += 1
    return x, it, xk

def g1(x): return 8 - 15/x
def g2(x): return 108 - 815/x + 1500/(x**2)

def dg1(x): return 15 / (x ** 2)
def dg2(x): return 815 / (x ** 2) - 1500 / (x ** 3)

xx = np.arange(1, 110)
plt.title("g1(x)")
plt.ylim(-5, 10)
plt.plot(xx, xx)
plt.plot(xx, g1(xx), label="g1(x)")
plt.plot(xx, dg1(xx), label="g1'(x)")
plt.plot([5], [g1(5)], 'o')
plt.plot([5], [dg1(5)], 'o')
plt.legend()
plt.show()

plt.title("g2(x)")
plt.ylim(-5, 110)
plt.plot(xx, xx)
plt.plot(xx, g2(xx), label="g2(x)")
plt.plot(xx, dg2(xx), label="g2'(x)")
plt.plot([5], [g2(5)], 'o')
plt.plot([5], [dg2(5)], 'o')
plt.plot([100], [g2(100)], 'o')
plt.plot([100], [dg2(100)], 'o')
plt.legend()
plt.show()

punto, it, xk = iterazione(g1, 1, 1e-12)
print(f"g1 => {punto} con {it} iterazioni")

punto, it, xk = iterazione(g2, 1, 1e-12)
print(f"g2 => {punto} con {it} iterazioni")