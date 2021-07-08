import numpy as np


def stima_ordine(xks):
    """
    Stima dell'ordine di convergenza di un metodo tramite le sue iterate.

    :param xks: il vettore con le iterate del metodo.
    :return: l'ordine di convergenza del metodo.
    """
    k = len(xks) - 4
    return np.log(abs(xks[k + 3] - xks[k + 2]) / abs(xks[k + 2] - xks[k + 1])) / np.log(
        abs(xks[k + 2] - xks[k + 1]) / abs(xks[k + 1] - xks[k]))
