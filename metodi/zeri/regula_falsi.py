import math

import numpy as np


def regula_falsi(f, a, b, tol, nmax):
    """
    Algoritmo di regula falsi per il calcolo dello zero di una funzione.

    :param f: la funzione di cui trovare lo zero
    :param a: il valore minimo del dominio
    :param b: il valore massimo del dominio
    :param tol: la tolleranza
    :param nmax: il numero massimo di iterazioni
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """

    def sign(value):
        return math.copysign(1, value)

    def prossimax(x): return a - fa * (b - a) / (fb - fa)

    fa, fb, x = f(a), f(b), None
    if sign(fa) == sign(fb):
        print("sign(fa) == sign(fb) => Non applicabile")
        return None, 0, []

    fx = fa
    it, xk = 0, []
    while it < nmax and abs(b - a) >= tol + np.spacing(1) * max(abs(a), abs(b)) and abs(fx) >= tol:
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        if sign(fx) == sign(fa):
            a, fa = x, fx
        else:
            b, fb = x, fx
        it += 1

    return x, it, xk
