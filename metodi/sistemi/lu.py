import numpy as np


def solve_l(L, b):
    """

    :param L:
    :param b:
    :return:
    """
    m, n = L.shape

    if m != n:
        print("Matrice non quadrata")
        return [], False
    if not np.all(np.diag(L)):
        print("Elemento diagonale nullo")
        return [], False

    x = np.zeros((n, 1))
    for i in range(n):
        s = np.dot(L[i, :i], x[:i])
        x[i] = (b[i] - s) / L[i, i]

    return x, True


def solve_u(U, b):
    """

    :param U:
    :param b:
    :return:
    """
    m, n = U.shape

    if m != n:
        print("Matrice non quadrata")
        return [], False
    if not np.all(np.diag(U)):
        print("Elemento diagonale nullo")
        return [], False

    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / U[i, i]

    return x, True


def fattorizzazione_lu_no_pivot(A):
    """

    :param A:
    :return:
    """
    m, n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [], [], False

    U = A.copy()
    for k in range(n - 1):
        if U[k, k] == 0:
            print("Elemento diagonale nullo")
            return [], [], False
        for i in range(k + 1, n):
            U[i, k] /= U[k, k]
            for j in range(k + 1, n):
                U[i, j] -= U[i, k] * U[k, j]

    L = np.tril(U, -1) + np.eye(n)
    U = np.triu(U)
    return L, U, True


def fattorizzazione_lu_pivot(A):
    """

    :param A:
    :return:
    """

    def swap_rows(M, r1, r2):
        M[[r1, r2], :] = M[[r2, r1], :]

    m, n = A.shape
    if m != n:
        print("Matrice non quadrata")
        return [], [], [], False

    U = A.copy()
    P = np.eye(n)
    for k in range(n - 1):
        if U[k, k] == 0:
            print("Elemento diagonale nullo")
            return [], [], [], False
        for i in range(k + 1, n):
            pivot = k + np.argmax(abs(U[k:, k]))
            if k != pivot:
                swap_rows(U, k, pivot)
                swap_rows(P, k, pivot)
            U[i, k] /= U[k, k]
            for j in range(k + 1, n):
                U[i, j] -= U[i, k] * U[k, j]

    L = np.tril(U, -1) + np.eye(n)
    U = np.triu(U)
    return L, U, P, True


def solve_lu(L, U, P, b):
    """

    :param L:
    :param U:
    :param P:
    :param b:
    :return:
    """
    y, flag = solve_l(L, np.dot(P, b))
    if not flag:
        return [], flag
    return solve_u(U, y)


def solve(A, B, pivot):
    """

    :param A:
    :param B: deve avere i vettori nelle colonne
    :param pivot:
    :return:
    """
    L, U, P, flag = fattorizzazione_lu_pivot(A) if pivot else fattorizzazione_lu_no_pivot(A)
    if min(B.shape) == 1:
        return solve_lu(L, U, P, B)
    m, n = A.shape
    X = np.zeros((n, n))
    B = B.transpose()
    for i in range(B.shape[0]):
        X[i] = solve_lu(L, U, P, B[i]).squeeze(1)
    return X.transpose(), True
