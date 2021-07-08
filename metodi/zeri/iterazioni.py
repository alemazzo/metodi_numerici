def iterazioni(g, x0, tolx, nmax):
    """
    Algoritmo di iterazione per il calcolo del punto fisso di una funzione.

    :param g: la funzione di cui trovare il punto fisso
    :param x0: il valore di innesco
    :param tolx: la tolleranza
    :param nmax: il numero massimo di iterazioni
    :return: (punto fisso, numero di iterazioni, iterazioni)
    """
    x = g(x0)
    it, xk = 1, [x]
    while it < nmax and abs(x - x0) >= tolx * abs(x):
        x0 = x
        x = g(x)
        xk.append(x)
        it += 1
    return x, it, xk
