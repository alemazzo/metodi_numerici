def secanti(f, x1, x0, tolx, tolf, nmax):
    """
    Algoritmo delle secanti per il calcolo dello zero di una funzione.

    :param f: funzione di cui calcolare lo zero
    :param x1: secondo punto di innesco
    :param x0: primo punto di innesco
    :param tolx: tolleranza sull'incremento
    :param tolf: tolleranza sul valore della funzione
    :param nmax: numero massimo di iterazioni
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """

    def delta(p1, p2): return (f(p1) - f(p2)) / (p1 - p2)

    def prossimax(p1, p2): return p1 - f(p1) / delta(p1, p2)

    x = prossimax(x1, x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(delta(x, x1)) >= tolx * abs(x):
        temp = x
        x = prossimax(x, x1)
        xk.append(x)
        fx = f(x)
        x1 = temp
        it += 1

    return x, it, xk
