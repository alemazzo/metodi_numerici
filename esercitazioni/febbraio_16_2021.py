import math
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
from sympy.utilities.lambdify import lambdify

def stima_ordine(xk, num):
    k = num - 4
    num = np.log(abs(xk[k + 3] - xk[k + 2]) / abs(xk[k + 2] - xk[k + 1]))
    den = np.log(abs(xk[k + 2] - xk[k + 1]) / abs(xk[k + 1] - xk[k]))
    return num / den

def newton(f, df, m, x0, tolx, tolf, nmax):
    def delta(val): return f(val) / df(val) if abs(df(val)) > np.spacing(1) else print("DERIVATA NULLA")
    def prossimax(val): return val - delta(val) * m
    
    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x,]
    while it < nmax and abs(fx) > tolf and abs(delta(x)) > tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1
    
    return x, it, xk


x = sym.symbols('x')
fx = x - (1/3) * sym.sqrt(30*x - 25)
dfx = sym.diff(fx, x, 1)

f = lambdify(x, fx, np)
df = lambdify(x, dfx, np)

a = 5 / 6
b = 25 / 6

xs = np.linspace(a, b, 100)


xz = xs * 0
plt.plot(xs, xz)
plt.plot(xs, f(xs))



## Calcolo lo zero
alpha, it, xk = newton(f, df, 1, a, 1e-18, 1e-18, 1_000)
print(f"Lo zero è {alpha}, it = {it}")

# Punto C
ordine = stima_ordine(xk, it)
print(f"L'ordine è {ordine}")
plt.show()

### Punto D
plt.semilogy(range(it), xk)
