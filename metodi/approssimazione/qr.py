import numpy as np
import scipy.linalg as spl

from ..sistemi import solve_u


def metodo_qr(x, y, n):
    """
    Approssimazine ai minimi quadrati tramite il metodo QR.

    :param x: le ascisse dei punti
    :param y: le ordinate dei punti
    :param n: grado del polinomio approssimante
    :return: il polinomio ottenuto tramite il metodo QR
    """
    H = np.vander(x, n + 1)  # Creo la matrice di vandermonde
    Q, R = spl.qr(H)  # Fattorizzo nelle matrici Q ed R
    Y = np.dot(Q.transpose(), y)
    polinomio, _ = solve_u(R[:n + 1, :], Y[:n + 1])
    return polinomio
