

def secanti(f, x1, x0, tolx, tolf, nmax):
    """

    :param f:
    :param x1:
    :param x0:
    :param tolx:
    :param tolf:
    :param nmax:
    :return:
    """
    def delta(p1, p2): return (f(p1) - f(p2)) / (p1 - p2)
    def prossimax(p1, p2): return p1 - f(p1) / delta

    x = prossimax(x1, x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(delta(x, x1)) >= tolx * abs(x):
        temp = x
        x = prossimax(x, x1)
        fx = f(x)
        x1 = temp
        it += 1

    return x, it, xk
