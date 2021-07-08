import numpy as np


def trapezio(f, a, b, n=1):
    h = (b - a) / n
    nodi = np.arange(a, b + h, h)
    fnodi = f(nodi)
    integrale = (h / 2) * (fnodi[0] + 2 * np.sum(fnodi[1:n]) + fnodi[n])
    return integrale


def simpson(f, a, b, n=1):
    """

    :param f:
    :param a:
    :param b:
    :param n:
    :return:
    """
    h = (b - a) / (2 * n)
    nodi = np.arange(a, b + h, h)
    fnodi = f(nodi)
    integrale = (h / 3) * (fnodi[0] + 2 * np.sum(fnodi[2::2]) + 4 * np.sum(fnodi[1::2]) + fnodi[2 * n])
    return integrale


def integrale(f, a, b, tol, metodo, nmax=2048):
    """

    :param f:
    :param a:
    :param b:
    :param tol:
    :param metodo:
    :param nmax:
    :return:
    """
    err = 1
    n = 1
    I = metodo(f, a, b, n)
    while n <= nmax and err > tol:
        n *= 2
        I2 = metodo(f, a, b, n)
        if metodo == trapezio:
            err = np.abs(I2 - I) / 3
        else:
            err = np.abs(I2 - I) / 15
        I = I2
    return I, n
