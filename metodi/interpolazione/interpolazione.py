import math

import numpy as np


def zeri_di_chebyshev(a, b, n):
    """
    Ottieni i nodi di Chebyshev nell'intervallo specificato.

    :param a: lower bound del range
    :param b: upper bound del range
    :param n: il numero di punto (grado del polinomio + 1)
    :return: nodi di Chebyshev dell'intervallo [a, b]
    """
    t1 = (a + b) / 2
    t2 = (b - a) / 2
    x = np.zeros((n,))
    for k in range(n):
        x[k] = t1 + t2 * np.cos((math.pi * (2 * k + 1)) / (2 * n))
    return x


def lagrange(x, k):
    """

    :param x:
    :param k:
    :return:
    """
    if k == 0:
        zeri = x[1:]
    else:
        zeri = np.append(x[:k], x[k + 1:])

    numeratore = np.poly(zeri)
    denominatore = np.polyval(numeratore, x[k])
    return numeratore / denominatore


def interpola(x, y, punti):
    """

    :param x:
    :param y:
    :param punti:
    :return:
    """
    n, m = x.size, punti.size
    L = np.zeros((n, m))
    for k in range(n):
        p = lagrange(x, k)
        L[k, :] = np.polyval(p, punti)
    return np.dot(y, L)
