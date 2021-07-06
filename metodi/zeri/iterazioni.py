def iterazioni(g, x0, tolx, nmax):
    """

    :param g:
    :param x0:
    :param tolx:
    :param nmax:
    :return:
    """
    x = g(x0)
    it, xk = 1, [x]
    while it < nmax and abs(x - x0) >= tolx * abs(x):
        x0 = x
        x = g(x)
        xk.append(x)
        it += 1
    return x, it, xk
