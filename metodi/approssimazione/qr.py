import numpy as np
import scipy.linalg as spl
from ..sistemi import solve_u

def metodo_qr(x, y, n):
    """

    :param x:
    :param y:
    :param n:
    :return: il polinomio ottenuto tramite il metodo QR
    """
    H = np.vander(x, n + 1) # Creo la matrice di vandermonde
    Q, R = spl.qr(H) # Fattorizzo nelle matrici Q ed R
    Y = np.dot(Q.transpose(), y)
    a, _ = solve_u(R[:n+1, :], Y[0:n+1])
    return a