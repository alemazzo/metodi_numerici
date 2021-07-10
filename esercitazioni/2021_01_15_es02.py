#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 15:20:56 2021

@author: alessandro
"""

import numpy as np
import scipy.linalg as spl

def lunopivot(A):
    m, n = A.shape
    
    U = A.copy()
    for k in range(n - 1):
        if U[k, k] == 0:
            print("elemento diagonale nullo")
            return [],[], False
        for i in range(k + 1, n):
            U[i, k] /= U[k, k]
            for j in range(k + 1, n):
                U[i, j] -= U[i, k] * U[k, j]
    L = np.tril(U, -1) + np.eye(n)
    U = np.triu(U)
    return L, U, True

def lsolve(L, b):
    m, n = L.shape
    x = np.zeros((n, 1))
    for i in range(n):
        s = np.dot(L[i, :i], x[:i])
        x[i] = (b[i] - s) / L[i, i]
    return x

def usolve(U, b):
    m, n = U.shape
    x = np.zeros((n, 1))
    for i in range(n - 1, -1, -1):
        s = np.dot(U[i, i + 1:], x[i + 1:])
        x[i] = (b[i] - s) / U[i, i]
    return x

def lusolve(A, b):
    L, U, flag = lunopivot(A)
    y = lsolve(L, b)
    x = usolve(U, y)
    return x

def lulusolve(L, U, b):
    y1 = lsolve(L, b)
    y2 = usolve(U, y1)
    y3 = lsolve(L, y2)
    y4 = usolve(U, y3)
    return y4

for n in range(5, 11):
    A = spl.pascal(n)
    b = np.dot(A.T, np.ones((n, 1)))
    c = np.dot(np.dot(A, A), np.ones((n, 1)))
    
    print(f"b = {b}")
    
    s1 = lusolve(A, b).T
    print(f"soluzione 1 = {s1}")
    
    #s2 = lusolve(np.dot(A, A), c).T
    #print(f"soluzione 2 = {s2}")
    
    L, U, flag = lunopivot(A)
    s2 = lulusolve(L, U, c).T
    print(f"soluzione 2 = {s2}")
    
    