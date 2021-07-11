def corde(f, m, x0, tolx, tolf, nmax):
    """
    Algoritmo delle corde per il calcolo dello zero di una funzione.

    :param f: la funzione di cui calcolare lo zero
    :param m: il valore del coefficente angolare della retta
    :param x0: il valore di innesco
    :param tolx: la tolleranza sull incremento
    :param tolf: la tolleranza sul valore della f
    :param nmax: il numero massimo di iterazioni
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """

    def prossimax(x): return x - f(x) / m

    x = prossimax(x0)
    fx = f(x)
    it, xk = 1, [x]
    while it < nmax and abs(fx) >= tolf and abs(f(x) / m) >= tolx * abs(x):
        x = prossimax(x)
        xk.append(x)
        fx = f(x)
        it += 1
    return x, it, xk


def corde_con_derivata(f, df, x0, tolx, tolf, nmax):
    """
    Algoritmo delle per il calcolo dello zero di una funzione con coefficente angolare calcolato con la derivata in x0.

    :param f: la funzione di cui calcolare lo zero
    :param df: la derivata della funzione
    :param x0: il valore di innesco
    :param tolx: la tolleranza sull incremento
    :param tolf: la tolleranza sul valore della f
    :param nmax: il numero massimo di iterazioni
    :return: (zero della funzione, numero di iterazioni, iterazioni)
    """
    return corde(f, df(x0), x0, tolx, tolf, nmax)
