import math

import numpy as np


def zeri_di_chebyshev(a, b, n):
    """
    Nodi di Chebyshev per il calcolo del polinomio interpolatore nell'intervallo specificato.

    :param a: lower bound del range
    :param b: upper bound del range
    :param n: il numero di punti (grado del polinomio + 1)
    :return: i nodi di Chebyshev dell'intervallo [a, b]
    """
    t1 = (a + b) / 2
    t2 = (b - a) / 2
    x = np.zeros((n,))
    for k in range(n):
        x[k] = t1 + t2 * np.cos((math.pi * (2 * k + 1)) / (2 * n))  # funzione per il calcolo dei nodi di Chebyshev
    return x


def lagrange(x, k):
    """
    Polinomio di Lagrange di indice k

    :param x: ascisse dei nodi da interpolare
    :param k: indice del polinomio di Lagrange
    :return: coefficenti del k-esimo polinomio di Lagrange calcolato nelle ascisse dei nodi da interpolare
    """

    # Seleziono tutte le x tranne la k-esima
    if k == 0:
        zeri = x[1:]
    else:
        zeri = np.append(x[:k], x[k + 1:])

    numeratore = np.poly(zeri)
    denominatore = np.polyval(numeratore, x[k])  # il denominatore è uguale al numeratore valutato in x[k]
    return numeratore / denominatore


def interpola(x, y, punti):
    """
    Interpolazione dei nodi composti dalle coordinate (x, y) calcolato nei punti specificati.

    :param x: le ascisse dei nodi da interpolare
    :param y: le ordinate dei nodi da interpolare
    :param punti: i punti in cui valutare il polinomio interpolatore
    :return: il valore del polinomio interpolatore nei punti specificati
    """
    n, m = x.size, punti.size
    L = np.zeros((n, m))
    for k in range(n):
        p = lagrange(x, k)
        L[k, :] = np.polyval(p, punti)
    return np.dot(y, L)
