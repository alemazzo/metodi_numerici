import numpy as np


def stima_ordine(xks, numero_iterazioni):
    k = numero_iterazioni - 3
    return np.log(abs(xks[k + 3] - xks[k + 2]) / abs(xks[k + 2] - xks[k + 1])) / np.log(
        abs(xks[k + 2] - xks[k + 1]) / abs(xks[k + 1] - xks[k]))
