import numpy as np


def solve_l(L, b):
    """
    Risoluzione di un sistema lineare triangolare inferiore con procedura di sostituzioni in avanti.

    :param L: la matrice triangolare inferiore
    :param b: il vettore dei termini noti
    :return: il vettore x delle incognite e il flag di successo
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
    Risoluzione di un sistema lineare triangolare superiore con procedura di sostituzioni all'indietro.

    :param U: la matrice triangolare superiore
    :param b: il vettore dei termini noti
    :return: il vettore x delle incognite e il flag di successo
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
    Fattorizzazione LU di una matrice senza l'utilizzo del pivoting parziale

    :param A: la matrice da fattorizzare (quadrata)
    :return: le matrici L, U ed il flag di successo
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
    Fattorizzazione LU di una matrice con l'utilizzo del pivoting parziale

    :param A: la matrice da fattorizzare (quadrata)
    :return: le matrici L, U, P ed il flag di successo
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
    Risoluzione di un sistema lineare che è stato fattorizzato con le matrici L, U e P.

    :param L: la matrice L
    :param U: la matrice U
    :param P: la matrice P (nel caso di fattorizzazione senza pivot sarà una matrice identità)
    :param b: il vettore dei termini noti
    :return: il vettore x delle incognite e il flag di successo
    """
    y, flag = solve_l(L, np.dot(P, b))
    return solve_u(U, y)


def solve(A, B, pivot):
    """
    Solve generico di un sistema lineare anche a più dimensioni.

    :param A: la matrice A
    :param B: la matrice contente i vettori dei termini noti nelle colonne
    :param pivot: flag indicante se si vuole utilizzare il pivoting parziale o meno
    :return: la matrice risultante X con i vettori delle incognite nelle colonne
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
