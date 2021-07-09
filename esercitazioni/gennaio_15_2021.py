#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 16:55:51 2021

@author: alessandro
"""

import math
import numpy as np
import scipy as sp
import scipy.linalg as spl

# a)

def lu_nopivot(A):
    m, n = A.shape
    U = A.copy()
    for k in range(n - 1):
        if U[k, k] == 0:
            return [], [], False
        for i in range(k + 1, n):
            U[i, k] /= U[k, k]
            for j in range(k + 1, n):
                U[i, j] -= U[i, k] * U[k, j]
    L = np.tril(U, -1) + np.eye(n)
    U = np.triu(U)
    return L, U, True

# b)
def solve_u(U, b):
    m, n = U.shape
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / L[i, i]
    return x, True

# c)
def solve_l(L, b):
    m, n = L.shape
    x = np.zeros((n, 1))
    for i in range(n):
        s = np.dot(L[i, :i], x[:i])
        x[i] = (b[i] - s) / L[i, i]
    return x, True

# d)

def lu_solve(L, U, b):
    y, flag = solve_l(L, b)
    return solve_u(U, y)

def lulu_solve(L,U,b):
    #Soluzione del sistema lineare A**2 x= c che equivale a L U L U x =b
    y3, flag = solve_l(L, b)
    y2, flag = solve_u(U, y3)
    y1, flag = solve_l(L, y2)
    x, flag = solve_u(U, y1)
    return x

for n in range(5, 11):
    A = spl.pascal(n)
    b = np.dot(A.transpose(), np.ones((n, 1)))
    c = np.dot(np.dot(A, A), np.ones((n, 1)))
    
    # (A^T)x=b
    L, U, flag = lu_nopivot(A.transpose())
    x1 = lu_solve(L, U, b)[0].transpose()
    print(f"n = {n} => sistema 1 = {x1}")
    
    # (A^2)x=c = LULUx=c
    # Conviene fare LULUx=c invece che A^2x=b 
    # perchè A^2 è molto mal condizionata
    x2 = lulu_solve(L, U, c).transpose()
    xx2 = spl.solve(np.dot(A, A), c)
    print(f"n = {n} => sistema 2 = {xx2}")
    









