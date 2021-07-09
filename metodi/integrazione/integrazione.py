import numpy as np


def trapezio(f, a, b, n=1):
    """
    Metodo del trapezio per il calcolo integrale.

    :param f: la funzione da integrare
    :param a: il lowerbound di integrazione
    :param b: l'upperbound di integrazione
    :param n: il numero di sottointervalli da usare
    :return: il valore dell'integrale approssimato
    """
    h = (b - a) / n  # dimensione di ogni sottointervallo
    nodi = np.arange(a, b + h, h)  # nodi che dividono il range in n sottointervalli
    fnodi = f(nodi)  # valore della funzione nei nodi divisori
    I = (h / 2) * (fnodi[0] + 2 * np.sum(fnodi[1:n]) + fnodi[n])  # integrale risultante
    return I


def simpson(f, a, b, n=1):
    """
    Metodo di Simpson per il calcolo integrale.

    :param f: la funzione da integrare
    :param a: il lowerbound di integrazione
    :param b: l'upperbound di integrazione
    :param n: il numero di sottointervalli da usare
    :return: il valore dell'integrale approssimato
    """
    h = (b - a) / (2 * n)  # dimensione di ogni sottointervallo considerando che simpson usa un polinomio di grado 2
    nodi = np.arange(a, b + h, h)  # nodi che dividono il range
    fnodi = f(nodi)  # valore della funzione nei nodi divisori
    I = (h / 3) * (fnodi[0] + 2 * np.sum(fnodi[2:2*n:2]) + 4 * np.sum(fnodi[1:2*n:2]) + fnodi[2 * n])  # integrale risutante
    return I


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
    n = 1  # numero di sottointervalli
    I = metodo(f, a, b, n)
    while n <= nmax and err > tol:
        n *= 2  # raddoppio i sottointervalli
        I2 = metodo(f, a, b, n)
        if metodo == trapezio:
            err = np.abs(I2 - I) / 3  # formula dell'errore per il metodo del trapezio
        else:
            err = np.abs(I2 - I) / 15  # formula dell errore per il metodo di Simpson
        I = I2
    return I, n
