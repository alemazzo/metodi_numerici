import math

import numpy as np


def bisezione(f, a, b, tol):
    """
    Algoritmo di Bisezione per il calcolo dello zero di una funzione.

    :param f: la funzione di cui calcolare lo zero
    :param a: il valore minimo dell'intervallo
    :param b: il valore massimo dell'intervallo
    :param tol: la tollerenza
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """

    def sign(value):
        return math.copysign(1, value)

    fa, fb, x = f(a), f(b), None

    if sign(fa) == sign(fb):
        print("sign(fa) == sign(fb) => Non applicabile")
        return None, 0, []

    max_iterazioni = int(math.ceil(math.log2((b - a) / tol)))
    it, xk = 0, []
    while it < max_iterazioni and abs(b - a) >= tol + np.spacing(1) * max(abs(a), abs(b)):
        x = a + (b - a) / 2  # Calcolo il punto medio
        xk.append(x)
        fx = f(x)
        if sign(fx) == sign(fa):
            a, fa = x, fx
        else:
            b, fb = x, fx
        it += 1
    return x, it, xk
