import numpy as np


def newton_modificato(f, df, x0, m, tolx, tolf, nmax):
    """
    Algoritmo di Newton modificato per il calcolo dello zero di una funzione con molteplicità multipla.

    :param f: la funzione di cui calcolare lo zero
    :param df: la derivata della funzione di cui calcolare lo zero
    :param x0: il valore di innesco
    :param m: molteplicità dello zero
    :param tolx: la tolleranza sull'incremento
    :param tolf: la tolleranza sul valore della funzione
    :param nmax: il numero massimo di iterazioni
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """

    def delta(value): return f(value) / df(value) if df(value) > np.spacing(1) else exit("Derivata nulla")

    def prossimax(value): return value - m * delta(value)

    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(delta(x)) >= tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1

    return x, it, xk
