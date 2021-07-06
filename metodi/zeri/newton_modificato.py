import numpy as np


def newton_modificato(f, df, x0, m, tolx, tolf, nmax):
    """

    :param f:
    :param df:
    :param x0:
    :param m:
    :param tolx:
    :param tolf:
    :param nmax:
    :return:
    """

    def delta(value): return f(value) / df(value) if df(value) > np.spacing(1) else exit("Derivata nulla")

    def prossimax(value): return x - m * delta(value)

    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(delta(x)) >= tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1

    return x, it, xk
