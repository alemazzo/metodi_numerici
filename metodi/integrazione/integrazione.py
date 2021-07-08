import numpy as np


def trapezio(f, a, b, n=1):
    """
    Metodo del trapezio per il calcolo integrale
    :param f: la funzione da integrare
    :param a: il lowerbound di integrazione
    :param b: l'upperbound di integrazione
    :param n: il numero di sottointervalli da usare
    :return: il valore dell'integrale approssimato
    """
    h = (b - a) / n
    nodi = np.arange(a, b + h, h)
    fnodi = f(nodi)
    integrale = (h / 2) * (fnodi[0] + 2 * np.sum(fnodi[1:n]) + fnodi[n])
    return integrale


def simpson(f, a, b, n=1):
    """
    Metodo di Simpson per il calcolo integrale
    :param f: la funzione da integrare
    :param a: il lowerbound di integrazione
    :param b: l'upperbound di integrazione
    :param n: il numero di sottointervalli da usare
    :return: il valore dell'integrale approssimato
    """
    h = (b - a) / (2 * n)
    nodi = np.arange(a, b + h, h)
    fnodi = f(nodi)
    integrale = (h / 3) * (fnodi[0] + 2 * np.sum(fnodi[2::2]) + 4 * np.sum(fnodi[1::2]) + fnodi[2 * n])
    return integrale


def integrale(f, a, b, tol, metodo, nmax=2048):
    """
    Calcolo dell'integrale approssimato della funzione f tramite il metodo specificato
    e con la scelta del numero di sottointervalli adattiva in base alla tolleranza.
    :param f: la funzione da integrare
    :param a: il lowerbound di integrazione
    :param b: l'upperbound di integrazione
    :param tol: la tolleranze
    :param metodo: il metodo da utilizzare per l'integrazione
    :param nmax: il massimo numero di sottointervalli
    :return: il valore dell'integrale approssimato con la tolleranza specificata
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
