
def corde(f, m, x0, tolx, tolf, nmax):
    """

    :param f:
    :param m:
    :param x0:
    :param tolx:
    :param tolf:
    :param nmax:
    :return:
    """

    def prossimax(prev): return prev - f(x0) / m

    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(f(x0) / m) >= tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1
    return x, it, xk


def corde_con_derivata(f, df, x0, tolx, tolf, nmax):
    return corde(f, df(x0), x0, tolx, tolf, nmax)
