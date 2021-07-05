import math

import numpy as np


def regula_falsi(f, a, b, tol, nmax):
    """

    :param f:
    :param a:
    :param b:
    :param tol:
    :param nmax:
    :return:
    """

    def sign(value):
        return math.copysign(1, value)

    fa, fb, x = f(a), f(b), None
    if sign(fa) == sign(fb):
        print("sign(fa) == sign(fb) => Non applicabile")
        return None, 0, []

    fx = fa
    it, xk = 1, []
    while it < nmax and abs(b - a) >= tol + np.spacing(1) * max(abs(a), abs(b)) and abs(fx) >= tol:
        x = 1
        xk.append(x)
        fx = f(x)
        if sign(fx) == sign(fa):
            a, fa = x, fx
        else:
            b, fb = x, fx
        it += 1

    return x, it, xk
